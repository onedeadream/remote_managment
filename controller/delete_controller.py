from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from sqlalchemy.orm import sessionmaker

from model.list_hosts import engine, List_Hosts
from view.delete_view import Delete_Server


class Delete_Controller:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.delete = Delete_Server()
        self.create_list_server()
        self.delete.button_delete.clicked.connect(self.delete_server)
        self.session = Session(autoflush=True)

    def create_list_server(self):
        self.model_1 = QtCore.QStringListModel(self.delete)
        list_from_bd = self.session.query(List_Hosts).all()
        self.session.close()
        list_for_server = []
        for server in list_from_bd:
            list_for_server.append(server.host_name)
        self.model_1.setStringList(list_for_server)
        self.delete.list_servers.setModel(self.model_1)

    def delete_server(self):
        selected_index = self.delete.list_servers.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self.delete, 'Ошибка', 'Не выбран ни один из серверов!')
        model = self.delete.list_servers.model()
        name_host = model.data(selected_index, QtCore.Qt.DisplayRole)
        host = self.session.query(List_Hosts).filter_by(host_name=name_host).first()
        self.session.delete(host)
        self.session.commit()
        QMessageBox.information(self.delete, 'Успешно', 'Выбранный сервер был удален!')
