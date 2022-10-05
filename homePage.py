from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
class HomePage(QWidget):
    def __init__(self, mainWindow):
        QWidget.__init__(self)
        self.mainWindow = mainWindow
        mainLayout = QVBoxLayout()

        welcomeLabel = QLabel(self)
        welcomeLabel.setFont(QFont('Arial', 40))
        welcomeLabel.setText("WELCOME")  
        welcomeLabel.setTextFormat(Qt.TextFormat.PlainText)
        welcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(welcomeLabel)