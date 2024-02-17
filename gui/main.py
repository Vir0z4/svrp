import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6 import QtWidgets

from about import AboutDialog
from sny import SnyPatcher
from modmenu import ModMenu

class SVRP(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 180)

        self.setWindowTitle("Sony VAIO Recovery Patcher")
        self.setGeometry(100, 100, 300, 150)

        self.header_text = QLabel("Sony VAIO Recovery Patcher (SVRP)", self)
        self.header_text.setGeometry(10, 10, 280, 30)
        self.header_text.setStyleSheet("font: 12pt")
        self.header_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.under_header_text = QLabel("Select type of file you wish to patch:", self)
        self.under_header_text.setGeometry(10, 40, 280, 30)
        self.under_header_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.left_button = QPushButton(".sny\n(Windows installation)", self)
        self.left_button.setFixedSize(140, 50)
        self.left_button.move(10, 75)
        self.left_button.clicked.connect(self.run_script1)
        self.right_button = QPushButton(".mod\n(Apps and Drivers)", self)
        self.right_button.setFixedSize(140, 50)
        self.right_button.move(150, 75)
        self.right_button.clicked.connect(self.run_script2)
        
        self.warning_text = QLabel("Please read the documentation before using\nthis program!", self)
        self.warning_text.setGeometry(10, 130, 280, 40)
        self.warning_text.setStyleSheet("font: 8pt; font-weight:bold;")
        self.warning_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.under_header_text = QLabel(self)
        self.under_header_text.setOpenExternalLinks(True)
        self.under_header_text.setText("<a href='https://svrp.vaiolibrary.com'>documentation</a>")
        self.under_header_text.setGeometry(10, 123, 294, 40)
        self.under_header_text.setStyleSheet("font: 8pt; font-weight:bold;")
        self.under_header_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(245, 155, 50, 20)
        self.about_button.clicked.connect(self.about)
        self.about_button.raise_()
        
        self.bottom_text = QLabel("GUI v2.0.2", self)
        self.bottom_text.setGeometry(5, 145, 100, 30)
        self.bottom_text.setStyleSheet("font: 7pt")
        self.bottom_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)

        self.centerWindow()

    def run_script1(self):
        sny_dialog = SnyPatcher(self)
        self.close()
        sny_dialog.exec()

    def run_script2(self):
        modmenu_dialog = ModMenu(self)
        self.close()
        modmenu_dialog.exec()
        
    def about(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec()

    def centerWindow(self):
        window_geometry = self.frameGeometry()
        center_point = QtWidgets.QApplication.primaryScreen().availableGeometry().center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('VAIO.ico'))
    window = SVRP()
    window.show()
    sys.exit(app.exec())