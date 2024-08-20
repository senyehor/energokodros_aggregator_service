from time import sleep

from aggregator_controller.aggregation_start_results import AggregationStartResults
from settings import REDIS
from start_aggregation_request_communicator.config import START_AGGREGATION_REQUEST_LISTENER_CONFIG as _
from utils.commands import Command
from utils.redis.commands import SendRedisMessageCommand


class StartAggregationRequestCommunicator:

    def __init__(self, check_request_came: Command):
        self.__check_request_came_command = check_request_came

    def check_start_aggregation_request_came(self) -> bool:
        return self.__check_request_came_command.execute()

    def notify_on_aggregation_start_result(self, result: AggregationStartResults):
        # todo fix
        SendRedisMessageCommand(
            _.aggregation_start_result_send_channel,
            result,
            REDIS
        ).execute()

    def sleep_for_request_check_delay(self):
        sleep(_.check_request_interval_seconds)
