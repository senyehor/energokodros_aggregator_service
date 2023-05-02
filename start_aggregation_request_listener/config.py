import os
from dataclasses import dataclass

from utils.config_base import RedisChannelMixin


@dataclass
class __StartAggregationRequestListenerConfig(RedisChannelMixin):
    check_request_interval_seconds: int
    start_aggregation_request_message: str


START_AGGREGATION_REQUEST_LISTENER_CONFIG = __StartAggregationRequestListenerConfig(
    channel_name=os.getenv(
        'START_AGGREGATION_REQUEST_LISTENER_LISTEN_CHANNEL_NAME'
    ),
    start_aggregation_request_message=os.getenv(
        'START_AGGREGATION_REQUEST_LISTENER_START_AGGREGATION_MESSAGE'
    ),
    check_request_interval_seconds=int(
        os.getenv(
            'START_AGGREGATION_REQUEST_LISTENER_CHECK_REQUEST_INTERVAL_SECONDS'
        )
    ),
)
