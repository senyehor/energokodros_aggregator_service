import os
from dataclasses import dataclass

from utils.config_base import RedisChannelMixin


@dataclass
class __BoxListenerControllerConfig(RedisChannelMixin):
    stop_listening_message: str
    resume_listening_message: str
    state_key: str


BOX_LISTENER_CONTROLLER_CONFIG = __BoxListenerControllerConfig(
    channel_name=os.getenv(
        'BOX_LISTENER_CONTROLLER_CONFIG_CHANNEL_NAME'
    ),
    stop_listening_message=os.getenv(
        'BOX_LISTENER_CONTROLLER_CONFIG_STOP_LISTENING_MESSAGE'
    ),
    resume_listening_message=os.getenv(
        'BOX_LISTENER_CONTROLLER_CONFIG_RESUME_LISTENING_MESSAGE'
    ),
    state_key=os.getenv(
        'BOX_LISTENER_CONTROLLER_BOX_LISTENER_STATE_KEY'
    )
)
