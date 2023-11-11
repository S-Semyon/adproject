import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from project import UserFlow, ExampleApp
from project.logging import logger

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

try:
    main()
except Exception as e:
    logger.error("Exception", exc_info=True)
    raise e
finally:
    logger.info("=== (END PROGRAM) ===")