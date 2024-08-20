from utils.exceptions import LogicException


class BoxListenerAlreadyStopped(LogicException):
    ...


class BoxListenerAlreadyRunning(LogicException):
    ...


class AggregationDidNotStart(LogicException):
    ...
