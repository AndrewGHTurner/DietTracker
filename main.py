import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sqlite3

from homePage import HomePage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 40, 1000, 1000)
        self.stack = QStackedWidget(self)

        self.homePage = HomePage(self)

        self.stack.addWidget(self.homePage)

        self.setCentralWidget(self.stack)
        self.stack.setCurrentWidget(self.homePage)

        #these will be a connection and cursor that are common to all of the pages of this application
        self.connection = sqlite3.connect("Diet.db")
        self.cursor = self.connection.cursor()
        self.setUpDatabase()

    def setUpDatabase(self):#this will create the database and it's tables if they are not already available
        pass

def main():

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
    
	
if __name__ == '__main__':
   main()