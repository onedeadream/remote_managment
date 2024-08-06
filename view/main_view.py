from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создание виджета
        self.centralWidget = QWidget(self)
        self.info_widget = QWidget(self.centralWidget)
        # Добавление элементов QT на виджет
        self.allServers = QTableWidget(self.centralWidget)
        self.con = QPushButton(self.centralWidget)
        self.on = QPushButton(self.centralWidget)
        self.stat = QPushButton(self.centralWidget)
        self.off = QPushButton(self.centralWidget)
        self.select = QPushButton(self.centralWidget)
        self.start_monitoring = QPushButton(self.centralWidget)
        self.scan = QPushButton(self.centralWidget)
        self.give_system_info = QPushButton(self.centralWidget)
        self.screen = QPushButton(self.centralWidget)
        self.info_about_host = QPushButton(self.centralWidget)
        self.setting_action = QAction('Настройки', self)
        self.exit_action = QAction('Выход', self)
        self.add_server = QAction('Добавить', self)
        self.change_server = QAction('Изменить', self)
        self.delete_server = QAction('Удалить', self)
        self.refresh_server = QAction('Обновить', self)
        # Функции
        self.initUi()
        self.content_name()

    def initUi(self):
        menubar = self.menuBar()
        menubar.setStyleSheet('background-color: #fff; color: black')
        file_menu = menubar.addMenu('Файл')
        server_menu = menubar.addMenu('Сервер')

        file_menu.addAction(self.setting_action)
        file_menu.addAction(self.exit_action)

        server_menu.addAction(self.add_server)
        server_menu.addAction(self.delete_server)
        server_menu.addAction(self.change_server)
        server_menu.addAction(self.refresh_server)

        self.setObjectName("MainWindow")
        self.resize(750, 500)
        # Основной виджет
        self.centralWidget.setGeometry(0, 0, 750, 500)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet('.QWidget {background-image: url(fon.png); background-size: cover; background-repeat: no-repeat;}')
        # Кнопка подключения к серверу
        self.con.setGeometry(635, 40, 50, 50)
        self.con.setObjectName("connect")
        icon = QIcon('../pictures/con.png')
        self.con.setStyleSheet('border-radius: 10px;')
        self.con.setIcon(icon)
        self.con.setIconSize(QSize(50, 50))
        self.con.setToolTip('Подключиться')
        # Кнопка включения компьютера
        self.on.setGeometry(635, 95, 50, 50)
        self.on.setObjectName("on")
        icon = QIcon('on.png')
        self.on.setStyleSheet('border-radius: 10px;')
        self.on.setIcon(icon)
        self.on.setIconSize(QSize(50, 50))
        self.on.setToolTip('Включить')
        # Кнопка выключения компьютера
        self.off.setGeometry(635, 150, 50, 50)
        self.off.setObjectName("off")
        self.off.setStyleSheet('border-radius: 10px;')
        icon = QIcon('off.png')
        self.off.setStyleSheet('border-radius: 10px;')
        self.off.setIcon(icon)
        self.off.setIconSize(QSize(50, 50))
        self.off.setToolTip('Выключить')
        # Кнопка добавления выделения компьютеров
        self.select.setGeometry(635, 420, 100, 30)
        self.select.setObjectName("off")
        self.select.setText("Выбрать")
        self.select.setStyleSheet('background-color: #FFB83E; color: black; border-radius: 10px;')
        # Кнопка вывода состояния компьютера
        self.stat.setGeometry(635, 205, 50, 50)
        self.stat.setObjectName("stat")
        self.stat.setStyleSheet('border-radius: 10px;')
        icon = QIcon('stat.png')
        self.stat.setIcon(icon)
        self.stat.setIconSize(QSize(50, 50))
        self.stat.setToolTip('Мониторинг')
        # Кнопка посылающая сигнал на сервер, о том, что надо начать мониторить хосты
        self.start_monitoring.setGeometry(690, 40, 50, 50)
        self.start_monitoring.setStyleSheet('border-radius: 10px;')
        icon = QIcon('start_monitoring.png')
        self.start_monitoring.setIcon(icon)
        self.start_monitoring.setIconSize(QSize(50, 50))
        self.start_monitoring.setToolTip('Начать мониторинг хостов')
        # Принудительное сканирование
        self.scan.setGeometry(690, 95, 50, 50)
        self.scan.setStyleSheet('border-radius: 10px;')
        icon = QIcon('scan.png')
        self.scan.setIcon(icon)
        self.scan.setIconSize(QSize(50, 50))
        self.scan.setToolTip('Запустить принудительное сканирование')
        # Вывод информации о хосте
        self.info_about_host.setGeometry(635, 315, 50, 50)
        self.info_about_host.setStyleSheet('border-radius: 10px;')
        icon = QIcon('info.png')
        self.info_about_host.setIcon(icon)
        self.info_about_host.setIconSize(QSize(50, 50))
        self.info_about_host.setToolTip('Мониторинг')
        # Подать запрос на получение информации о хостах
        self.give_system_info.setGeometry(690, 150, 50, 50)
        self.give_system_info.setStyleSheet('border-radius: 10px;')
        icon = QIcon('give_system_info.png')
        self.give_system_info.setIcon(icon)
        self.give_system_info.setIconSize(QSize(50, 50))
        self.give_system_info.setToolTip('Получить информацию о хостах')
        # Получение экрана хоста
        self.screen.setGeometry(635, 260, 50, 50)
        self.screen.setStyleSheet('border-radius: 10px;')
        icon = QIcon('screen.png')
        self.screen.setIcon(icon)
        self.screen.setIconSize(QSize(50, 50))
        self.screen.setToolTip('Экран хоста')
        # Таблица серверов
        self.select.setObjectName("allServer")
        self.allServers.setGeometry(20, 40, 600, 300)
        self.allServers.setStyleSheet("QTableWidget {border-radius: 10px; color: white; background-color: transparent}")
        self.allServers.verticalHeader().setVisible(False)

    def content_name(self):
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("Удаленное управление")


