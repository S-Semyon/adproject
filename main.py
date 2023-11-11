from project import UserFlow
from project.logging import logger

try:
    UserFlow()
except:
    pass
finally:
    logger.info("=== (END PROGRAM) ===")
