import sys
from PySide6.QtWidgets import QApplication

from main_window import MainWindow

app = QApplication(sys.argv)
main_window = MainWindow(app)
main_window.show()

app.exec()