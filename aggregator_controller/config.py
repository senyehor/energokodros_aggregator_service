import os
from dataclasses import dataclass

from utils.config_base import RedisChannelMixin


@dataclass
class __AggregatorControllerConfig(RedisChannelMixin):
    start_aggregation_message: str
    aggregator_state_key: str


AGGREGATOR_CONTROLLER_CONFIG = __AggregatorControllerConfig(
    channel_name=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG_CHANNEL_NAME'
    ),
    start_aggregation_message=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG_START_AGGREGATION_MESSAGE'
    ),
    aggregator_state_key=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG_AGGREGATOR_STATE_KEY'
    )
)
