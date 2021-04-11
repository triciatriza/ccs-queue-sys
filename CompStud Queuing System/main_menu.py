import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from CSQueuingSystem import Ui_ComputerStudiesQueuingSystem
from ui_animation import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ComputerStudiesQueuingSystem()
        self.ui.setupUi(self)
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 225, True))
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())