from PySide6.QtWidgets import QMainWindow
from main_widget import MainWidget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Printer Control")
        self.resize(800,800)
        self.setCentralWidget(MainWidget())
