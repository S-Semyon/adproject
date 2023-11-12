import sys
from PyQt5 import QtWidgets, QtCore
from ui import edit_scripts
from .autorun import Ui_MainWindow

class ExampleApp(QtWidgets.QMainWindow, edit_scripts.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.programs: dict[str, list] = {}

        self.add_project.clicked.connect(self.browse_folder_project)
        self.del_project.clicked.connect(self.del_item_project)
        self.add_program.clicked.connect(self.browse_folder_program)
        self.del_program.clicked.connect(self.del_item_program)

        self.list_programs.itemClicked.connect(self.select_program)

        self.comboBox.addItem("Программирование")
        self.comboBox.addItem("Работа с документами")
        self.comboBox.addItem("Играть")
        
    def get_selected_item_name(self) -> str:
        selected_items = self.list_programs.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            return selected_item.text()
        else:
            return None # type: ignore

    def set_args_prg(self, args: str):
        """Установка аргументов для программы"""
        selected_item = self.list_programs.currentItem()
        if selected_item:
            selected_item = self.list_programs.row(selected_item)
            if selected_item not in self.programs:
                self.programs[selected_item] = []
        self.programs[selected_item].append(args)
    
    def del_args_prg(self, args: str):
        """Удаление аргументов для программы"""
        selected_item = self.list_programs.currentItem()
        if selected_item:
            selected_item = self.list_programs.row(selected_item)
            if selected_item not in self.programs:
                self.programs[selected_item] = []
            if args in self.programs[selected_item]:
                self.programs[selected_item].remove(args)

    def del_item_project(self):
        selected_item = self.list_project.currentItem()
        if selected_item:
            self.list_project.takeItem(self.list_project.row(selected_item))
        a = self.comboBox.currentText()
        print(a)

    def browse_folder_project(self):
        selected_item = self.list_programs.currentItem()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if directory:
            self.list_project.addItem(directory)
            selected_item = self.get_selected_item_name()
            if selected_item:
                if selected_item not in self.programs:
                    self.programs[selected_item] = []
                self.programs[selected_item].append(directory)

    def del_item_program(self):
        selected_item = self.list_programs.currentItem()
        if selected_item:
            self.list_programs.takeItem(self.list_programs.row(selected_item))
            self.list_project.clear()

    def browse_folder_program(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")[0]
        if file:
            self.list_programs.addItem(file)
            self.list_programs.setCurrentRow(self.list_programs.count() - 1)
            self.list_project.clear()

    def select_program(self):
        selected_item = self.list_programs.currentItem()
        if selected_item:
            selected_item = self.get_selected_item_name()
            if selected_item not in self.programs:
                self.programs[selected_item] = []
            self.list_project.clear()
            self.list_project.addItems(self.programs[selected_item])

class UserFlow:
    from .logging import logger
    logger.info("=== (START PROGRAM) ===")
    def __init__(self) -> None:
        from .settings import Settings
        self.settings = Settings("settings.json", logger=self.logger)
        self.logger.info("Иницилизация [CLASS] UserFlow")

    def start_edit_script(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        window = ExampleApp()
        window.show()
        sys.exit(app.exec_())

    def starts_script(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow(logger=self.logger)
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())