import logging

from dotenv import load_dotenv

from aggregator_controller import create_redis_aggregator_controller
from aggregator_controller.aggregation_start_results import AggregationStartResults
from aggregator_controller.exceptions import AggregationDidNotFinishInTime
from box_listening_controller import create_redis_box_listener_controller
from box_listening_controller.exceptions import AggregationDidNotStart
from start_aggregation_request_communicator import \
    create_redis_start_aggregation_request_communicator
from utils.exceptions import LogicException

load_dotenv()

log = logging.getLogger(__name__)


def main():
    start_aggregation_request_communicator = create_redis_start_aggregation_request_communicator()
    box_listening_suspender = create_redis_box_listener_controller()
    aggregator_controller = create_redis_aggregator_controller()
    while True:
        if start_aggregation_request_communicator.check_start_aggregation_request_came():
            try:
                with box_listening_suspender:
                    match aggregator_controller.start_aggregation():
                        case AggregationStartResults.STARTED \
                             | AggregationStartResults.COMPLETED_QUICKLY:
                            start_aggregation_request_communicator. \
                                notify_aggregation_started_or_completed_successfully()
                            aggregator_controller.wait_until_aggregation_is_complete()
                            continue
                        case AggregationStartResults.DID_NOT_START:
                            start_aggregation_request_communicator.notify_aggregation_failed()
                            raise AggregationDidNotStart
            except AggregationDidNotFinishInTime as e:
                log.error(e, exc_info=True)
                exit(1)
            except LogicException as e:
                log.error(e, exc_info=True)
        else:
            start_aggregation_request_communicator.sleep_for_request_check_delay()


if __name__ == '__main__':
    main()
