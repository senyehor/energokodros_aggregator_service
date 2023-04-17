class LogicException(Exception):
    pass


class LogicExceptionWithMessage(LogicException):
    message: str

    def __str__(self):
        return f'{super().__str__()}' \
               f'\n' \
               f'{self.message}'
