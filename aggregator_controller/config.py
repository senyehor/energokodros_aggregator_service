import os
from dataclasses import dataclass
from datetime import timedelta

from utils.config_base import RedisChannelMixin


@dataclass
class __AggregatorControllerConfig(RedisChannelMixin):
    start_aggregation_message: str
    aggregator_state_key: str
    aggregation_last_time_run_key: str


AGGREGATOR_CONTROLLER_CONFIG = __AggregatorControllerConfig(
    channel_name=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG_CHANNEL_NAME'
    ),
    start_aggregation_message=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG_START_AGGREGATION_MESSAGE'
    ),
    aggregator_state_key=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG_AGGREGATOR_STATE_KEY'
    ),
    aggregation_last_time_run_key=os.getenv(
        'AGGREGATOR_CONTROLLER_CONFIG_AGGREGATION_LAST_TIME_RUN_KEY'
    )
)

TIMEDELTA_TO_WAIT_UNTIL_AGGREGATION_STARTS = timedelta(seconds=10)
MAX_AGGREGATION_TIME = timedelta(hours=1)
AGGREGATION_FINISHED_CHECK_INTERVAL_SECONDS = 10
