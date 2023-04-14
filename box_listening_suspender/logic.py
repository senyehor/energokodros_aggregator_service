from box_listening_suspender.commands import get_box_listener_state, update_box_listener_state
from box_listening_suspender.suspender import BoxListeningSuspender
from utils.current_state_retreiver import RedisRawCurrentStateRetriever


def create_redis_box_listener_suspender() -> BoxListeningSuspender:
    return BoxListeningSuspender(
        RedisRawCurrentStateRetriever(update_box_listener_state, get_box_listener_state)
    )
