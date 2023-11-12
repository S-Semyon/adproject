from project import UserFlow
from project.logging import logger

try:
    main = UserFlow()
    main.start_edit_script()
except Exception as e:
    logger.error("Exception", exc_info=True)
    raise e
finally:
    logger.info("=== (END PROGRAM) ===")