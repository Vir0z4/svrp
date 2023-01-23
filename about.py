import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5 import QtWidgets

class AboutDialog(QtWidgets.QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedSize(300, 150)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.setWindowTitle("About SVRP")
        self.setGeometry(100, 100, 300, 150)

        self.header_text = QLabel("About SVRP", self)
        self.header_text.setGeometry(10, 10, 280, 30)
        self.header_text.setStyleSheet("font: 12pt")
        self.header_text.setAlignment(Qt.AlignCenter)

        self.under_header_text = QLabel("Sony VAIO Recovery Patcher is a program developed\nby the VAIO Library team.", self)
        self.under_header_text.setGeometry(10, 40, 280, 30)
        self.under_header_text.setAlignment(Qt.AlignCenter)
        
        self.under_header_text_2 = QLabel("SVRP is a utility designed to patch and combine\nsplit WIM (.sny) and .mod files from Sony VAIO\nrecoveries, in order to bypass Sony's model checks.", self)
        self.under_header_text_2.setGeometry(10, 70, 280, 50)
        self.under_header_text_2.setAlignment(Qt.AlignCenter)

        self.back_button = QPushButton("Close", self)
        self.back_button.setGeometry(245, 8, 50, 20)
        self.back_button.clicked.connect(self.run_script1)
        
        self.github_button = QPushButton("GitHub", self)
        self.github_button.setGeometry(245, 125, 50, 20)
        self.github_button.clicked.connect(self.run_script2)
        
        self.github_button = QPushButton("VAIO Library", self)
        self.github_button.setGeometry(165, 125, 75, 20)
        self.github_button.clicked.connect(self.run_script3)
        
        self.bottom_text = QLabel("GUI v2.0", self)
        self.bottom_text.setGeometry(5, 115, 100, 30)
        self.bottom_text.setStyleSheet("font: 7pt")
        self.bottom_text.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

    def run_script1(self):
        self.close()
        
    def run_script2(self):
        url = QUrl("https://github.com/Vir0z4/svrp")
        QDesktopServices.openUrl(url)
        
    def run_script3(self):
        url = QUrl("https://vaiolibrary.com")
        QDesktopServices.openUrl(url)