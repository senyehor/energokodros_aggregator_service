from utils.exceptions import LogicExceptionWithMessage


class AggregationAlreadyRunning(LogicExceptionWithMessage):
    message = 'start aggregation request came while aggregation was already running'
