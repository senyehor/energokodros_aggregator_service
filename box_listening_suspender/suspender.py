from box_listening_suspender.box_listener_states import BoxListenerStates
from box_listening_suspender.commands import resume_listening, stop_listening
from box_listening_suspender.exceptions import (
    BoxListeningWasNotResumed,
    BoxListeningWasNotSuspended,
)
from utils.current_state_retreiver import (
    RawCurrentStateRetriever, try_convert_raw_state_with_correct_exception,
)


class BoxListeningSuspenderContexManager:
    __state: BoxListenerStates

    def __init__(self, box_listener_state_retriever: RawCurrentStateRetriever):
        self.__state_retriever = box_listener_state_retriever
        self.__update_current_state()

    def __stop_box_listening(self):
        if self.__is_box_listening_running:
            stop_listening.execute()
        self.__update_current_state()
        if self.__is_box_listening_suspended:
            return
        raise BoxListeningWasNotSuspended

    def __resume_box_listening(self):
        if self.__is_box_listening_suspended:
            resume_listening.execute()
        self.__update_current_state()
        if self.__is_box_listening_running:
            return
        raise BoxListeningWasNotResumed

    def __enter__(self):
        self.__stop_box_listening()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__resume_box_listening()

    def __update_current_state(self):
        raw_current_state = self.__state_retriever.get_current_raw_state()
        current_state = try_convert_raw_state_with_correct_exception(
            raw_current_state,
            BoxListenerStates
        )
        self.__state = current_state

    @property
    def __is_box_listening_running(self) -> bool:
        return self.__state == BoxListenerStates.RUNNING

    @property
    def __is_box_listening_suspended(self) -> bool:
        return self.__state == BoxListenerStates.SUSPENDED
