from typing import TypeAlias, TypedDict

from utils.redis.exceptions import FailedRawRedisMessageDataCast

RawRedisMessage: TypeAlias = TypedDict(
    'RawRedisMessage',
    {
        'type':    str,
        'pattern': None | str,
        'channel': bytes,
        'data':    int | bytes
    }
)


class Message:
    def __init__(self, raw_message: RawRedisMessage):
        self.__channel = str(raw_message['channel'])
        self.__raw_message_data = raw_message['data']

    def get_data_as_str(self) -> str:
        try:
            return self.__raw_message_data.decode()
        except ValueError as e:
            raise FailedRawRedisMessageDataCast from e
        except AttributeError as e:
            raise FailedRawRedisMessageDataCast from e

    def get_data_as_int(self) -> int:
        try:
            return int(self.__raw_message_data)
        except ValueError as e:
            raise FailedRawRedisMessageDataCast from e

    @property
    def channel_name(self) -> str:
        return self.__channel
