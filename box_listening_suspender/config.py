import os
from dataclasses import dataclass

from utils.config_base import RedisSendListenChannelsConfig, UpdateStateMessageConfig


@dataclass
class __BoxListenerSuspenderConfig(RedisSendListenChannelsConfig, UpdateStateMessageConfig):
    stop_listening_message: str
    resume_listening_message: str


BOX_LISTENER_SUSPENDER_CONFIG = __BoxListenerSuspenderConfig(
    _channel_base_name=os.getenv(
        'BOX_LISTENER_SUSPENDER_CONFIG.CHANNEL_NAME'
    ),
    update_state_message=os.getenv(
        'BOX_LISTENER_SUSPENDER_CONFIG.UPDATE_STATE_MESSAGE'
    ),
    stop_listening_message=os.getenv(
        'BOX_LISTENER_SUSPENDER_CONFIG.STOP_LISTENING_MESSAGE'
    ),
    resume_listening_message=os.getenv(
        'BOX_LISTENER_SUSPENDER_CONFIG.RESUME_LISTENING_MESSAGE'
    )
)
