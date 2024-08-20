from box_listening_controller.commands import (
    get_box_listener_state, resume_listening,
    stop_listening,
)
from box_listening_controller.controller import BoxListenerController


def create_redis_box_listener_controller() -> BoxListenerController:
    return BoxListenerController(stop_listening, resume_listening, get_box_listener_state)
