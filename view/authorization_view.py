from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QDialog


class Login_Window(QDialog):
    def __init__(self):
        super().__init__()
        self.login_button = QtWidgets.QPushButton(self)
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_label = QtWidgets.QLabel(self)
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_label = QtWidgets.QLabel(self)
        self.authorization_label = QtWidgets.QLabel(self)
        self.widget = QtWidgets.QWidget(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(410, 401)

        self.login_button.setGeometry(QtCore.QRect(150, 290, 111, 41))
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet("border-radius: 10px; color: white; background-color: #009A63")
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(13)
        self.login_button.setFont(font)

        self.username_input.setGeometry(QtCore.QRect(80, 140, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("border-radius: 10px;")
        self.username_input.setObjectName("username_input")

        self.username_label.setGeometry(QtCore.QRect(80, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(15)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")

        self.password_input.setGeometry(QtCore.QRect(80, 220, 251, 41))
        self.password_input.setStyleSheet("border-radius: 10px;")
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_input.setFont(font)

        self.password_label.setGeometry(QtCore.QRect(80, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(15)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")

        self.authorization_label.setGeometry(QtCore.QRect(120, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.authorization_label.setFont(font)
        self.authorization_label.setObjectName("authorization_label")

        self.widget.setGeometry(QtCore.QRect(0, 0, 411, 401))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet('.QWidget {background-image: url(pictures/fon.png); background-size: cover; background-repeat: no-repeat;}')

        self.widget.raise_()
        self.login_button.raise_()
        self.username_input.raise_()
        self.username_label.raise_()
        self.password_input.raise_()
        self.password_label.raise_()
        self.authorization_label.raise_()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        Dialog.setWindowIcon(QIcon("pictures/icon.png"))
        self.login_button.setText(_translate("Dialog", "Войти"))
        self.username_label.setText(_translate("Dialog", "Логин"))
        self.password_label.setText(_translate("Dialog", "Пароль"))
        self.authorization_label.setText(_translate("Dialog", "Авторизация"))
