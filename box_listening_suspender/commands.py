from box_listening_suspender.config import BOX_LISTENER_SUSPENDER_CONFIG
from settings import REDIS
from utils.redis.commands import SendRedisMessageToOneReceiverCommand

_ = BOX_LISTENER_SUSPENDER_CONFIG

stop_listening = SendRedisMessageToOneReceiverCommand(
    channel=_.channel_name,
    message=_.stop_listening_message,
    r=REDIS,
    command_name='stop_box_listening'
)
resume_listening = SendRedisMessageToOneReceiverCommand(
    channel=_.channel_name,
    message=_.resume_listening_message,
    r=REDIS,
    command_name='resume_box_listening'
)
