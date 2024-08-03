from utils.commands import Command


class BoxListenerController:

    def __init__(self, stop_listening: Command, resume_listening: Command):
        self.__stop_listening = stop_listening
        self.__resume_listening = resume_listening

    def __stop_box_listening(self):
        self.__stop_listening.execute()

    def __resume_box_listening(self):
        self.__resume_listening.execute()

    def __enter__(self):
        self.__stop_box_listening()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__resume_box_listening()
