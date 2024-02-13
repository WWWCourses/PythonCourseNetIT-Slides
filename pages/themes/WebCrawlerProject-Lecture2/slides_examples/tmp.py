import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger.setLevel(logging.DEBUG)

def foo():
    logger.debug(f'debug')
    logger.info(f'info')
    logger.warning(f'warning')
    logger.error(f'error')


foo()