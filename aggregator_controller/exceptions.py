from utils.exceptions import LogicException, LogicExceptionWithMessage


class AggregationAlreadyRunning(LogicExceptionWithMessage):
    message = 'start aggregation request came while aggregation was already running'


class AggregationDidNotFinishInTime(LogicException):
    ...
