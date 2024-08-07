from box_listening_controller.config import BOX_LISTENER_CONTROLLER_CONFIG
from settings import REDIS
from utils.redis.commands import GetRedisValue, SendRedisMessageToOneReceiverCommand

_ = BOX_LISTENER_CONTROLLER_CONFIG

stop_listening = SendRedisMessageToOneReceiverCommand(
    channel=_.channel_name,
    message=_.stop_listening_message,
    r=REDIS
)
resume_listening = SendRedisMessageToOneReceiverCommand(
    channel=_.channel_name,
    message=_.resume_listening_message,
    r=REDIS
)
get_box_listener_state = GetRedisValue(
    value_key=_.state_key,
    r=REDIS
)
