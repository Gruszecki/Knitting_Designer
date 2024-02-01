from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Knitting Designer')
        self.setMinimumSize(QSize(1280, 720))
