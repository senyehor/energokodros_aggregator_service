class LogicException(Exception):
    pass


class LogicExceptionWithMessage(LogicException):
    message: str


class StateWasNotUpdated(LogicException):
    pass


class InvalidRawState(LogicException):
    pass
