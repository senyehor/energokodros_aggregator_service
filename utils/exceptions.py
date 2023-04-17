class LogicException(Exception):
    pass


class LogicExceptionWithMessage(LogicException):
    message: str
