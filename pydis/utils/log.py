from concurrent_log_handler import ConcurrentRotatingFileHandler
from logging import INFO, getLogger
import os

__log_folder__ = os.getcwd() + os.sep + "logs" + os.sep
log_file = __log_folder__ + os.sep + 'log.txt'

logger = getLogger(__name__)
rotateHandler = ConcurrentRotatingFileHandler(log_file, "a", 512 * 1024, 5)
logger.addHandler(rotateHandler)
logger.setLevel(INFO)