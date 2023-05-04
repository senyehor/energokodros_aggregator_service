from aggregator_controller.commands import (
    get_aggregator_state, start_aggregation,
)
from aggregator_controller.controller import AggregatorController
from aggregator_controller.states import AggregatorStates
from utils.redis.state import StateReceiver


def create_redis_aggregator_controller() -> AggregatorController:
    aggregator_state_receiver = StateReceiver(get_aggregator_state, AggregatorStates)
    return AggregatorController(
        aggregator_state_receiver,
        start_aggregation
    )
