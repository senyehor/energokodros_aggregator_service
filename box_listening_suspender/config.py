import os
from dataclasses import dataclass

from utils.config_base import RedisChannelMixin


@dataclass
class __BoxListenerSuspenderConfig(RedisChannelMixin):
    stop_listening_message: str
    resume_listening_message: str


BOX_LISTENER_SUSPENDER_CONFIG = __BoxListenerSuspenderConfig(
    channel_name=os.getenv(
        'BOX_LISTENER_SUSPENDER_CONFIG.CHANNEL_NAME'
    ),
    stop_listening_message=os.getenv(
        'BOX_LISTENER_SUSPENDER_CONFIG.STOP_LISTENING_MESSAGE'
    ),
    resume_listening_message=os.getenv(
        'BOX_LISTENER_SUSPENDER_CONFIG.RESUME_LISTENING_MESSAGE'
    )
)
