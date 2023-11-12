from PyQt5 import QtCore, QtGui, QtWidgets

import pathlib
from pathlib import Path
import os

import asyncio

loop = asyncio.get_event_loop()

class Ui_MainWindow(object):
    def __init__(self, logger) -> None:
        super().__init__()
        self.logger = logger

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        MainWindow.setStyleSheet("background-color: rgb(90, 90, 90);\n"
                                 "font: 9pt \"Arial\";\n"
                                 "color: rgb(223, 223, 223);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.default_1 = QtWidgets.QPushButton(self.centralwidget)
        self.default_1.setGeometry(QtCore.QRect(40, 240, 191, 121))
        self.default_1.setStyleSheet("QPushButton {\n"
                                     "    border-radius:  10px;\n"
                                     "    background-color: rgb(80, 80, 80);\n"
                                     "    color:  rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color:  rgb(75, 75, 75);\n"
                                     "}")
        self.default_1.setObjectName("default_1")
        self.prog_args = QtWidgets.QComboBox(self.centralwidget)
        self.prog_args.setGeometry(QtCore.QRect(580, 130, 290, 30))
        self.prog_args.setStyleSheet("QPushButton {\n"
                                     "    border-radius:  10px;\n"
                                     "    background-color: rgb(80, 80, 80);\n"
                                     "    color:  rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color:  rgb(75, 75, 75);\n"
                                     "}")
        self.prog_args.setObjectName("prog_args")
        self.prog_args.addItem("")
        self.prog_args.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 250, 50))
        self.label.setStyleSheet("font: 15pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.docs = QtWidgets.QPushButton(self.centralwidget)
        self.docs.setGeometry(QtCore.QRect(310, 280, 230, 130))
        self.docs.setStyleSheet("QPushButton {\n"
                                "    border-radius:  10px;\n"
                                "    background-color: rgb(70, 70, 70);\n"
                                "    color:  rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    background-color:  rgb(65, 65, 65);\n"
                                "}")
        self.docs.setObjectName("docs")
        self.gaming = QtWidgets.QPushButton(self.centralwidget)
        self.gaming.setGeometry(QtCore.QRect(310, 440, 230, 130))
        self.gaming.setStyleSheet("QPushButton {\n"
                                  "    border-radius:  10px;\n"
                                  "    background-color: rgb(70, 70, 70);\n"
                                  "    color:  rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed {\n"
                                  "    background-color:  rgb(65, 65, 65);\n"
                                  "}")
        self.gaming.setObjectName("gaming")
        self.programming = QtWidgets.QPushButton(self.centralwidget)
        self.programming.setGeometry(QtCore.QRect(310, 120, 230, 130))
        self.programming.setStyleSheet("QPushButton {\n"
                                       "    border-radius:  10px;\n"
                                       "    background-color: rgb(70, 70, 70);\n"
                                       "    color:  rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:  rgb(65, 65, 65);\n"
                                       "}")
        self.programming.setObjectName("programming")
        self.docs_args = QtWidgets.QComboBox(self.centralwidget)
        self.docs_args.setGeometry(QtCore.QRect(580, 290, 290, 30))
        self.docs_args.setStyleSheet("QPushButton {\n"
                                     "    border-radius:  10px;\n"
                                     "    background-color: rgb(80, 80, 80);\n"
                                     "    color:  rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color:  rgb(75, 75, 75);\n"
                                     "}")
        self.docs_args.setObjectName("docs_argd")
        self.docs_args.addItem("")
        self.docs_args.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.click()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UserFlow - Запуск сценариев"))
        self.prog_args.setItemText(0, _translate("MainWindow", "pyqt5"))
        self.prog_args.setItemText(1, _translate("MainWindow", "Python project"))
        self.docs_args.setItemText(0, _translate("MainWindow", "document"))
        self.docs_args.setItemText(1, _translate("MainWindow", "привет мир"))
        self.default_1.setText(_translate("MainWindow", "Режим по умолчанию"))
        self.label.setText(_translate("MainWindow", "Выберите сценарий"))
        self.docs.setText(_translate("MainWindow", "Работа с документами"))
        self.gaming.setText(_translate("MainWindow", "Играть"))
        self.programming.setText(_translate("MainWindow", "Программирование"))

    def click(self):
        self.default_1.clicked.connect(self.ex)
        self.programming.clicked.connect(self.prog)
        self.gaming.clicked.connect(self.game)
        self.docs.clicked.connect(self.doc)

    def ex(self):
        sys.exit(0)

    def prog(self):
        prog = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.1\\bin\\pycharm64.exe'
        f = ""
        if self.prog_args.currentText() == 'pyqt5':
            f = r'D:\Python\Pycharm_Projects\pyqt5'
        elif self.prog_args.currentText() == 'Python project':
            f = r'D:\Python\Pycharm_Projects\Python_project'
        try:
            from ..script.starter import start_programs
            loop.run_until_complete(start_programs([(prog, f)], logger=self.logger))

        except FileNotFoundError:
            print('Файл не найден')
        except Exception as e:
            raise e

    def doc(self):
        f = ""
        if self.docs_args.currentText() == 'document':
            f = r'C:\Users\ivlev\\OneDrive\Документы\document.docx'
        elif self.docs_args.currentText() == 'привет мир':
            f = 'C:\\Users\\ivlev\\OneDrive\\Документы\\привет_мир.docx'
        try:
            os.system('start ' + f)
        except FileNotFoundError:
            print('Файл не найден')

    def game(self):
        f = r"C:\Program Files (x86)\Steam\steam.exe"
        from ..script.starter import start_programs
        loop.run_until_complete(start_programs([(f, "")], logger=self.logger))


if __name__ == "__main__":
    import sys
    from ..logging import logger
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(logger=logger)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())