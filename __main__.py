from dotenv import load_dotenv

from aggregator_controller import create_redis_aggregator_controller
from box_listening_suspender import create_redis_box_listener_suspender
from start_aggregation_request_listener import create_redis_start_aggregation_request_listener

load_dotenv()


def main():
    start_aggregation_request_listener = create_redis_start_aggregation_request_listener()
    box_listening_suspender = create_redis_box_listener_suspender()
    aggregator_controller = create_redis_aggregator_controller()
    while True:
        if start_aggregation_request_listener.check_start_aggregation_request_came():
            with box_listening_suspender:
                aggregator_controller.start_aggregation()
        else:
            start_aggregation_request_listener.sleep_for_request_check_delay()


if __name__ == '__main__':
    main()
