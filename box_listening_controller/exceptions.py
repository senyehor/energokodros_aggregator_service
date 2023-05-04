from utils.exceptions import LogicException


class BoxListenerAlreadyStopped(LogicException):
    ...


class BoxListenerDidNotStop(LogicException):
    ...


class BoxListenerAlreadyRunning(LogicException):
    ...


class BoxListenerDidNotResume(LogicException):
    ...


class AggregationDidNotStart(LogicException):
    ...
