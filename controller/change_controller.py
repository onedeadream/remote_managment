from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.orm import sessionmaker

from model.list_hosts import engine, List_Hosts
from view.change_server_view import Change_Server


class Change_Controller:
    def __init__(self):
        self.change = Change_Server()
        self.create_listView()
        self.saved_host = None
        self.change.select_button.clicked.connect(self.select_server)
        self.change.save_button.clicked.connect(self.save_server)

    def create_listView(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        self.model_1 = QtCore.QStringListModel(self.change)
        list_server = session.query(List_Hosts).all()
        session.close()
        for server in list_server:
            self.change.hostname_list.append(server.host_name)
        self.model_1.setStringList(self.change.hostname_list)
        self.change.server_list.setModel(self.model_1)

    def select_server(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        selected_index = self.change.server_list.currentIndex()
        model = self.change.server_list.model()
        name_host = model.data(selected_index, QtCore.Qt.DisplayRole)
        host = session.query(List_Hosts).filter_by(host_name=name_host).first()
        self.change.input_host_name.setText(f"{host.host_name}")
        self.change.input_ip_address.setText(f"{host.ip_address}")
        self.change.input_mac_address.setText(f"{host.mac_address}")
        self.saved_host = host

    def save_server(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        host_name = self.change.input_host_name.text()
        ip_address = self.change.input_ip_address.text()
        mac_address = self.change.input_mac_address.text()
        self.saved_host.host_name = host_name
        self.saved_host.ip_address = ip_address
        self.saved_host.mac_address = mac_address
        session.commit()
        QMessageBox.information(self.change, 'Оповещение', 'Данные выбранного хоста изменены!')
