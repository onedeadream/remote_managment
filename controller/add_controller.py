from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.orm import sessionmaker

from model.list_hosts import engine, List_Hosts
from view.add_server_view import Add_Server


class Add_Controller:
    def __init__(self):
        self.add = Add_Server()
        self.add.button_add.clicked.connect(self.add_new_server)

    def add_new_server(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        new_hostname = self.add.input_hostname.text()
        new_ip = self.add.input_ip.text()
        new_mac = self.add.input_mac.text()
        if not new_hostname or not new_ip or not new_mac:
            QMessageBox.warning(self.add, 'Ошибка', 'Некоторые поля не заполнены!')
            self.add.input_hostname.clear()
            self.add.input_ip.clear()
            self.add.input_mac.clear()
        else:
            new_host = List_Hosts(
                host_name=new_hostname,
                ip_address=new_ip,
                mac_address=new_mac
            )
            session.add(new_host)
            session.commit()
            QMessageBox.information(self.add, 'Успешно', 'Новых хост успешно был добавлен!')
