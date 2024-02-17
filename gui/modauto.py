import ctypes
import re
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class AutoMod(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedSize(475, 240)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        self.setWindowTitle("Sony VAIO Recovery Patcher (.mod automatic)")
        self.setWindowIcon(QIcon("VAIO.ico"))

        self.heading_text = QLabel("Sony VAIO Recovery Patcher (SVRP)", self)
        self.heading_text.setGeometry(12, 10, 500, 30)
        self.heading_text.setStyleSheet("font: 16pt")
        self.heading_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
        self.heading_text = QLabel("GUI v2.0.2", self)
        self.heading_text.setGeometry(367, 0, 500, 30)
        self.heading_text.setStyleSheet("font: 8pt")
        
        self.warning_label = QLabel("Please make sure that file names don't contain spaces!\nIf they do, please manually rename the files.", self)
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
        
        self.auto_label = QLabel("AUTO PATCHER", self)
        self.auto_label.setGeometry(12, 175, 250, 45)
        self.auto_label.setStyleSheet("font: 14pt")
        
        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(420, 5, 50, 20)
        self.back_button.clicked.connect(self.back)

        self.bottom_text = QLabel("© 2024 Vir0z4 Network IT", self)
        self.bottom_text.setGeometry(5, 205, 200, 30)
        self.bottom_text.setStyleSheet("font: 7pt")
        self.bottom_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)

    def open_file(self):
        options = QFileDialog.Option.ReadOnly
        folder_name = QFileDialog.getExistingDirectory(self, "Select folder", options=options)
        if folder_name:
            self.input_bar.setText(folder_name)
            
    def open_file_2(self):
        options = QFileDialog.Option.ReadOnly
        folder_name = QFileDialog.getExistingDirectory(self, "Select folder", options=options)
        if folder_name:
            self.output_bar.setText(folder_name)
            
    def back(self):
        self.close()
        self.main_window.show()

    def patch(self):
        input_path = self.input_bar.text()
        output_path = self.output_bar.text()
        
        if not input_path or not output_path:
            QMessageBox.warning(self, 'Error', "You have not filled one or more of the input bars!")
        elif has_spaces(input_path):
            QMessageBox.warning(self, 'Error', "Your input path contains spaces!")
        elif has_spaces(output_path):
            QMessageBox.warning(self, 'Error', "Your output path contains spaces!")
        else:
            batch_file = r"C:\SVRP\automodpatcher.bat"
            cmd = ' '.join([batch_file, input_path, output_path])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", '/c '+cmd, None, 1)

def has_spaces(string):
    return bool(re.search(r"\s", string))