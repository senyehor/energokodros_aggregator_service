from enum import StrEnum
from typing import Any, Callable, TypeAlias

from utils.commands import Command
from utils.redis.exceptions import InvalidRawState

StatesBase: TypeAlias = StrEnum


class StateReceiver:

    def __init__(self, get_state: Command, state_maker: Callable[[str], Any]):
        self.__get_state = get_state
        self.__state_maker = state_maker

    def get_state(self) -> StatesBase:
        raw_state = self.__get_state.execute()
        try:
            return self.__state_maker(raw_state)
        except ValueError as e:
            raise InvalidRawState(raw_state) from e
