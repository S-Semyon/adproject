from typing import Any
from .logging import logger as Logger

class Settings:
    def __init__(self, pl, *, logger) -> None:
        import json
        self._json = json
        self._path = pl
        self.logger: Logger = logger # type: ignore

    def _load_json(self):
        with open(self._path, "r") as file:
            data = self._json.load(file)
        return data

    def save(self, cell: Any, arg: Any) -> (Any | None):
        """Сохранить данные в ячейку"""
        data = self._load_json()
        data[cell] = arg
        with open(self._path, "w") as file:
            self._json.dump(data, file, indent=4)
        self.logger.info("[Settings] [save] successfully saved")

    def load(self, cell: Any) -> (Any | None):
        """Загрузить данные из ячейки"""
        data = self._load_json()
        self.logger.info("[Settings] [load] successfully loaded")
        if cell in data:
            return data[cell]
        return None

