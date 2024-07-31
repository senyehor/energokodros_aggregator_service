from utils.exceptions import LogicException, LogicExceptionWithMessage


class FailedRawRedisMessageDataCast(LogicException):
    pass


class InvalidReceiversCount(LogicExceptionWithMessage):
    def __init__(self, actual_count: int, channel_name: str):
        self.message = f'message to channel {channel_name} expected 1 receiver, got {actual_count}'

    def __str__(self):
        return f'{super().__str__()}' \
               f'\n' \
               f'{self.message}'


class InvalidChannelSubscriberCount(LogicException):
    pass
