import logging

def setup_logging():
    # Configure root logger
    logging.basicConfig(
        level = logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s ",
    )

    # Example get a logger for modules
    logger = logging.getLogger(__name__)
    return logger