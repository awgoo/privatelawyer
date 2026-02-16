import time
from core.config import MAX_RETRIES
from core.logger import logger

def retry(func):

    def wrapper(*args, **kwargs):
        for attempt in range(MAX_RETRIES):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.warning(f"Retry {attempt+1} بسبب error: {e}")
                time.sleep(1.5)

        raise Exception("Max retries exceeded")

    return wrapper
