class UserFlow:
    from .logging import logger
    logger.info("=== (START PROGRAM) ===")
    def __init__(self) -> None:
        from .settings import Settings
        self.settings = Settings("settings.json", logger=self.logger)
        self.logger.info("Иницилизация [CLASS] UserFlow")

    def start(self, *args, **kwargs) -> None:
        pass