import os
from dataclasses import dataclass
from datetime import timedelta

from utils.config_base import RedisChannelMixin

AGGREGATION_LAST_TIME_RUN_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'
TIMEDELTA_TO_CHECK_WHETHER_AGGREGATION_WAS_RUN_TOO_FAST = timedelta(seconds=5)
BOX_LISTENER_CHANGE_STATE_DELAY_SECONDS = 3


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
