from enum import StrEnum


class AggregationStartResults(StrEnum):
    STARTED = 'started'
    COMPLETED_QUICKLY = 'completed_quickly'
    DID_NOT_START = 'did_not_start'
