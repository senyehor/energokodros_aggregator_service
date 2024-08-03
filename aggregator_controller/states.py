from utils.redis.state import StatesBase


class AggregatorStates(StatesBase):
    RUNNING = 'running'
    IDLE = 'idle'
