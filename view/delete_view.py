from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Delete_Server(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_widget = QtWidgets.QWidget(self)
        self.list_servers = QtWidgets.QListView(self)
        self.label_info = QtWidgets.QLabel(self)
        self.button_delete = QtWidgets.QPushButton(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(400, 328)
        self.setWindowIcon(QIcon('icon.png'))

        self.main_widget.resize(400, 328)
        self.main_widget.setStyleSheet('background-image: url(fon.png)')

        self.list_servers.setGeometry(QtCore.QRect(70, 50, 256, 192))
        self.list_servers.setStyleSheet("border-radius: 10px;")
        self.list_servers.setObjectName("listView")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_servers.setFont(font)

        self.label_info.setGeometry(QtCore.QRect(60, 25, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label")

        self.button_delete.setGeometry(QtCore.QRect(160, 260, 91, 31))
        self.button_delete.setStyleSheet("background-color: red; border-radius: 10px;")
        self.button_delete.setObjectName("pushButton")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Удалить сервер"))
        self.label_info.setText(_translate("Form", "Выберите хост, который хотите удалить"))
        self.button_delete.setText(_translate("Form", "Удалить"))
