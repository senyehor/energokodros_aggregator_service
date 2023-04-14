from box_listening_suspender.config import BOX_LISTENER_SUSPENDER_CONFIG
from settings import REDIS
from utils.redis.commands import GetRedisMessageCommand, SendRedisMessageToOneReceiverCommand

_ = BOX_LISTENER_SUSPENDER_CONFIG

stop_listening = SendRedisMessageToOneReceiverCommand(
    channel=_.channels.send_channel,
    message=_.stop_listening_message,
    r=REDIS,
    command_name='stop_box_listening'
)
resume_listening = SendRedisMessageToOneReceiverCommand(
    channel=_.channels.send_channel,
    message=_.resume_listening_message,
    r=REDIS,
    command_name='resume_box_listening'
)
update_box_listener_state = SendRedisMessageToOneReceiverCommand(
    channel=_.channels.send_channel,
    message=_.update_state_message,
    r=REDIS,
    command_name='update_box_listener_state'
)
get_box_listener_state = GetRedisMessageCommand(
    channel=_.channels.listen_channel,
    r=REDIS,
    command_name='get_box_listener_state'
)
