from dataclasses import dataclass


@dataclass
class RedisChannelMixin:
    channel_name: str
