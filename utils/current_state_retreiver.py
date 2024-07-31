from abc import ABC, abstractmethod
from typing import Any, Callable

from utils.exceptions import InvalidRawState, StateWasNotUpdated
from utils.redis.commands import GetRedisMessageCommand, SendRedisMessageToOneReceiverCommand


class RawCurrentStateRetriever(ABC):
    @abstractmethod
    def get_current_raw_state(self) -> str:
        pass


class RedisRawCurrentStateRetriever(RawCurrentStateRetriever):
    def __init__(
            self, update_state_command: SendRedisMessageToOneReceiverCommand,
            get_state_command: GetRedisMessageCommand
    ):
        self.__update_state_command = update_state_command
        self.__get_state_command = get_state_command

    def get_current_raw_state(self) -> str:
        self.__update_state_command.execute()
        return self.__get_current_stored_raw_state()

    def __get_current_stored_raw_state(self) -> str:
        message = self.__get_state_command.execute()
        if message:
            return message.get_data_as_str()
        raise StateWasNotUpdated(
            f'state was not found after command {self.__update_state_command.command_name}'
        )


def try_convert_raw_state_with_correct_exception(raw_state: str, state_maker: Callable[[str], Any]):
    try:
        return state_maker(raw_state)
    except ValueError as e:
        raise InvalidRawState from e
