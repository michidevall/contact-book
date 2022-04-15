import sys
from PyQt5.QtWidgets import QApplication
from .views import Window

def main():
    # create the application
    app = QApplication(sys.argv)
    # create the main window
    win = Window()
    win.show()
    # run the even loop
    sys.exit(app.exec())