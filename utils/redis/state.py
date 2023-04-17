from enum import StrEnum
from typing import Any, Callable

from utils.commands import Command
from utils.exceptions import InvalidRawState

StatesBase = StrEnum


class StateRetriever:

    def __init__(self, get_state: Command, state_maker: Callable[[str], Any]):
        self.__get_state = get_state
        self.__state_maker = state_maker

    def get_state(self) -> StatesBase:
        try:
            return self.__state_maker(self.__get_state.execute())
        except ValueError as e:
            raise InvalidRawState from e
