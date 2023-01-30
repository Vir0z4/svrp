import sys
import subprocess
import ctypes
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QTextOption
from PyQt5 import QtWidgets, QtGui

class AutoMod(QtWidgets.QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedSize(475, 240)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.setWindowTitle("Sony VAIO Recovery Patcher (.mod automatic)")
        self.setWindowIcon(QtGui.QIcon("VAIO.ico"))
        self.setGeometry(100, 100, 475, 240)

        self.heading_text = QLabel("Sony VAIO Recovery Patcher (SVRP)", self)
        self.heading_text.setGeometry(12, 10, 500, 30)
        self.heading_text.setStyleSheet("font: 16pt")
        self.heading_text.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.heading_text = QLabel("GUI v2.0.1", self)
        self.heading_text.setGeometry(360, 13, 500, 30)
        self.heading_text.setStyleSheet("font: 8pt")
        
        self.warning_label = QLabel("Please make sure that the path to input and output directory does\nnot contain spaces! Also make sure file names don't contain spaces!", self)
        self.warning_label.setGeometry(12, 42, 500, 35)
        self.warning_label.setStyleSheet("font: 8pt; font-weight:bold;")

        self.input_bar = QLineEdit(self)
        self.input_bar.setGeometry(12, 105, 340, 20)

        self.input_bar_label = QLabel("Input folder with .mod files:", self)
        self.input_bar_label.setGeometry(12, 80, 200, 20)

        self.open_file_button = QPushButton("Open folder", self)
        self.open_file_button.setGeometry(365, 100, 100, 30)
        self.open_file_button.clicked.connect(self.open_file)
        
        self.output_bar = QLineEdit(self)
        self.output_bar.setGeometry(12, 155, 340, 20)

        self.output_bar_label = QLabel("Output folder:", self)
        self.output_bar_label.setGeometry(12, 130, 200, 20)
        
        self.open_file_button_2 = QPushButton("Open folder", self)
        self.open_file_button_2.setGeometry(365, 150, 100, 30)
        self.open_file_button_2.clicked.connect(self.open_file_2)

        self.patch_button = QPushButton("Auto extract", self)
        self.patch_button.setGeometry(365, 200, 100, 30)
        self.patch_button.clicked.connect(self.patch)
        self.patch_button.raise_()
        
        self.auto_label = QLabel("AUTO PATCHER", self)
        self.auto_label.setGeometry(12, 175, 250, 45)
        self.auto_label.setStyleSheet("font: 14pt")
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(420, 5, 50, 20)
        self.back_button.clicked.connect(self.back)

        self.bottom_text = QLabel("2023 • Vir0z4 Network IT", self)
        self.bottom_text.setGeometry(5, 205, 200, 30)
        self.bottom_text.setStyleSheet("font: 7pt")
        self.bottom_text.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_name = QFileDialog.getExistingDirectory(self, "Select folder", "", options=options)
        if folder_name:
            self.input_bar.setText(folder_name)
            
    def open_file_2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_name = QFileDialog.getExistingDirectory(self, "Select folder", "", options=options)
        if folder_name:
            self.output_bar.setText(folder_name)
            
    def back(self):
        self.close()
        self.main_window.show()

    def patch(self):
        input_path = self.input_bar.text()
        output_path = self.output_bar.text()
        
        if not input_path or not output_path:
            QtWidgets.QMessageBox.warning(self, 'Error', "You have not filled one or more of the input bars!")
        else:
            batch_file = "C:\\SVRP\\automodpatcher.bat"
            cmd = ' '.join([batch_file, input_path, output_path])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", '/c '+cmd, None, 1)