from aggregator_controller.commands import (
    get_aggregator_state, start_aggregation,
    update_aggregator_state,
)
from aggregator_controller.controller import AggregatorController
from utils.current_state_retreiver import RedisRawCurrentStateRetriever


def create_redis_aggregator_controller() -> AggregatorController:
    redis_state_retriever = RedisRawCurrentStateRetriever(
        update_aggregator_state,
        get_aggregator_state
    )
    return AggregatorController(redis_state_retriever, start_aggregation)
