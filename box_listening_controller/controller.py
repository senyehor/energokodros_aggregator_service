from box_listening_controller.box_listener_states import BoxListenerStates
from box_listening_controller.exceptions import BoxListenerAlreadyRunning, BoxListenerAlreadyStopped
from utils.commands import Command
from utils.redis.state import StateReceiver


class BoxListenerController:

    def __init__(
            self, stop_listening: Command, resume_listening: Command,
            box_listener_state_receiver: StateReceiver
    ):
        self.__stop_listening = stop_listening
        self.__resume_listening = resume_listening
        self.__state_receiver = box_listener_state_receiver

    def __stop_box_listening(self):
        state = self.__state_receiver.get_state()
        if state == BoxListenerStates.STOPPED:
            raise BoxListenerAlreadyStopped
        self.__stop_listening.execute()

    def __resume_box_listening(self):
        state = self.__state_receiver.get_state()
        if state == BoxListenerStates.RUNNING:
            raise BoxListenerAlreadyRunning
        self.__resume_listening.execute()

    def __enter__(self):
        self.__stop_box_listening()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__resume_box_listening()
