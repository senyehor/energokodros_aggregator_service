from start_aggregation_request_communicator.commands import (
    get_start_aggregation_request_message_from_redis, notify_aggregation_failed,
    notify_aggregation_started_or_completed_successfully,
)
from start_aggregation_request_communicator.communicator import StartAggregationRequestCommunicator


def create_redis_start_aggregation_request_communicator() -> StartAggregationRequestCommunicator:
    return StartAggregationRequestCommunicator(
        get_start_aggregation_request_message_from_redis,
        notify_aggregation_failed,
        notify_aggregation_started_or_completed_successfully
    )
