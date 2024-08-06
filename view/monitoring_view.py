from datetime import datetime
import numpy as np
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QMessageBox
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker

from model.list_hosts import List_Hosts
from model.monitoring_info import engine, Monitoring_System


class Monitoring_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ip = None
        self.resize(1000, 500)
        self.setWindowTitle('Данные мониторинга')
        self.setWindowIcon(QIcon("icon.png"))

        layout = QGridLayout()
        self.setLayout(layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas, 0, 0)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        layout.addWidget(self.canvas2, 0, 1)

        self.figure3 = Figure()
        self.canvas3 = FigureCanvas(self.figure3)
        layout.addWidget(self.canvas3, 1, 0)

        self.figure4 = Figure()
        self.canvas4 = FigureCanvas(self.figure4)
        layout.addWidget(self.canvas4, 1, 1)

    def search_data(self):
        Session = sessionmaker(bind=engine)
        session = Session(autoflush=True)
        host = session.query(List_Hosts).filter_by(ip_address=self.ip).one()
        data = None
        try:
            data = session.query(Monitoring_System).filter_by(host_id=host.id).one()
            return data
        except NoResultFound:
            data = None
            return data

    def cpu_stat(self):
        data = self.search_data()
        y = np.array([int(float(row)) for row in data.cpu_percent])
        x = [datetime.strptime(t, "%H:%M:%S") for t in data.time_monitoring]
        plt.gcf().autofmt_xdate()
        self.axes = self.figure.add_subplot(111)
        self.axes.plot(x, y)
        self.axes.set_xlabel('Время')
        self.axes.set_ylabel('Используется CPU')
        self.axes.set_title('Загруженность CPU')
        self.canvas.draw()

    def gpu_stat(self):
        data = self.search_data()
        # Генерируем тестовые данные для графика
        y = np.array([int(float(row)) for row in data.gpu_percent])
        x = [datetime.strptime(t, "%H:%M:%S") for t in data.time_monitoring]
        plt.gcf().autofmt_xdate()
        # Строим график
        self.axes = self.figure2.add_subplot(111)
        self.axes.plot(x, y)
        self.axes.set_xlabel('Время')
        self.axes.set_ylabel('Используется GPU')
        self.axes.set_title('Загруженность GPU')
        self.canvas2.draw()
        # !!!Виртуальная память
    def virtual_memory(self):
        data = self.search_data()
        # Генерируем тестовые данные для графика
        y = np.array([int(float(row)) for row in data.used_virtual_memory])
        x = [datetime.strptime(t, "%H:%M:%S") for t in data.time_monitoring]
        plt.gcf().autofmt_xdate()
        # Строим график
        self.axes = self.figure3.add_subplot(111)
        self.axes.plot(x, y)
        self.axes.set_xlabel('Время')
        self.axes.set_ylabel('Используется Virtual Memory')
        self.axes.set_title('Загруженность Virtual Memory')
        self.canvas3.draw()

    def temp_gpu(self):
        # !!!Температура GPU
        data = self.search_data()
        # Генерируем тестовые данные для графика
        y = np.array([int(float(row)) for row in data.temperature_gpu])
        x = [datetime.strptime(t, "%H:%M:%S") for t in data.time_monitoring]
        plt.gcf().autofmt_xdate()
        # Строим график
        self.axes = self.figure4.add_subplot(111)
        self.axes.plot(x, y)
        self.axes.set_xlabel('Время')
        self.axes.set_ylabel('Температура GPU')
        self.axes.set_title('Температура GPU')
        self.canvas4.draw()

    def set_ip(self, ip_address):
        self.ip = ip_address
        print(f"IP-адрес установлен: {self.ip}")
        if self.search_data() is None:
            QMessageBox.warning(self, 'Ошибка', f"Хост с ip-адресом: {self.ip} еще не проходил процесс мониторинга")
        else:
            self.show()
            self.cpu_stat()
            self.gpu_stat()
            self.virtual_memory()
            self.temp_gpu()
