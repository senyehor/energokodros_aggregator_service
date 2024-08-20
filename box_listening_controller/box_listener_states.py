from enum import Enum


class BoxListenerStates(str, Enum):
    STOPPED = 'stopped'
    RUNNING = 'running'
