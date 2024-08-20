import os
from dataclasses import dataclass


@dataclass
class __StartAggregationRequestListenerConfig:
    check_request_interval_seconds: int
    start_aggregation_request_message: str
    aggregation_request_listen_channel: str
    aggregation_start_result_send_channel: str
    aggregation_started_or_completed_successfully_message: str


START_AGGREGATION_REQUEST_LISTENER_CONFIG = __StartAggregationRequestListenerConfig(
    aggregation_request_listen_channel=os.getenv(
        'START_AGGREGATION_REQUEST_LISTENER_LISTEN_CHANNEL'
    ),
    aggregation_start_result_send_channel=os.getenv(
        'START_AGGREGATION_REQUEST_LISTENER_AGGREGATION_START_RESULT_SEND_CHANNEL'
    ),
    aggregation_started_or_completed_successfully_message=os.getenv(
        'AGGREGATION_STARTED_OR_COMPLETED_SUCCESSFULLY_MESSAGE'
    ),
    start_aggregation_request_message=os.getenv(
        'START_AGGREGATION_REQUEST_LISTENER_START_AGGREGATION_MESSAGE'
    ),
    check_request_interval_seconds=int(
        os.getenv(
            'START_AGGREGATION_REQUEST_LISTENER_CHECK_REQUEST_INTERVAL_SECONDS'
        )
    ),
)
