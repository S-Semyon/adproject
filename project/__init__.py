class UserFlow:
    from .logging import logger
    logger.info("=== (START PROGRAM) ===")
    def __init__(self) -> None:
        from .settings import Settings
        self.settings = Settings("settings.json", logger=self.logger)
        self.settings.save("test", 123)
        a = self.settings.load("test")
        print(a)
        self.logger.info("Иницилизация [CLASS] UserFlow")

    def start(self, *args, **kwargs) -> None:
        pass