from enum import StrEnum
from typing import Any, Callable

from utils.commands import Command
from utils.redis.exceptions import InvalidRawState

StatesBase = StrEnum


class StateReceiver:

    def __init__(self, get_state: Command):
        self.__get_state = get_state

    def get_state(self, state_maker: Callable[[str], Any]) -> StatesBase:
        try:
            return state_maker(self.__get_state.execute())
        except ValueError as e:
            raise InvalidRawState from e
