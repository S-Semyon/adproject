from project import UserFlow
from project.logging import logger

try:
    UserFlow()
except Exception as e:
    logger.error("Exception", exc_info=True)
    raise e
finally:
    logger.info("=== (END PROGRAM) ===")
