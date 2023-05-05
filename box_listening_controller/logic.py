from box_listening_controller.box_listener_states import BoxListenerStates
from box_listening_controller.commands import (
    get_box_listener_state, resume_listening,
    stop_listening,
)
from box_listening_controller.controller import BoxListenerController
from utils.redis.state import StateReceiver


def create_redis_box_listener_controller() -> BoxListenerController:
    return BoxListenerController(
        stop_listening, resume_listening,
        StateReceiver(get_box_listener_state, BoxListenerStates)
    )
