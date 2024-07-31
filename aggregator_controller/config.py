import os
from dataclasses import dataclass

from utils.config_base import RedisSendListenChannelsConfig, UpdateStateMessageConfig


@dataclass
class __AggregatorControllerConfig(RedisSendListenChannelsConfig, UpdateStateMessageConfig):
    start_aggregation_message: str


AGGREGATOR_CONTROLLER_CONFIG = __AggregatorControllerConfig(
    _channel_base_name=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG.CHANNEL_NAME'
    ),
    update_state_message=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG.UPDATE_STATE_MESSAGE'
    ),
    start_aggregation_message=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG.START_AGGREGATION_MESSAGE'
    ),
)
