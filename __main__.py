import logging

from dotenv import load_dotenv

from aggregator_controller import create_redis_aggregator_controller
from aggregator_controller.exceptions import AggregationAlreadyRunning
from box_listening_controller import create_redis_box_listener_controller
from start_aggregation_request_listener import create_redis_start_aggregation_request_listener

load_dotenv()

log = logging.getLogger(__name__)


def main():
    start_aggregation_request_listener = create_redis_start_aggregation_request_listener()
    box_listening_suspender = create_redis_box_listener_controller()
    aggregator_controller = create_redis_aggregator_controller()
    while True:
        if start_aggregation_request_listener.check_start_aggregation_request_came():
            with box_listening_suspender:
                try:
                    aggregator_controller.start_aggregation()
                except AggregationAlreadyRunning as e:
                    log.warning(e.message)
        else:
            start_aggregation_request_listener.sleep_for_request_check_delay()


if __name__ == '__main__':
    main()
