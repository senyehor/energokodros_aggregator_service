import logging

from aggregator_controller.exceptions import AggregationAlreadyRunning
from aggregator_controller.states import AggregatorStates
from utils.commands import Command
from utils.redis.state import StateReceiver

log = logging.getLogger(__name__)


class AggregatorController:
    __aggregator_state: AggregatorStates

    def __init__(
            self, aggregator_state_receiver: StateReceiver,
            start_aggregation_command: Command
    ):
        self.__aggregator_state_receiver = aggregator_state_receiver
        self.__start_aggregation_command = start_aggregation_command

    def start_aggregation(self):
        self.__update_aggregator_state()
        if self.__is_aggregator_running:
            raise AggregationAlreadyRunning
        self.__start_aggregation_command.execute()

    @property
    def __is_aggregator_running(self) -> bool:
        return self.__aggregator_state == AggregatorStates.RUNNING

    def __update_aggregator_state(self):
        # noinspection PyTypeChecker
        self.__aggregator_state = self.__aggregator_state_receiver.get_state()
