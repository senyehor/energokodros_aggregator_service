from redis.client import Redis
from redis.typing import ChannelT

from settings import DEFAULT_TIMEOUT_SECONDS
from utils.commands import Command
from utils.redis.exceptions import InvalidChannelSubscriberCount, InvalidReceiversCount
from utils.redis.message import Message

EXPECTED_MESSAGE_RETRIEVER_COUNT = 1
EXPECTED_CHANNEL_SUBSCRIBER_COUNT = 1


class SendRedisMessageCommand(Command):
    def __init__(
            self, channel: ChannelT, message: str, r: Redis, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.__r = r
        self._channel = channel
        self.__message = message

    def execute(self) -> int:
        """returns receiver count"""
        return self.__r.publish(self._channel, self.__message)


class SendRedisMessageToOneReceiverCommand(SendRedisMessageCommand):

    def execute(self):
        receiver_count = super().execute()
        self.__check_receiver_count_is_one(receiver_count)

    def __check_receiver_count_is_one(self, receiver_count: int):
        if receiver_count != EXPECTED_MESSAGE_RETRIEVER_COUNT:
            raise InvalidReceiversCount(receiver_count, self._channel)


class GetRedisValue(Command):
    def __init__(self, value_key: str, r: Redis, command_name: str):
        super().__init__(command_name)
        self.__value_key = value_key
        self.__r = r

    def execute(self) -> str:
        return self.__r.get(self.__value_key)


class GetRedisMessageCommand(Command):

    def __init__(self, channel: ChannelT, r: Redis, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__channels = r.pubsub()
        self.__subscribe_to_channel(channel)

    def __subscribe_to_channel(self, channel_name: str):
        self.__channels.subscribe(channel_name)
        self.__dump_subscription_info_message()

    def execute(self, timeout_seconds: int = None) -> Message | None:
        return self.__get_message(timeout_seconds)

    def __get_message(self, timeout_seconds: int = None) -> Message | None:
        message = self.__channels.get_message(timeout=timeout_seconds or DEFAULT_TIMEOUT_SECONDS)
        return Message(message) if message else None

    def __dump_subscription_info_message(self):
        """this method must be called right after subscribing to a channel"""
        channel_subscribers_count = self.__get_message().get_data_as_int()
        if channel_subscribers_count != EXPECTED_CHANNEL_SUBSCRIBER_COUNT:
            raise InvalidChannelSubscriberCount
