from aggregator_controller.config import AGGREGATOR_CONTROLLER_CONFIG
from settings import REDIS
from utils.redis.commands import (
    GetRedisValue, SendRedisMessageToOneReceiverCommand,
)

_ = AGGREGATOR_CONTROLLER_CONFIG

start_aggregation = SendRedisMessageToOneReceiverCommand(
    channel=_.channel_name,
    message=_.start_aggregation_message,
    r=REDIS
)
get_aggregator_state = GetRedisValue(
    value_key=_.aggregator_state_key,
    r=REDIS
)
