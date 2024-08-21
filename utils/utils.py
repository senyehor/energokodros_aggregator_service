from datetime import datetime, timedelta
from typing import Callable


def wait_until_func_true(func: Callable[[], bool], delay: timedelta) -> bool:
    max_wait_time = datetime.now() + delay
    while datetime.now() < max_wait_time:
        if func():
            return True
    return False
