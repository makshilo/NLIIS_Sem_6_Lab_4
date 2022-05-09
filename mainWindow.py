# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lab_4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from animal_signs_logic import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 450)
        MainWindow.setMinimumSize(QtCore.QSize(380, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.send_message)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Dialogue"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Input message"))
        self.pushButton.setText(_translate("MainWindow", "Send message"))

    def send_message(self):
        message = self.lineEdit.text()
        self.textBrowser.append(message+'\n')
        self.lineEdit.clear()

        command_found = False

        if message != '':
            for word in message.split():
                if word in find_synonyms('help'):
                    command_found = True
                    self.textBrowser.append("Example command: find animals by feature aquatic, predator" +
                                            'Also you can get list of features using command: list' + '\n')
                elif word in find_synonyms('find'):
                    command_found = True
                    keywords = find_synonyms('features')
                    for keyword in keywords:
                        if keyword in message:
                            self.execute_command(message.partition(keyword)[2])
                elif word == 'list':
                    command_found = True
                    features = get_header()
                    for feature in features:
                        self.textBrowser.append(feature + '\n')
        else:
            self.textBrowser.append("Please, input message" + '\n')
        if not command_found:
            self.textBrowser.append("Command not recognized" + '\n')

    def execute_command(self, params):
        header = get_header()
        animals_lists = []
        params = params.replace(' ', '')
        for param in params.split(','):
            if param in header:
                animals_lists.append(get_animals(param))
        for animal_list in animals_lists:
            for animal in animal_list:
                self.textBrowser.append(animal)
        self.textBrowser.append('\n')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
