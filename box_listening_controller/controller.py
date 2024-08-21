from datetime import timedelta

from box_listening_controller.box_listener_states import BoxListenerStates
from box_listening_controller.config import BOX_LISTENER_CHANGE_STATE_DELAY_SECONDS
from box_listening_controller.exceptions import (
    BoxListenerAlreadyRunning,
    BoxListenerAlreadyStopped, BoxListenerDidNotResume, BoxListenerDidNotStop,
)
from utils.commands import Command
from utils.redis.state import StateReceiver
from utils.utils import wait_until_func_true


class BoxListenerController:

    def __init__(
            self, stop_listening: Command, resume_listening: Command,
            box_listener_state_receiver: StateReceiver
    ):
        self.__stop_listening = stop_listening
        self.__resume_listening = resume_listening
        self.__state_receiver = box_listener_state_receiver

    def __stop_box_listening(self):
        if self.__is_box_listener_stopped:
            raise BoxListenerAlreadyStopped
        self.__stop_listening.execute()
        box_listener_was_stopped = wait_until_func_true(
            lambda: self.__is_box_listener_stopped,
            timedelta(seconds=BOX_LISTENER_CHANGE_STATE_DELAY_SECONDS)
        )
        if not box_listener_was_stopped:
            raise BoxListenerDidNotStop

    def __resume_box_listening(self):
        if self.__is_box_listener_running:
            raise BoxListenerAlreadyRunning
        self.__resume_listening.execute()
        box_listener_was_resumed = wait_until_func_true(
            lambda: self.__is_box_listener_running,
            timedelta(seconds=BOX_LISTENER_CHANGE_STATE_DELAY_SECONDS)
        )
        if not box_listener_was_resumed:
            raise BoxListenerDidNotResume

    def __enter__(self):
        self.__stop_box_listening()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__resume_box_listening()

    @property
    def __is_box_listener_running(self) -> bool:
        return self.__state_receiver.get_state() == BoxListenerStates.RUNNING

    @property
    def __is_box_listener_stopped(self) -> bool:
        return self.__state_receiver.get_state() == BoxListenerStates.STOPPED
