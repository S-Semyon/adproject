# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_scripts.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        MainWindow.setStyleSheet("background-color: rgb(90, 90, 90);\n"
"font: 9pt \"Arial\";\n"
"color: rgb(223, 223, 223);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(740, 40, 171, 21))
        self.label_2.setStyleSheet("font: 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.create_script = QtWidgets.QPushButton(self.centralwidget)
        self.create_script.setGeometry(QtCore.QRect(830, 550, 150, 35))
        self.create_script.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}")
        self.create_script.setObjectName("create_script")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(680, 350, 300, 35))
        self.comboBox.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.del_script = QtWidgets.QPushButton(self.centralwidget)
        self.del_script.setGeometry(QtCore.QRect(670, 550, 150, 35))
        self.del_script.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}")
        self.del_script.setObjectName("del_script")
        self.script_name = QtWidgets.QLineEdit(self.centralwidget)
        self.script_name.setGeometry(QtCore.QRect(150, 20, 350, 50))
        self.script_name.setAccessibleName("")
        self.script_name.setStyleSheet("border-radius: 8px;\n"
"font: 12pt \"Arial\";\n"
"background-color: rgb(80, 80, 80);\n"
"border-color: #ffffff;")
        self.script_name.setText("")
        self.script_name.setCursorPosition(0)
        self.script_name.setAlignment(QtCore.Qt.AlignCenter)
        self.script_name.setObjectName("script_name")
        self.help_args = QtWidgets.QPushButton(self.centralwidget)
        self.help_args.setGeometry(QtCore.QRect(630, 550, 34, 34))
        self.help_args.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}")
        self.help_args.setObjectName("help_args")
        self.add_program = QtWidgets.QPushButton(self.centralwidget)
        self.add_program.setGeometry(QtCore.QRect(330, 350, 290, 35))
        self.add_program.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}")
        self.add_program.setObjectName("add_program")
        self.del_program = QtWidgets.QPushButton(self.centralwidget)
        self.del_program.setGeometry(QtCore.QRect(330, 400, 290, 35))
        self.del_program.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}")
        self.del_program.setObjectName("del_program")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 460, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.add_project = QtWidgets.QPushButton(self.centralwidget)
        self.add_project.setGeometry(QtCore.QRect(20, 350, 290, 35))
        self.add_project.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}\n"
"")
        self.add_project.setObjectName("add_project")
        self.del_project = QtWidgets.QPushButton(self.centralwidget)
        self.del_project.setGeometry(QtCore.QRect(20, 400, 290, 35))
        self.del_project.setStyleSheet("QPushButton {\n"
"    border-radius:  5px;\n"
"    background-color: rgb(80, 80, 80);\n"
"    color:  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(75, 75, 75);\n"
"}")
        self.del_project.setObjectName("del_project")
        self.list_project = QtWidgets.QListWidget(self.centralwidget)
        self.list_project.setGeometry(QtCore.QRect(20, 90, 290, 240))
        self.list_project.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"border-radius: 10px;")
        self.list_project.setObjectName("list_project")
        self.list_scripts = QtWidgets.QListWidget(self.centralwidget)
        self.list_scripts.setGeometry(QtCore.QRect(680, 90, 290, 240))
        self.list_scripts.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"border-radius: 10px;")
        self.list_scripts.setObjectName("list_scripts")
        self.list_programs = QtWidgets.QListWidget(self.centralwidget)
        self.list_programs.setGeometry(QtCore.QRect(330, 90, 290, 240))
        self.list_programs.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"border-radius: 10px;")
        self.list_programs.setObjectName("list_programs")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(70, 500, 130, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 550, 220, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(380, 500, 130, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(380, 550, 200, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UserFlow - Создание сценария"))
        self.label_2.setText(_translate("MainWindow", "Готовые сценарии"))
        self.create_script.setText(_translate("MainWindow", "Создать сценарий"))
        self.del_script.setText(_translate("MainWindow", "Удалить сценарий"))
        self.script_name.setPlaceholderText(_translate("MainWindow", "Название сценария"))
        self.help_args.setText(_translate("MainWindow", "?"))
        self.add_program.setText(_translate("MainWindow", "Добавить программу"))
        self.del_program.setText(_translate("MainWindow", "Удалить программу"))
        self.label.setText(_translate("MainWindow", "Шаблоны"))
        self.add_project.setText(_translate("MainWindow", "Добавить проект или файл"))
        self.del_project.setText(_translate("MainWindow", "Удалить проект или файл"))
        self.checkBox.setText(_translate("MainWindow", "Таймер отдыха"))
        self.checkBox_2.setText(_translate("MainWindow", "Режим производительности"))
        self.checkBox_3.setText(_translate("MainWindow", "Не беспокоить"))
        self.checkBox_4.setText(_translate("MainWindow", "Режим энергосбережения"))