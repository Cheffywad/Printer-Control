import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from main_widget import MainWidget

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("Printer Control")
main_window.resize(800,800)
main_window.setCentralWidget(MainWidget())

main_window.show()

app.exec()