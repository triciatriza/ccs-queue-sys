import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QFrame, QMessageBox
from PyQt5.uic import loadUi
from CSQueuingSystem import *

# GLOBAL VARIABLES FOR FRAMELESS WINDOW
window_size = 0
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

# GLOBAL VARIABLES FOR LOGIN_PAGE AND REGISTER_PAGE
access = False
user = ""
userType = ""

# GLOBAL VARIABLES FOR QUEUE_PAGE
queue = []
number = 0

# GLOBAL VARIABLES FOR ROOMRESERVATION_PAGE
reservations = [{"Date and Time": "01/10/1222 ", "Room": "FH 101", "State": "PENDING", "Reason": "date date"}]

# GLOBAL VARIABLES FOR APPOINTMENT_PAGE
appointments = [{}]

# GLOBAL VARIABLES FOR SCHOLARQUESTS_PAGE
quests = [{"Title": "", "Date and Time": "", "Duration": "", "Points": "", "Description": ""}]


# MESSAGEBOX FUNCTION FOR SHOWING ERROR
def showError(title, text):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(QMessageBox.Critical)
    msg.exec_()

# LOGIN_PAGE CLASS
class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        loadUi("login_page.ui", self)
        self.login_btn.clicked.connect(lambda: self.checkLogin())
        self.gotoregister_btn.clicked.connect(lambda: self.gotoRegister())

    # FUNCTION FOR USER VERIFICATION
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

    # SHOW REGISTER_PAGE
    def gotoRegister(self):
        login = Login(self)
        regWindow = Register(self)
        login.close()
        regWindow.show()

# REGISTER_PAGE CLASS
class Register(QDialog):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        loadUi("register_page.ui", self)
        self.gotologin_btn.clicked.connect(lambda: self.gotoLogin())
        self.register_btn.clicked.connect(lambda: self.registerAcc())

    # FUNCTION TO DISPLAY LOGIN_PAGE
    def gotoLogin(self):
        self.close()

    # FUNCTION TO CHECK IF AN ACCOUNT EXISTS
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

    # FUNCTION TO REGISTER A NEW ACCOUNT
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


# CSQUEUEINGSYSTEM CLASS (MAIN WINDOW)
class CSQueue(QMainWindow):
    def __init__(self, parent=None):
        super(CSQueue, self).__init__(parent)
        self.ui = Ui_ComputerStudiesQueuingSystem()
        self.ui.setupUi(self)

        # FRAMELESS WINNDOW
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # FUNCTIONALITIES FOR WINDOW BUTTONS (MINIMIZE/MAZIMIZE, RESTORE, CLOSE)
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_btn.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.close_btn.clicked.connect(lambda: self.close())

        # fUNCTION FOR TOGGLE MENU BUTTONS
        self.ui.Btn_Toggle.clicked.connect(lambda: self.slide_leftmenu())
        self.ui.queue_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.queue_page))
        self.ui.roomreservation_button.clicked.connect(lambda: self.loadReservations(self.ui.roomreservation_page, self.ui.rsv_table, reservations))
        self.ui.appointment_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.appointment_page))
        self.ui.scholarquests_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.scholarquests_page))
        self.ui.account_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.account_page))
        self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

########################################## CONTENT BUTTONS #########################################################

        # QUEUE_PAGE BUTTON FUNCTIONALITY
        self.ui.enrollmentqueue_btn.clicked.connect(lambda: self.displayNum())

        # Accept Queue Button
        self.ui.acceptQueue_btn.clicked.connect(lambda: print("Accepted queue!"))

        # Room Reservation Page Buttons
        self.ui.tp_setRsv_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setreservation_page))

        # Check Reservation Page Buttons
        self.ui.backRsv_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.roomreservation_page))
        self.ui.acceptRsv_btn.clicked.connect(lambda: print("Accepted reservation!"))
        self.ui.declineRsv_btn.clicked.connect(lambda: print("Declined reservation!"))

        # Set Reservation Page Buttons
        self.ui.setRsv_btn.clicked.connect(lambda: self.setReservations(self.ui.rsv_table, reservations))
        self.ui.cancelRsv_btn.clicked.connect(lambda: self.loadReservations(self.ui.roomreservation_page, self.ui.rsv_table, reservations))

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

        # FUNCTION FOR MOVABLE WINDOW
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        # CALL moveWindow FUNCTION
        self.ui.top_bar.mouseMoveEvent = moveWindow

        self.show()

    def loadReservations(self, page, table, data):
        self.ui.stackedWidget.setCurrentWidget(page)
        row = 0
        keys = len(data[0].keys())
        table.setRowCount(len(data))
        for x in reservations:
            table.setItem(row, 0, QtWidgets.QTableWidgetItem(x["Date and Time"]))
            table.setItem(row, 1, QtWidgets.QTableWidgetItem(x["Room"]))
            table.setItem(row, 2, QtWidgets.QTableWidgetItem(x["State"]))
            table.setItem(row, 3, QtWidgets.QTableWidgetItem(x["Reason"]))
            row = row + 1
    
    def setReservations(self, table, data):
        dateTime = self.ui.dtRsv.text()
        index = self.ui.roomRsv.currentIndex()
        room = self.ui.roomRsv.itemText(index)
        reason = self.ui.reasonRsv.text()

        if self.ui.confirmRsv.isChecked():
            data.append({"Date and Time": dateTime, "Room": room, "State": "PENDING", "Reason": reason})
            self.loadReservations(self.ui.roomreservation_page, self.ui.rsv_table, reservations)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Confirm appointment!')

    # FUNCTION FOR QUEUE_PAGE
    def displayNum(self):
        global number
        number = number + 1
        queue.append(number)
        QtWidgets.QMessageBox.information(self, 'Success', 'Your priority number is 1')
        self.ui.currentnum_display.setText(str(queue[0]))
        queue.pop()

######################################## MAIN MENU UI FUNCTIONALITIES ##################################################

    # ANIMATION FOR TOGGLE MENU
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

    # FUNCTION FOR RESTORING/MAXIMIZING WINDOW
    def restore_or_maximize_window(self):
        global window_size
        window_status = window_size

        if window_status == 0: # IF WINDOW IS MAXIMIZED
            window_size = 1
            self.showMaximized()
            self.ui.maximize_btn.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))
            self.ui.maximize_btn.setToolTip("Restore")
        else: # IF WINDOW IS RESTORED
            window_size = 0
            self.showNormal()
            self.ui.maximize_btn.setIcon(QtGui.QIcon(u":icons/icons/cil-window-maximize.png"))

    # FUNCTION CONNECTED TO moveWindow
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


# APPLICATION EXECUTION
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = CSQueue()
        window.show()
        sys.exit(app.exec_())