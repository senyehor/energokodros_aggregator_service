from aggregator_controller.config import AGGREGATOR_CONTROLLER_CONFIG
from settings import REDIS
from utils.redis.commands import GetRedisMessageCommand, SendRedisMessageToOneReceiverCommand

_ = AGGREGATOR_CONTROLLER_CONFIG

start_aggregation = SendRedisMessageToOneReceiverCommand(
    channel=_.channels.send_channel,
    message=_.start_aggregation_message,
    r=REDIS,
    command_name='start_aggregation'
)
update_aggregator_state = SendRedisMessageToOneReceiverCommand(
    channel=_.channels.send_channel,
    message=_.update_state_message,
    r=REDIS,
    command_name='update_aggregator_state'
)
get_aggregator_state = GetRedisMessageCommand(
    _.channels.listen_channel,
    r=REDIS,
    command_name='get_box_listener_state'
)
