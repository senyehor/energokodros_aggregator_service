from time import sleep

from start_aggregation_request_listener.config import START_AGGREGATION_REQUEST_LISTENER_CONFIG as _
from utils.commands import Command


class StartAggregationRequestListener:

    def __init__(self, check_request_came_command: Command):
        self.__check_request_came_command = check_request_came_command

    def check_start_aggregation_request_came(self) -> bool:
        return self.__check_request_came_command.execute()

    def sleep_for_request_check_delay(self):
        sleep(_.check_request_interval_seconds)
