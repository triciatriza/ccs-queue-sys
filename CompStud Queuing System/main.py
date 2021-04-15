import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import resource_rc

def loadMenu(menu):
    widget.addWidget(menu)
    widget.setCurrentIndex(widget.currentIndex()+1)

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi(r"ui\login_page.ui", self)
        self.gotoregister_btn.clicked.connect(lambda:loadMenu(Register()))

class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        loadUi(r"ui\register_page.ui", self)
        self.gotologin_btn.clicked.connect(lambda:loadMenu(Login()))

class CSQueue(QMainWindow):
    def __init__(self):
        super(CSQueue, self).__init__()
        loadUi(r"ui\CSQueuingSystem.ui", self)

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
app.exec_()



