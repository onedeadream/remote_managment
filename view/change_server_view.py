from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Change_Server(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hostname_list = []
        self.main_widget = QtWidgets.QWidget(self)
        self.server_list = QtWidgets.QListView(self)
        self.select_button = QtWidgets.QPushButton(self)
        self.input_host_name = QtWidgets.QLineEdit(self)
        self.input_ip_address = QtWidgets.QLineEdit(self)
        self.input_mac_address = QtWidgets.QLineEdit(self)
        self.label_hostname = QtWidgets.QLabel(self)
        self.label_ip = QtWidgets.QLabel(self)
        self.label_mac = QtWidgets.QLabel(self)
        self.save_button = QtWidgets.QPushButton(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(498, 300)
        self.setWindowIcon(QIcon('icon.png'))

        self.main_widget.resize(498, 300)
        self.main_widget.setStyleSheet('background-image: url(fon.png);')

        self.server_list.setGeometry(QtCore.QRect(60, 30, 171, 192))
        self.server_list.setObjectName("listView")
        self.server_list.setStyleSheet('border: 0; padding 5px')
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(13)
        self.server_list.setFont(font)

        self.select_button.setGeometry(QtCore.QRect(100, 230, 75, 24))
        self.select_button.setObjectName("pushButton")
        self.select_button.setStyleSheet('border-radius: 10px; background-color: orange;')

        self.input_host_name.setGeometry(QtCore.QRect(300, 50, 170, 40))
        self.input_host_name.setObjectName("lineEdit")
        self.input_host_name.setStyleSheet("border-radius: 10px; padding: 5px;")
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        self.input_host_name.setFont(font)

        self.input_ip_address.setGeometry(QtCore.QRect(300, 110, 170, 40))
        self.input_ip_address.setObjectName("lineEdit_2")
        self.input_ip_address.setStyleSheet("border-radius: 10px; padding: 5px;")
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        self.input_ip_address.setFont(font)

        self.input_mac_address.setGeometry(QtCore.QRect(300, 180, 170, 40))
        self.input_mac_address.setObjectName("lineEdit_3")
        self.input_mac_address.setStyleSheet("border-radius: 10px; padding: 5px;")
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        self.input_mac_address.setFont(font)

        self.label_hostname.setGeometry(QtCore.QRect(300, 30, 101, 16))
        self.label_hostname.setObjectName("label")

        self.label_ip.setGeometry(QtCore.QRect(300, 90, 101, 16))
        self.label_ip.setObjectName("label_2")

        self.label_mac.setGeometry(QtCore.QRect(300, 160, 101, 16))
        self.label_mac.setObjectName("label_3")

        self.save_button.setGeometry(QtCore.QRect(360, 230, 75, 24))
        self.save_button.setObjectName("pushButton_2")
        self.save_button.setStyleSheet('border-radius: 10px; background-color: green')

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Изменить"))
        self.select_button.setText(_translate("Form", "Выбрать"))
        self.label_hostname.setText(_translate("Form", "Название хоста"))
        self.label_ip.setText(_translate("Form", "Ip-адрес"))
        self.label_mac.setText(_translate("Form", "Mac-адрес"))
        self.save_button.setText(_translate("Form", "Сохранить"))
