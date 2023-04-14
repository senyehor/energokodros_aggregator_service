from aggregator_controller.states import AggregatorStates
from utils.commands import Command
from utils.current_state_retreiver import (
    RawCurrentStateRetriever,
    try_convert_raw_state_with_correct_exception,
)


class AggregatorController:  # todo mb make abc for state
    __aggregator_state: AggregatorStates

    def __init__(
            self, aggregator_state_receiver: RawCurrentStateRetriever,
            start_aggregation_command: Command
    ):
        self.__state_receiver = aggregator_state_receiver
        self.__start_aggregation_command = start_aggregation_command

    def start_aggregation(self):
        if self.__is_aggregator_running:
            return
        self.__start_aggregation_command.execute()

    @property
    def __is_aggregator_running(self) -> bool:
        return self.__aggregator_state == AggregatorStates.RUNNING

    @property
    def __is_aggregator_idle(self) -> bool:
        return self.__aggregator_state == AggregatorStates.IDLE

    def __update_current_state(self):
        raw_current_state = self.__state_receiver.get_current_raw_state()
        current_state = try_convert_raw_state_with_correct_exception(
            raw_current_state,
            AggregatorStates
        )
        self.__aggregator_state = current_state
