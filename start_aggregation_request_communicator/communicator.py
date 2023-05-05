from time import sleep

from start_aggregation_request_communicator.config import \
    START_AGGREGATION_REQUEST_LISTENER_CONFIG as _
from utils.commands import Command


class StartAggregationRequestCommunicator:

    def __init__(
            self, check_request_came: Command, notify_aggregation_failed: Command,
            notify_aggregation_started_or_completed_successfully: Command

    ):
        self.__check_request_came_command = check_request_came
        self.__notify_aggregation_failed_command = notify_aggregation_failed
        self.__notify_aggregation_started_or_completed_successfully_command = \
            notify_aggregation_started_or_completed_successfully

    def check_start_aggregation_request_came(self) -> bool:
        return self.__check_request_came_command.execute()

    def notify_aggregation_started_or_completed_successfully(self):
        self.__notify_aggregation_started_or_completed_successfully_command.execute()

    def notify_aggregation_failed(self):
        self.__notify_aggregation_failed_command.execute()

    def sleep_for_request_check_delay(self):
        sleep(_.check_request_interval_seconds)
