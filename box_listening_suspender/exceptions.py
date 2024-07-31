from utils.exceptions import LogicException


class BoxListeningWasNotSuspended(LogicException):
    pass


class BoxListeningWasNotResumed(LogicException):
    pass
