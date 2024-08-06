from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Add_Server(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_widget = QtWidgets.QWidget(self)
        self.input_hostname = QtWidgets.QLineEdit(self)
        self.label_hostname = QtWidgets.QLabel(self)
        self.input_ip = QtWidgets.QLineEdit(self)
        self.label_ip = QtWidgets.QLabel(self)
        self.input_mac = QtWidgets.QLineEdit(self)
        self.label_mac = QtWidgets.QLabel(self)
        self.button_add = QtWidgets.QPushButton(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(398, 358)
        self.setWindowIcon(QIcon('/pictures/icon.png'))

        self.main_widget.resize(398, 358)
        self.main_widget.setStyleSheet('background-image: url(/pictures/fon.png);')

        self.input_hostname.setGeometry(QtCore.QRect(110, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_hostname.setFont(font)
        self.input_hostname.setStyleSheet("border-radius: 10px; padding: 5px;")
        self.input_hostname.setText("")
        self.input_hostname.setObjectName("lineEdit")

        self.label_hostname.setGeometry(QtCore.QRect(110, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.label_hostname.setFont(font)
        self.label_hostname.setObjectName("label_hostname")

        self.input_ip.setGeometry(QtCore.QRect(110, 150, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_ip.setFont(font)
        self.input_ip.setStyleSheet("border-radius: 10px; padding: 5px;")
        self.input_ip.setText("")
        self.input_ip.setObjectName("lineEdit_2")

        self.label_ip.setGeometry(QtCore.QRect(110, 120, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_2")

        self.input_mac.setGeometry(QtCore.QRect(110, 220, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_mac.setFont(font)
        self.input_mac.setStyleSheet("border-radius: 10px; padding: 5px;")
        self.input_mac.setText("")
        self.input_mac.setObjectName("lineEdit_3")

        self.label_mac.setGeometry(QtCore.QRect(110, 190, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(12)
        self.label_mac.setFont(font)
        self.label_mac.setObjectName("label_3")

        self.button_add.setGeometry(QtCore.QRect(160, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("border-radius: 10px; background-color: green;")
        self.button_add.setObjectName("pushButton")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить сервер"))
        self.label_hostname.setText(_translate("Form", "Название хоста"))
        self.label_ip.setText(_translate("Form", "Ip-адрес"))
        self.label_mac.setText(_translate("Form", "Mac-адрес"))
        self.button_add.setText(_translate("Form", "Добавить"))
