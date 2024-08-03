import os
from dataclasses import dataclass

from utils.config_base import RedisChannelMixin


@dataclass
class __BoxListenerControllerConfig(RedisChannelMixin):
    stop_listening_message: str
    resume_listening_message: str


BOX_LISTENER_CONTROLLER_CONFIG = __BoxListenerControllerConfig(
    channel_name=os.getenv(
        'BOX_LISTENER_CONTROLLER_CONFIG.CHANNEL_NAME'
    ),
    stop_listening_message=os.getenv(
        'BOX_LISTENER_CONTROLLER_CONFIG.STOP_LISTENING_MESSAGE'
    ),
    resume_listening_message=os.getenv(
        'BOX_LISTENER_CONTROLLER_CONFIG.RESUME_LISTENING_MESSAGE'
    )
)
