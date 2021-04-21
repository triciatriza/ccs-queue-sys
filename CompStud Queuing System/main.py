import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QFrame, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from CSQueuingSystem import *

window_size = 0
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
access = False
user = ""
userType = ""

#Login Window
class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        loadUi("login_page.ui", self)
        self.login_btn.clicked.connect(lambda: self.checkLogin())
        self.gotoregister_btn.clicked.connect(lambda: self.gotoRegister())

    #User verification
    def checkLogin(self):
        global access
        global user
        global userType
        access = False
        idnum = self.IDnumber_field.text()
        password = self.password_field.text()
        file = open("accounts.txt", "r")
        for i in file:
            a, b, c, d, e, f, g, h = i.split(",")
            h = h.strip()
            if(idnum == d and password == g):
                access = True
                userType = h
                QtWidgets.QMessageBox.information(self, 'Success', 'Logged in successfully.')
                self.accept()
                break
        file.close()
        if access is False:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect username or password')

    #Show Register Window
    def gotoRegister(self):
        login = Login(self)
        regWindow = Register(self)
        login.close()
        regWindow.show()

#Register Window
class Register(QDialog):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        loadUi("register_page.ui", self)
        self.gotologin_btn.clicked.connect(lambda: self.gotoLogin())
        self.register_btn.clicked.connect(lambda: self.registerAcc())

    #returns to Login Widow
    def gotoLogin(self):
        self.close()

    #Check if user exists
    def checkUser(self):
        userExists = False
        firstname = self.firstname_field.text()
        middlename = self.middlename_field.text()
        lastname = self.lastname_field.text()
        idnum = self.IDnumber_field.text()
        email = self.email_field.text()
        course_type = self.course_comboBox.currentText()
        password = self.password_field.text()
        confirmpass = self.confirmpass_field.text()

        file = open("accounts.txt", "r")

        for i in file:
            a, b, c, d, e, f, g, h= i.split(",")
            h = h.strip()
            if idnum == d:
                file.close
                QtWidgets.QMessageBox.warning(self, 'Error', 'Account already exists!')
                exists = True
                break

        return userExists

    #Register a new account
    def registerAcc(self):
        global access
        firstname = self.firstname_field.text()
        middlename = self.middlename_field.text()
        lastname = self.lastname_field.text()
        idnum = self.IDnumber_field.text()
        email = self.email_field.text()
        course_type = self.course_comboBox.currentText()
        password = self.password_field.text()
        confirmpass = self.confirmpass_field.text()

        if (self.checkUser() == False):
            if (password == confirmpass):
                file =open("accounts.txt", "a")
                file.write("\n"+ firstname + "," + middlename + "," + lastname + "," + idnum + "," + email + "," + course_type + "," + password + "," + "student")
                file.close
                access = True
                QtWidgets.QMessageBox.information(self, 'Success', 'Registered successfully.')
                self.close()
            else:
                QtWidgets.QMessageBox.warning(self, 'Error', "Password doesn't match")


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

        # Accept Queue Buttons
        self.ui.acceptQueue_btn.clicked.connect(lambda: print("Accepted queue!"))

        # Room Reservation Page Buttons
        self.ui.tp_setRsv_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setreservation_page))

        # Check Reservation Page Buttons
        self.ui.backRsv_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.roomreservation_page))
        self.ui.acceptRsv_btn.clicked.connect(lambda: print("Accepted reservation!"))
        self.ui.declineRsv_btn.clicked.connect(lambda: print("Declined reservation!"))

        # Set Reservation Page Buttons
        # self.ui.dialogRsv_btn.accepted.connect(lambda: print("Set reservation!"))

        # Appointment Page Buttons
        self.ui.tp_chkApt_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.checkappointment_page))
        self.ui.tp_setApt_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.appointment_page))

        # Check Appointment Page Buttons
        self.ui.backApt_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.appointment_page))
        self.ui.acceptApt_btn.clicked.connect(lambda: print("Accepted appointment!"))
        self.ui.declineApt_btn.clicked.connect(lambda: print("Declined appointment!"))

        # Quests Page Buttons
        self.ui.tp_acceptQuest_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.acceptquests_page))

        # Accept Quests Page Buttons
        self.ui.acceptQuest_btn.clicked.connect(lambda: print("Accepted quest!"))

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





