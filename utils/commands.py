from abc import ABC, abstractmethod
from typing import Any


class Command(ABC):
    def __init__(self, command_name: str):
        self.__command_name = command_name

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        ...

    @property
    def command_name(self) -> str:
        return self.__command_name
