import logging
from datetime import datetime

from aggregator_controller.exceptions import (
    AggregationAlreadyRunning,
    AggregationDidNotFinishInTime,
)
from aggregator_controller.states import AggregatorStates
from box_listening_controller.config import (
    AGGREGATION_LAST_TIME_RUN_FORMAT, TIMEDELTA_TO_CHECK_WHETHER_AGGREGATION_WAS_RUN_TOO_FAST,
)
from utils.commands import Command
from utils.redis.state import StateReceiver
from utils.utils import wait_until_func_true
from .aggregation_start_results import AggregationStartResults
from .config import (
    MAX_AGGREGATION_TIME,
    TIMEDELTA_TO_WAIT_UNTIL_AGGREGATION_STARTS,
)

log = logging.getLogger(__name__)


class AggregatorController:
    __aggregator_state: AggregatorStates

    def __init__(
            self, aggregator_state_receiver: StateReceiver,
            start_aggregation_command: Command,
            get_aggregation_run_last_time: Command
    ):
        self.__aggregator_state_receiver = aggregator_state_receiver
        self.__start_aggregation_command = start_aggregation_command
        self.__get_aggregation_run_last_time = get_aggregation_run_last_time

    def start_aggregation(self) -> AggregationStartResults:
        self.__ensure_aggregation_is_not_already_running()
        self.__start_aggregation_command.execute()
        now = datetime.now()
        if self.__check_aggregation_started(now):
            return AggregationStartResults.STARTED
        if self.__check_aggregation_completed_quickly(now):
            return AggregationStartResults.COMPLETED_QUICKLY
        return AggregationStartResults.DID_NOT_START

    def wait_until_aggregation_is_complete(self):
        aggregation_finished_within_time = wait_until_func_true(
            lambda: self.__is_aggregator_idle,
            MAX_AGGREGATION_TIME
        )
        if not aggregation_finished_within_time:
            raise AggregationDidNotFinishInTime

    def __check_aggregation_started(self, now: datetime) -> bool:
        max_time_to_wait_until_aggregation_starts = \
            now + TIMEDELTA_TO_WAIT_UNTIL_AGGREGATION_STARTS
        while datetime.now() < max_time_to_wait_until_aggregation_starts:
            if self.__is_aggregator_running:
                return True

    def __check_aggregation_completed_quickly(
            self, time_start_aggregation_request_was_sent: datetime
    ) -> bool:
        aggregation_last_time_run_raw: str = self.__get_aggregation_run_last_time.execute()
        aggregation_last_time_run = datetime.strptime(
            aggregation_last_time_run_raw,
            AGGREGATION_LAST_TIME_RUN_FORMAT
        )
        difference = time_start_aggregation_request_was_sent - aggregation_last_time_run
        return difference < TIMEDELTA_TO_CHECK_WHETHER_AGGREGATION_WAS_RUN_TOO_FAST

    def __ensure_aggregation_is_not_already_running(self):
        if self.__is_aggregator_running:
            raise AggregationAlreadyRunning

    @property
    def __is_aggregator_running(self) -> bool:
        return self.__aggregator_state_receiver.get_state() == AggregatorStates.RUNNING

    @property
    def __is_aggregator_idle(self) -> bool:
        return self.__aggregator_state_receiver.get_state() == AggregatorStates.IDLE
