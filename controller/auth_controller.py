import socket
from PyQt5.QtWidgets import QMessageBox
from config import IP_ADDR, PORT
from controller.main_controller import Main_Controller
from view.authorization_view import Login_Window


class Auth_Controller:
    def __init__(self):
        self.auth = Login_Window()
        self.auth.login_button.clicked.connect(self.handle_login)
        self.main_controller = None

    def handle_login(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP_ADDR, PORT))
        username = self.auth.username_input.text()
        password = self.auth.password_input.text()
        client.send(f"auth: {username}, {password}".encode())
        data = client.recv(1024)
        if data.decode() == 'accept':  # Replace with your own validation
            self.auth.hide()
            self.main_controller = Main_Controller()
            self.main_controller.view.show()
        else:
            QMessageBox.warning(self.auth, 'Ошибка', 'Неправильно введены данные')
            self.auth.username_input.clear()
            self.auth.password_input.clear()
        client.close()