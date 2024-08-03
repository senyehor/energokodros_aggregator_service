from settings import REDIS
from utils.commands import Command
from utils.redis.commands import GetRedisMessageCommand
from utils.redis.message import Message
from .config import START_AGGREGATION_REQUEST_LISTENER_CONFIG as _
from .exceptions import ReceivedMessageIsNotCorrectStartAggregationRequest


class __StartAggregationRequestRedisCheckerCommand(Command):

    def __init__(
            self, start_aggregation_request_message: str,
            get_start_aggregation_request_command: Command, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.__get_start_aggregation_request_command = get_start_aggregation_request_command
        self.__start_aggregation_request_message = start_aggregation_request_message

    def execute(self, *args, **kwargs) -> bool:
        message = self.__get_start_aggregation_request_command.execute()
        if message:
            self.__ensure_start_aggregation_message_is_valid(message)
            return True
        return False

    def __ensure_start_aggregation_message_is_valid(self, message: Message):
        data = message.get_data_as_str()
        if data != self.__start_aggregation_request_message:
            raise ReceivedMessageIsNotCorrectStartAggregationRequest


__get_start_aggregation_request_command = GetRedisMessageCommand(
    _.channel_name, REDIS, command_name='get_start_aggregation_request_command'
)

get_start_aggregation_request_message_from_redis = __StartAggregationRequestRedisCheckerCommand(
    start_aggregation_request_message=_.start_aggregation_request_message,
    get_start_aggregation_request_command=__get_start_aggregation_request_command,
    command_name='get_start_aggregation_request_message_from_redis',
)
