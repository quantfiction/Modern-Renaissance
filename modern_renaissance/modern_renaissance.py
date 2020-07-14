"""Main module."""
import logging
from modern_renaissance.log import logger_init

logger = logging.getLogger(__name__)


def test_logger():
    logger.info("test info")
    logger.log(22, "test start")
    logger.log(44, "test complete")


if __name__ == "__main__":
    test_logger()
