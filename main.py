import sys
import subprocess
import win32api
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5 import QtWidgets

class SVRP(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 180)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.setWindowTitle("Sony VAIO Recovery Patcher")
        self.setGeometry(100, 100, 300, 150)

        self.header_text = QLabel("Sony VAIO Recovery Patcher (SVRP)", self)
        self.header_text.setGeometry(10, 10, 280, 30)
        self.header_text.setStyleSheet("font: 12pt")
        self.header_text.setAlignment(Qt.AlignCenter)

        self.under_header_text = QLabel("Select type of file you wish to patch:", self)
        self.under_header_text.setGeometry(10, 40, 280, 30)
        self.under_header_text.setAlignment(Qt.AlignCenter)

        self.left_button = QPushButton(".sny", self)
        self.left_button.setFixedSize(140, 50)
        self.left_button.move(10, 75)
        self.left_button.clicked.connect(self.run_script1)
        self.right_button = QPushButton(".mod", self)
        self.right_button.setFixedSize(140, 50)
        self.right_button.move(150, 75)
        self.right_button.clicked.connect(self.run_script2)
        
        self.warning_text = QLabel("Please read the documentation before using\nthis program!", self)
        self.warning_text.setGeometry(10, 130, 280, 40)
        self.warning_text.setStyleSheet("font: 8pt; font-weight:bold;")
        self.warning_text.setAlignment(Qt.AlignCenter)
        
        self.under_header_text = QLabel(self)
        self.under_header_text.setOpenExternalLinks(True)
        self.under_header_text.setText("<a href='https://github.com/Vir0z4/svrp/wiki'>documentation</a>")
        self.under_header_text.setGeometry(10, 124, 298, 40)
        self.under_header_text.setStyleSheet("font: 8pt; font-weight:bold;")
        self.under_header_text.setAlignment(Qt.AlignCenter)
        
        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(245, 155, 50, 20)
        self.about_button.clicked.connect(self.about)
        self.about_button.raise_()
        
        self.bottom_text = QLabel("GUI v2.0", self)
        self.bottom_text.setGeometry(5, 145, 100, 30)
        self.bottom_text.setStyleSheet("font: 7pt")
        self.bottom_text.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

    def run_script1(self):
        import sny
        sny_dialog = sny.SnyPatcher(self)
        self.close()
        sny_dialog.exec_()

    def run_script2(self):
        import modmenu
        modmenu_dialog = modmenu.ModMenu(self)
        self.close()
        modmenu_dialog.exec_()
        
    def about(self):
        import about
        about_dialog = about.AboutDialog(self)
        about_dialog.exec_()

app = QApplication(sys.argv)
window = SVRP()
window.show()
sys.exit(app.exec_())