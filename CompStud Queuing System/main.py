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
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        loadUi("login_page.ui", self)
        self.login_btn.clicked.connect(lambda: self.checkLogin())
        self.gotoregister_btn.clicked.connect(lambda: self.gotoRegister())

    def checkLogin(self):
        if (self.username_field.text() == 'student' and self.password_field.text() == '1234'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect username or password')

    def gotoRegister(self):
        login = Login(self)
        regWindow = Register(self)
        login.close()
        regWindow.show()



class Register(QDialog):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        loadUi("register_page.ui", self)
        self.gotologin_btn.clicked.connect(lambda: self.gotoLogin())

    def gotoLogin(self):
        self.close()


#Main Menu
class CSQueue(QMainWindow):
    def __init__(self, parent=None):
        super(CSQueue, self).__init__(parent)
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

        # Content Buttons

        # Appointment Page Buttons
        

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = CSQueue()
        window.show()
        sys.exit(app.exec_())





