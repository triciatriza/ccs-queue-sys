# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSQueuingSystem.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ComputerStudiesQueuingSystem(object):
    def setupUi(self, ComputerStudiesQueuingSystem):
        ComputerStudiesQueuingSystem.setObjectName("ComputerStudiesQueuingSystem")
        ComputerStudiesQueuingSystem.resize(1000, 610)
        ComputerStudiesQueuingSystem.setMinimumSize(QtCore.QSize(1000, 610))
        ComputerStudiesQueuingSystem.setStyleSheet("background-color: rgb(0, 58, 108);")
        self.centralwidget = QtWidgets.QWidget(ComputerStudiesQueuingSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMinimumSize(QtCore.QSize(0, 50))
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar.setStyleSheet("background-color: rgb(0, 58, 108);\n"
"")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_button = QtWidgets.QFrame(self.top_bar)
        self.toggle_button.setMaximumSize(QtCore.QSize(70, 60))
        self.toggle_button.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-radius: 15px\n"
"}")
        self.toggle_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toggle_button.setFrameShadow(QtWidgets.QFrame.Plain)
        self.toggle_button.setObjectName("toggle_button")
        self.Btn_Toggle = QtWidgets.QPushButton(self.toggle_button)
        self.Btn_Toggle.setGeometry(QtCore.QRect(0, -20, 70, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QtCore.QSize(70, 60))
        self.Btn_Toggle.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Btn_Toggle.setStyleSheet("QPushButton{\n"
"    \n"
"    background-image: url(:/icons/icons/cil-menu.png);\n"
"    background-repeat:none;\n"
"    padding: 5px 30px;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(70, 141, 211);\n"
"}\n"
"\n"
"")
        self.Btn_Toggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QtCore.QSize(24, 24))
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.horizontalLayout.addWidget(self.toggle_button)
        self.frame_top = QtWidgets.QFrame(self.top_bar)
        self.frame_top.setStyleSheet("")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_15 = QtWidgets.QFrame(self.frame_top)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setContentsMargins(0, 0, 9, 9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_10.addWidget(self.frame_16)
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        self.label_9.setMaximumSize(QtCore.QSize(50, 40))
        self.label_9.setStyleSheet("image: url(:/icons/icons/CS.png);")
        self.label_9.setText("")
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setPixmap(QtGui.QPixmap("icons/CS.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.label_5 = QtWidgets.QLabel(self.frame_15)
        self.label_5.setMinimumSize(QtCore.QSize(200, 0))
        self.label_5.setMaximumSize(QtCore.QSize(900, 16777215))
        self.label_5.setStyleSheet("font: 75 14pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_10.addWidget(self.frame_17)
        self.horizontalLayout_4.addWidget(self.frame_15)
        self.frame_14 = QtWidgets.QFrame(self.frame_top)
        self.frame_14.setMinimumSize(QtCore.QSize(125, 0))
        self.frame_14.setMaximumSize(QtCore.QSize(125, 16777215))
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.minimize_btn = QtWidgets.QPushButton(self.frame_14)
        self.minimize_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.minimize_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.minimize_btn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    \n"
"    image: url(:/icons/icons/cil-window-minimize.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.minimize_btn.setText("")
        self.minimize_btn.setIconSize(QtCore.QSize(30, 30))
        self.minimize_btn.setObjectName("minimize_btn")
        self.horizontalLayout_9.addWidget(self.minimize_btn)
        self.maximize_btn = QtWidgets.QPushButton(self.frame_14)
        self.maximize_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.maximize_btn.setSizeIncrement(QtCore.QSize(30, 30))
        self.maximize_btn.setToolTipDuration(0)
        self.maximize_btn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    \n"
"    image: url(:/icons/icons/cil-window-maximize.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.maximize_btn.setText("")
        self.maximize_btn.setIconSize(QtCore.QSize(30, 30))
        self.maximize_btn.setObjectName("maximize_btn")
        self.horizontalLayout_9.addWidget(self.maximize_btn)
        self.close_btn = QtWidgets.QPushButton(self.frame_14)
        self.close_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.close_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.close_btn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    \n"
"    image: url(:/icons/icons/cil-x.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.close_btn.setText("")
        self.close_btn.setIconSize(QtCore.QSize(30, 30))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_9.addWidget(self.close_btn)
        self.horizontalLayout_4.addWidget(self.frame_14)
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("background-color: rgb(226, 240, 255);")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Plain)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("QFrame{\n"
"    background-color: rgb(0, 58, 108);\n"
"}\n"
"QPushButton{\n"
"    padding: 20px 30px;\n"
"    border: none;\n"
"    background-color: rgb(0, 58, 108);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_for_buttons = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_for_buttons.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_for_buttons.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_for_buttons.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.frame_for_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_for_buttons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_for_buttons.setObjectName("frame_for_buttons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_for_buttons)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.queue_button = QtWidgets.QPushButton(self.frame_for_buttons)
        self.queue_button.setMinimumSize(QtCore.QSize(200, 0))
        self.queue_button.setMaximumSize(QtCore.QSize(250, 16777215))
        self.queue_button.setStyleSheet("QPushButton{\n"
"    background-image: url(:/icons/icons/cil-browser.png);\n"
"    background-repeat:none;\n"
"    padding-left:45px;\n"
"    background-position: center left;\n"
"    font: 75 9pt \"Century Gothic\";\n"
"    background-color: rgb(0, 58, 108);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(70, 141, 211);\n"
"}\n"
"")
        self.queue_button.setObjectName("queue_button")
        self.verticalLayout_2.addWidget(self.queue_button)
        self.roomreservation_button = QtWidgets.QPushButton(self.frame_for_buttons)
        self.roomreservation_button.setMinimumSize(QtCore.QSize(200, 0))
        self.roomreservation_button.setMaximumSize(QtCore.QSize(250, 16777215))
        self.roomreservation_button.setStyleSheet("QPushButton{\n"
"    background-image: url(:/icons/icons/cil-3d.png);\n"
"    background-repeat:none;\n"
"    padding-left:51px;    \n"
"    background-position: center left;\n"
"    font: 75 9pt \"Century Gothic\";\n"
"    background-color: rgb(0, 58, 108);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(70, 141, 211);\n"
"}\n"
"")
        self.roomreservation_button.setObjectName("roomreservation_button")
        self.verticalLayout_2.addWidget(self.roomreservation_button)
        self.appointment_button = QtWidgets.QPushButton(self.frame_for_buttons)
        self.appointment_button.setMinimumSize(QtCore.QSize(200, 0))
        self.appointment_button.setMaximumSize(QtCore.QSize(250, 16777215))
        self.appointment_button.setStyleSheet("QPushButton{    \n"
"    background-image: url(:/icons/icons/cil-pencil.png);\n"
"    background-repeat:none;\n"
"    padding-left:52px;\n"
"    background-position: center left;\n"
"    font: 75 9pt \"Century Gothic\";\n"
"    background-color: rgb(0, 58, 108);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(70, 141, 211);\n"
"}\n"
"")
        self.appointment_button.setObjectName("appointment_button")
        self.verticalLayout_2.addWidget(self.appointment_button)
        self.scholarquests_button = QtWidgets.QPushButton(self.frame_for_buttons)
        self.scholarquests_button.setMinimumSize(QtCore.QSize(200, 0))
        self.scholarquests_button.setMaximumSize(QtCore.QSize(250, 16777215))
        self.scholarquests_button.setStyleSheet("QPushButton{\n"
"    background-image: url(:/icons/icons/cil-pin.png);\n"
"    background-repeat:none;\n"
"    padding-left:36px;\n"
"    background-position: center left;\n"
"    font: 75 9pt \"Century Gothic\";\n"
"    background-color: rgb(0, 58, 108);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(70, 141, 211);\n"
"}\n"
"")
        self.scholarquests_button.setObjectName("scholarquests_button")
        self.verticalLayout_2.addWidget(self.scholarquests_button)
        self.frame_10 = QtWidgets.QFrame(self.frame_for_buttons)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_2.addWidget(self.frame_10)
        self.account_button = QtWidgets.QPushButton(self.frame_for_buttons)
        self.account_button.setMinimumSize(QtCore.QSize(200, 0))
        self.account_button.setMaximumSize(QtCore.QSize(250, 16777215))
        self.account_button.setStyleSheet("QPushButton{\n"
"    background-image: url(:/icons/icons/cil-user.png);\n"
"    background-repeat:none;\n"
"    padding-left:35px;\n"
"    background-position: center left;\n"
"    font: 75 9pt \"Century Gothic\";\n"
"    background-color: rgb(0, 58, 108);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(70, 141, 211);\n"
"}\n"
"\n"
"")
        self.account_button.setObjectName("account_button")
        self.verticalLayout_2.addWidget(self.account_button)
        self.settings_button = QtWidgets.QPushButton(self.frame_for_buttons)
        self.settings_button.setMinimumSize(QtCore.QSize(200, 0))
        self.settings_button.setMaximumSize(QtCore.QSize(250, 16777215))
        self.settings_button.setStyleSheet("QPushButton{\n"
"    background-image: url(:/icons/icons/cil-settings.png);\n"
"    background-repeat: none;\n"
"    padding-left:35px;\n"
"    background-position: center left;\n"
"    font: 75 9pt \"Century Gothic\";\n"
"    background-color: rgb(0, 58, 108);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(70, 141, 211);\n"
"}\n"
"\n"
"")
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_2.addWidget(self.settings_button)
        self.verticalLayout_3.addWidget(self.frame_for_buttons)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.stackedWidget = QtWidgets.QStackedWidget(self.content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.queue_page = QtWidgets.QWidget()
        self.queue_page.setObjectName("queue_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.queue_page)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.queue_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 125))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8.addWidget(self.frame_11)
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setStyleSheet("color: rgb(0, 58, 108);\n"
"font: 48pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8.addWidget(self.frame_12)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.line = QtWidgets.QFrame(self.frame_8)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.frame_13 = QtWidgets.QFrame(self.frame_2)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_8.addWidget(self.frame_13)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.queue_page)
        self.frame.setMinimumSize(QtCore.QSize(375, 0))
        self.frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(300, 75))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 58, 108);")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 58, 108);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 475))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 700))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.enrollment_btn = QtWidgets.QPushButton(self.frame_3)
        self.enrollment_btn.setMinimumSize(QtCore.QSize(125, 125))
        self.enrollment_btn.setMaximumSize(QtCore.QSize(325, 325))
        self.enrollment_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 97, 176);\n"
"    border: none;\n"
"    padding-top: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    font: 12pt \"Segoe UI\";\n"
"} \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(70, 141, 211);\n"
"}")
        self.enrollment_btn.setObjectName("enrollment_btn")
        self.horizontalLayout_5.addWidget(self.enrollment_btn)
        self.clearance_btn = QtWidgets.QPushButton(self.frame_3)
        self.clearance_btn.setMinimumSize(QtCore.QSize(125, 125))
        self.clearance_btn.setMaximumSize(QtCore.QSize(325, 325))
        self.clearance_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 97, 176);\n"
"    border: none;\n"
"    padding-top: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    \n"
"    font: 12pt \"Segoe UI\";\n"
"} \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(70, 141, 211);\n"
"}")
        self.clearance_btn.setObjectName("clearance_btn")
        self.horizontalLayout_5.addWidget(self.clearance_btn)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.academics_btn = QtWidgets.QPushButton(self.frame_4)
        self.academics_btn.setMinimumSize(QtCore.QSize(125, 125))
        self.academics_btn.setMaximumSize(QtCore.QSize(225, 225))
        self.academics_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 97, 176);\n"
"    border: none;\n"
"    padding-top: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    \n"
"    font: 12pt \"Segoe UI\";\n"
"} \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(70, 141, 211);\n"
"}")
        self.academics_btn.setObjectName("academics_btn")
        self.horizontalLayout_6.addWidget(self.academics_btn)
        self.organization_btn = QtWidgets.QPushButton(self.frame_4)
        self.organization_btn.setMinimumSize(QtCore.QSize(125, 125))
        self.organization_btn.setMaximumSize(QtCore.QSize(225, 225))
        self.organization_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 97, 176);\n"
"    border: none;\n"
"    padding-top: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    \n"
"    font: 12pt \"Segoe UI\";\n"
"} \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(70, 141, 211);\n"
"}")
        self.organization_btn.setObjectName("organization_btn")
        self.horizontalLayout_6.addWidget(self.organization_btn)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.regular_btn = QtWidgets.QPushButton(self.frame_5)
        self.regular_btn.setMinimumSize(QtCore.QSize(125, 125))
        self.regular_btn.setMaximumSize(QtCore.QSize(225, 225))
        self.regular_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 97, 176);\n"
"    border: none;\n"
"    padding-top: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    \n"
"    font: 12pt \"Segoe UI\";\n"
"} \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(70, 141, 211);\n"
"}")
        self.regular_btn.setObjectName("regular_btn")
        self.horizontalLayout_7.addWidget(self.regular_btn)
        self.faculty_btn = QtWidgets.QPushButton(self.frame_5)
        self.faculty_btn.setMinimumSize(QtCore.QSize(125, 125))
        self.faculty_btn.setMaximumSize(QtCore.QSize(225, 225))
        self.faculty_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 97, 176);\n"
"    border: none;\n"
"    padding-top: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    \n"
"    font: 12pt \"Segoe UI\";\n"
"} \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(70, 141, 211);\n"
"}")
        self.faculty_btn.setObjectName("faculty_btn")
        self.horizontalLayout_7.addWidget(self.faculty_btn)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.horizontalLayout_3.addWidget(self.frame)
        self.stackedWidget.addWidget(self.queue_page)
        self.roomreservation_page = QtWidgets.QWidget()
        self.roomreservation_page.setObjectName("roomreservation_page")
        self.label_4 = QtWidgets.QLabel(self.roomreservation_page)
        self.label_4.setGeometry(QtCore.QRect(320, 220, 331, 91))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.roomreservation_page)
        self.appointment_page = QtWidgets.QWidget()
        self.appointment_page.setObjectName("appointment_page")
        self.label_6 = QtWidgets.QLabel(self.appointment_page)
        self.label_6.setGeometry(QtCore.QRect(390, 230, 151, 21))
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.appointment_page)
        self.scholarquests_page = QtWidgets.QWidget()
        self.scholarquests_page.setObjectName("scholarquests_page")
        self.label_10 = QtWidgets.QLabel(self.scholarquests_page)
        self.label_10.setGeometry(QtCore.QRect(400, 250, 121, 16))
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.scholarquests_page)
        self.account_page = QtWidgets.QWidget()
        self.account_page.setObjectName("account_page")
        self.label_11 = QtWidgets.QLabel(self.account_page)
        self.label_11.setGeometry(QtCore.QRect(410, 230, 81, 16))
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.account_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.label_12 = QtWidgets.QLabel(self.settings_page)
        self.label_12.setGeometry(QtCore.QRect(390, 253, 131, 20))
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.settings_page)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.content)
        ComputerStudiesQueuingSystem.setCentralWidget(self.centralwidget)

        self.retranslateUi(ComputerStudiesQueuingSystem)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ComputerStudiesQueuingSystem)

    def retranslateUi(self, ComputerStudiesQueuingSystem):
        _translate = QtCore.QCoreApplication.translate
        ComputerStudiesQueuingSystem.setWindowTitle(_translate("ComputerStudiesQueuingSystem", "MainWindow"))
        self.label_5.setText(_translate("ComputerStudiesQueuingSystem", "Computer Studies Queuing System"))
        self.minimize_btn.setToolTip(_translate("ComputerStudiesQueuingSystem", "Minimize"))
        self.maximize_btn.setToolTip(_translate("ComputerStudiesQueuingSystem", "Maximize"))
        self.close_btn.setToolTip(_translate("ComputerStudiesQueuingSystem", "Close"))
        self.queue_button.setText(_translate("ComputerStudiesQueuingSystem", "QUEUE"))
        self.roomreservation_button.setText(_translate("ComputerStudiesQueuingSystem", "ROOM RESERVATION"))
        self.appointment_button.setText(_translate("ComputerStudiesQueuingSystem", "APPOINTMENT SETTER"))
        self.scholarquests_button.setText(_translate("ComputerStudiesQueuingSystem", "SCHOLAR QUESTS"))
        self.account_button.setText(_translate("ComputerStudiesQueuingSystem", "ACCOUNT"))
        self.settings_button.setText(_translate("ComputerStudiesQueuingSystem", "SETTINGS"))
        self.label_3.setText(_translate("ComputerStudiesQueuingSystem", "Queue"))
        self.label.setText(_translate("ComputerStudiesQueuingSystem", "        GET QUEUE NUMBER"))
        self.label_2.setText(_translate("ComputerStudiesQueuingSystem", "           SELECT PURPOSE HERE:"))
        self.enrollment_btn.setText(_translate("ComputerStudiesQueuingSystem", "Enrollment"))
        self.clearance_btn.setText(_translate("ComputerStudiesQueuingSystem", "Clearance"))
        self.academics_btn.setText(_translate("ComputerStudiesQueuingSystem", "Academics"))
        self.organization_btn.setText(_translate("ComputerStudiesQueuingSystem", "Organization"))
        self.regular_btn.setText(_translate("ComputerStudiesQueuingSystem", "Regular Lane"))
        self.faculty_btn.setText(_translate("ComputerStudiesQueuingSystem", "Faculty"))
        self.label_4.setText(_translate("ComputerStudiesQueuingSystem", "Room reservation"))
        self.label_6.setText(_translate("ComputerStudiesQueuingSystem", "appointment page"))
        self.label_10.setText(_translate("ComputerStudiesQueuingSystem", "scholarship_quest_page"))
        self.label_11.setText(_translate("ComputerStudiesQueuingSystem", "accounts page"))
        self.label_12.setText(_translate("ComputerStudiesQueuingSystem", "Settings"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ComputerStudiesQueuingSystem = QtWidgets.QMainWindow()
    ui = Ui_ComputerStudiesQueuingSystem()
    ui.setupUi(ComputerStudiesQueuingSystem)
    ComputerStudiesQueuingSystem.show()
    sys.exit(app.exec_())
