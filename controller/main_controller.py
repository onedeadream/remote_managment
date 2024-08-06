import os
import socket
import threading
import time
import paramiko
import ping3
import pyautogui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QLabel
from sqlalchemy.orm import sessionmaker
from vidstream import StreamingServer

from controller.add_controller import Add_Controller
from controller.change_controller import Change_Controller
from controller.delete_controller import Delete_Controller
from config import SSH_USER, SSH_PASSWORD, IP_ADDR, PORT
from model.list_hosts import engine, List_Hosts
from view.main_view import MainWindow
from view.monitoring_view import Monitoring_Widget


def thread_screen_server():
    server_stream = StreamingServer(IP_ADDR, 9999)
    server_stream.start_server()
    while input('') != 'STOP':
        continue
    server_stream.stop_server()


class Main_Controller:
    def __init__(self):
        self.view = MainWindow()
        self.monitoring = None
        self.change_controller = None
        self.add_controller = None
        self.delete_controller = None
        self.create_table()
        self.view.add_server.triggered.connect(self.add_server)
        self.view.delete_server.triggered.connect(self.delete_server)
        self.view.change_server.triggered.connect(self.change_data_server)
        self.view.refresh_server.triggered.connect(self.create_table)
        self.view.con.clicked.connect(self.connected)
        self.view.off.clicked.connect(self.pc_off)
        self.view.select.clicked.connect(self.select_server)
        self.view.stat.clicked.connect(self.monitoring_info)
        self.view.screen.clicked.connect(self.screen_stream)
        self.view.give_system_info.clicked.connect(self.give_system_info)
        self.view.scan.clicked.connect(self.make_scan)
        self.view.start_monitoring.clicked.connect(self.start_monitoring)
        self.view.info_about_host.clicked.connect(self.info_host)

    def add_server(self):
        self.add_controller = Add_Controller()
        self.add_controller.add.show()

    def change_data_server(self):
        self.change_controller = Change_Controller()
        self.change_controller.change.show()

    def delete_server(self):
        self.delete_controller = Delete_Controller()
        self.delete_controller.delete.show()

    def info_host(self):
        self.view.resize(1050, 500)
        self.view.centralWidget.resize(1050, 500)
        self.view.info = QLabel(self.view.centralWidget)
        self.view.info.setGeometry(770, 520, 300, 300)
        self.view.info.setStyleSheet('background-color: white')
        self.view.info.setText('Привет')

    def start_monitoring(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_ADDR, PORT))
        client.send('start monitoring'.encode())

    def make_scan(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_ADDR, PORT))
        client.send('nmap'.encode())

    def give_system_info(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_ADDR, PORT))
        client.send('give system info'.encode())

    def screen_stream(self):
        selected_row = self.view.allServers.currentRow()
        ip = self.view.allServers.item(selected_row, 1)
        take_ip = ip.text()

        thread = threading.Thread(target=thread_screen_server)
        thread.start()

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_ADDR, PORT))
        client.send(f'screen: {take_ip}'.encode())

    def monitoring_info(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        self.monitoring = Monitoring_Widget()
        selected_row = self.view.allServers.currentRow()
        if selected_row == -1:
            return
        name_item = self.view.allServers.item(selected_row, 0)
        if name_item is None:
            QMessageBox.warning(self.view.centralWidget, 'Ошибка', 'Не выбран ни один из элементов')
        name = name_item.text()
        host = session.query(List_Hosts).filter_by(host_name=name).first()
        session.close()
        self.monitoring.set_ip(host.ip_address)

    def create_table(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        servers = session.query(List_Hosts).all()
        countRow = len(servers)
        self.view.allServers.setRowCount(countRow)
        self.view.allServers.setColumnCount(4)
        self.view.allServers.setColumnWidth(0, 150)
        self.view.allServers.setColumnWidth(1, 150)
        self.view.allServers.setColumnWidth(2, 150)
        self.view.allServers.setColumnWidth(3, 150)
        list_row = ['Название', 'Ip-адрес', 'Mac-адрес', 'Статус']
        header_stylesheet = """
        QHeaderView::section {
            background-color: #003860;  /* Цвет фона */
            color: white; 
        }
        """
        self.view.allServers.horizontalHeader().setStyleSheet(header_stylesheet)
        self.view.allServers.setHorizontalHeaderLabels(list_row)
        self.view.allServers.setShowGrid(False)
        tableRow = 0
        for server in servers:
            self.view.allServers.setItem(tableRow, 0, QTableWidgetItem(f"{server.host_name}"))
            self.view.allServers.setItem(tableRow, 1, QTableWidgetItem(f"{server.ip_address}"))
            self.view.allServers.setItem(tableRow, 2, QTableWidgetItem(f"{server.mac_address}"))
            self.view.allServers.setItem(tableRow, 3, QTableWidgetItem(f"{self.checkPc(server.ip_address)}"))
            tableRow += 1

        for row in range(len(servers)):
            item = self.view.allServers.item(row, 0)  # Второй столбец имеет индекс 1
            item.setBackground(QColor('#3FB0FF'))

        for row in range(len(servers)):
            item = self.view.allServers.item(row, 1)  # Второй столбец имеет индекс 1
            item.setBackground(QColor('#2993FC'))

        for row in range(len(servers)):
            item = self.view.allServers.item(row, 2)  # Второй столбец имеет индекс 1
            item.setBackground(QColor('#0070C0'))

        for row in range(len(servers)):
            item = self.view.allServers.item(row, 3)  # Второй столбец имеет индекс 1
            item.setBackground(QColor('#004D84'))

    def checkPc(self, ip):
        response = ping3.ping(ip)
        if response:
            return "Включен"
        else:
            return "Выключен"

    def select_server(self):
        number_of_server = self.view.allServers.rowCount()
        self.view.allServers.insertColumn(4)
        self.view.allServers.setGeometry(20, 20, 640, 300)
        self.view.allServers.setColumnWidth(4, 20)
        self.view.allServers.setHorizontalHeaderItem(4, QTableWidgetItem(""))
        for i in range(number_of_server):
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            checkbox.setTextAlignment(Qt.AlignCenter)
            self.view.allServers.setItem(i, 4, checkbox)

    def pc_off(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        selected_row = self.view.allServers.currentRow()
        name_item = self.view.allServers.item(selected_row, 0)
        name = name_item.text()
        connect_pc = session.query(List_Hosts).filter(host_name=f'{name}').one()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=f'{connect_pc.ip}', username=f'{SSH_USER}',
                   password=f'{SSH_PASSWORD}', port=22)
        client.exec_command('shutdown -s')
        client.close()

    def pc_on(self):
        selected_row = self.view.allServers.currentRow()
        mac_address_item = self.view.allServers.item(selected_row, 2)
        mac_address = mac_address_item.text()
        ip_address_item = self.view.allServers.item(selected_row, 1)
        ip_address = ip_address_item.text()
        mac_bytes = bytes.fromhex(mac_address.replace(':', ''))
        wol_packet = b'\xff' * 6 + mac_bytes * 16
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(wol_packet, (ip_address, 9))

    def connected(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        # Получаем выделенный элемент
        selected_row = self.view.allServers.currentRow()
        # Получаем id элемента
        name = self.view.allServers.item(selected_row, 0).text()
        ip = self.view.allServers.item(selected_row, 1).text()
        connect_pc = session.query(List_Hosts).filter(List_Hosts.namePc == f'{name}').one()
        os.system(f"start cmd /K ssh {SSH_USER}@{connect_pc.ip}")
        pyautogui.hotkey('alt', 'tab')
        time.sleep(2)
        pyautogui.typewrite(f'{SSH_PASSWORD}')
        time.sleep(1)
        pyautogui.press('enter')
