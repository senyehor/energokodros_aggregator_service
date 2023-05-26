from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from .commands import start_aggregation as start_aggregation_command
from .config import HOUR_AUTOMATICALLY_RUN_AGGREGATION_AT


def setup_autostart_at_hour_zero_to_twenty_three(hour: int = HOUR_AUTOMATICALLY_RUN_AGGREGATION_AT):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        start_aggregation,
        'cron',
        hour=str(hour)
    )
    scheduler.start()


def start_aggregation():
    start_aggregation_command.execute()


def check_aggregation_autostart_caused_aggregation_already_running(
        hour: int = HOUR_AUTOMATICALLY_RUN_AGGREGATION_AT
):
    now = datetime.now()
    return now.hour == hour and now.minute == 0
