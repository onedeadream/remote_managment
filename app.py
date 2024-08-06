import sys
from PyQt5.QtWidgets import QApplication
from controller.auth_controller import Auth_Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth = Auth_Controller()
    auth.auth.show()
    sys.exit(app.exec_())