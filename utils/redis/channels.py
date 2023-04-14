class ListenRedisChannel:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name


class SendRedisChannel:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name


class SendListenRedisChannels:
    __send_channel_postfix = '_send'
    __listen_channel_postfix = '_listen'

    def __init__(self, channel_base_name: str):
        self.__send_channel = SendRedisChannel(channel_base_name + self.__send_channel_postfix)
        self.__listen_channel = ListenRedisChannel(channel_base_name + self.__listen_channel_postfix)

    @property
    def send_channel(self) -> SendRedisChannel:
        return self.__send_channel

    @property
    def listen_channel(self) -> ListenRedisChannel:
        return self.__listen_channel
