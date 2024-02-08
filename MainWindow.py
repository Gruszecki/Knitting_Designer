from random import choice, choices

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QHBoxLayout, QWidget, QGridLayout, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Knitting Designer')
        # self.setMinimumSize(QSize(1280, 720))

        self.label = QLabel('...')

        self.button_1 = QPushButton()
        self.button_2 = QPushButton()
        self.button_3 = QPushButton()

        # self.button.clicked.connect(self.button_was_clicked)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.button_3)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def mouseReleaseEvent(self, event):
        self.label.setText('Mouse released')
        print(event)

    def mouseMoveEvent(self, event):
        self.label.setText(f'Tracking {event.globalX()}')