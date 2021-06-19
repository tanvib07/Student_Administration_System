# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(800, 600)
        LoginPage.setStyleSheet("background-color: qconicalgradient(cx:0.818, cy:0, angle:0, stop:0.568182 rgba(0, 160, 187, 255), stop:0.954545 rgba(255, 0, 75, 255));")
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(431, 401))
        self.frame.setMaximumSize(QtCore.QSize(431, 401))
        self.frame.setStyleSheet("QToolButton{\n"
"background:#11f0f0;\n"
"border-radius:40px\n"
" }\n"
"\n"
"QFrame{\n"
"background:#2a2a2a;\n"
" }\n"
"\n"
"QLineEdit{\n"
"background:#2a2a2a;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"\n"
"QPushButton{\n"
"background:#B4C6C5;\n"
"border-radius:16px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 120, 101, 41))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(170, 10, 91, 91))
        self.toolButton.setStyleSheet("image: url(:/img/profileimg.png);")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/profileimg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(120, 126))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.username_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.username_lineEdit.setGeometry(QtCore.QRect(60, 210, 311, 41))
        self.username_lineEdit.setStyleSheet("")
        self.username_lineEdit.setText("")
        self.username_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.password_lineEdit.setGeometry(QtCore.QRect(60, 280, 311, 31))
        self.password_lineEdit.setInputMask("")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_Button = QtWidgets.QPushButton(self.frame)
        self.login_Button.setGeometry(QtCore.QRect(160, 350, 111, 41))
        self.login_Button.setObjectName("login_Button")
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "MainWindow"))
        self.label.setText(_translate("LoginPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">LOGIN HERE</span></p></body></html>"))
        self.username_lineEdit.setPlaceholderText(_translate("LoginPage", "Username"))
        self.password_lineEdit.setPlaceholderText(_translate("LoginPage", "Password"))
        self.login_Button.setText(_translate("LoginPage", "ENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
