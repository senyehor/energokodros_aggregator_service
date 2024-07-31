from dataclasses import dataclass

from utils.redis import SendListenRedisChannels
from utils.redis.channels import ListenRedisChannel


@dataclass
class RedisListenChannelConfigMixin:
    _channel_base_name: str

    def __post_init__(self):
        self.__channel = ListenRedisChannel(self._channel_base_name)

    @property
    def listen_channel(self) -> ListenRedisChannel:
        return self.__channel


@dataclass
class RedisSendListenChannelsConfig:
    _channel_base_name: str

    def __post_init__(self):
        self.__channels = SendListenRedisChannels(self._channel_base_name)

    @property
    def channels(self) -> SendListenRedisChannels:
        return self.__channels


@dataclass
class UpdateStateMessageConfig:
    update_state_message: str
