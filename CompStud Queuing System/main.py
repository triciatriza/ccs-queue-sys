import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QFrame
from PyQt5.uic import loadUi
from CSQueuingSystem import *

window_size = 0
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login_page.ui", self)
        self.gotoregister_btn.clicked.connect(self.gotoRegister)

    def gotoRegister(self):
        widget.addWidget(Register())
        widget.setCurrentIndex(widget.currentIndex()+1)

class Register(QDialog):
    def __init__(self):
        super(Register, self).__init__()
        loadUi("register_page.ui", self)
        self.gotologin_btn.clicked.connect(self.gotoLogin)

    def gotoLogin(self):
        widget.addWidget(Login())
        widget.setCurrentIndex(widget.currentIndex() + 1)


#Main Menu
class CSQueue(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ComputerStudiesQueuingSystem()
        self.ui.setupUi(self)

        #FramelessWindow
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Window buttons functionalities
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_btn.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.close_btn.clicked.connect(lambda: self.close())

        #Toggle Button and Navigation Bar Buttons
        self.ui.Btn_Toggle.clicked.connect(lambda: self.slide_leftmenu())
        self.ui.queue_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.queue_page))
        self.ui.roomreservation_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.roomreservation_page))
        self.ui.appointment_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.appointment_page))
        self.ui.scholarquests_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.scholarquests_page))
        self.ui.account_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.account_page))
        self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

        # for moving/dragging window
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.top_bar.mouseMoveEvent = moveWindow

        self.show()

    #animation for toggle menu
    def slide_leftmenu(self):
        width = self.ui.frame_left_menu.width()

        if width == 70:
            newwidth = 225
        else:
            newwidth = 70

        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newwidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    #Restore or maximize main menu function
    def restore_or_maximize_window(self):
        global window_size
        window_status = window_size

        if window_status == 0: #if window is in maximized mode
            window_size = 1
            self.showMaximized()
            self.ui.maximize_btn.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))
            self.ui.maximize_btn.setToolTip("Restore")
        else: #if window is in restored mode
            window_size = 0
            self.showNormal()
            self.ui.maximize_btn.setIcon(QtGui.QIcon(u":icons/icons/cil-window-maximize.png"))

    # function connected to moveWindow() for moving/dragging window
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = Login()
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())




