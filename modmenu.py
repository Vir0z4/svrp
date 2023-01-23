import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui

class ModMenu(QtWidgets.QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedSize(300, 150)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.setWindowTitle("Sony VAIO Recovery Patcher")
        self.setWindowIcon(QtGui.QIcon("VAIO.ico"))
        self.setGeometry(100, 100, 300, 150)

        self.header_text = QLabel(".mod extraction", self)
        self.header_text.setGeometry(10, 10, 280, 30)
        self.header_text.setStyleSheet("font: 12pt")
        self.header_text.setAlignment(Qt.AlignCenter)

        self.under_header_text = QLabel(".mod extraction methods:", self)
        self.under_header_text.setGeometry(10, 40, 280, 30)
        self.under_header_text.setAlignment(Qt.AlignCenter)
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(245, 8, 50, 20)
        self.back_button.clicked.connect(self.back)

        self.left_button = QPushButton("Automatic extraction", self)
        self.left_button.setFixedSize(140, 50)
        self.left_button.move(10, 75)
        self.left_button.clicked.connect(self.run_script1)
        self.right_button = QPushButton("Manual extraction", self)
        self.right_button.setFixedSize(140, 50)
        self.right_button.move(150, 75)
        self.right_button.clicked.connect(self.run_script2)
        
        self.bottom_text = QLabel("GUI v2.0", self)
        self.bottom_text.setGeometry(5, 115, 100, 30)
        self.bottom_text.setStyleSheet("font: 7pt")
        self.bottom_text.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

    def run_script1(self):
        import modauto
        modauto_dialog = modauto.AutoMod(self.main_window)
        self.close()
        modauto_dialog.exec_()

    def run_script2(self):
        import mod
        mod_dialog = mod.ManualMod(self.main_window)
        self.close()
        mod_dialog.exec_()
        
    def back(self):
        self.close()
        self.main_window.show()