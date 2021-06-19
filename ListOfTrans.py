# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListOfTrans.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="local",
    password="",
    database="mpdev"
)

class Ui_ListMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 841)
        MainWindow.setStyleSheet("\n"
"background-color: #212121;\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_title_label = QtWidgets.QLabel(self.centralwidget)
        self.list_title_label.setMinimumSize(QtCore.QSize(300, 50))
        self.list_title_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.list_title_label.setFont(font)
        self.list_title_label.setObjectName("list_title_label")
        self.verticalLayout.addWidget(self.list_title_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_recent = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_recent.setMinimumSize(QtCore.QSize(0, 50))
        self.radioButton_recent.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_recent.setFont(font)
        self.radioButton_recent.setStyleSheet("color: rgb(238, 238, 238);")
        self.radioButton_recent.setChecked(False)
        self.radioButton_recent.setObjectName("radioButton_recent")
        self.horizontalLayout.addWidget(self.radioButton_recent)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.radioButton_daily = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_daily.setMinimumSize(QtCore.QSize(0, 50))
        self.radioButton_daily.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_daily.setFont(font)
        self.radioButton_daily.setStyleSheet("color: rgb(238, 238, 238);")
        self.radioButton_daily.setObjectName("radioButton_daily")
        self.horizontalLayout.addWidget(self.radioButton_daily)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(1000, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("border: 3px solid #0d7377;\n"
"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(190)
        self.verticalLayout.addWidget(self.tableWidget)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(140, 50))
        self.backButton.setMaximumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton#backButton{\n"
"                                       color: #eeeeee;\n"
"                                        background-color: #212121;\n"
"                                        border: 2px solid #9a0002;\n"
"                                        border-radius: 25px;\n"
"                                        }\n"
"                                  \n"
"QPushButton#backButton:hover{\n"
"border: 3px solid rgb(255, 0, 0);\n"
" background-color: #9a0002;\n"
"                                        }")
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.radioButton_recent.clicked.connect(self.recentMonTrans)
        self.radioButton_daily.clicked.connect(self.dailyTrans)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.list_title_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#32e0c4;\">List Of Transactions</span></p></body></html>"))
        self.radioButton_recent.setText(_translate("MainWindow", "Recent Month Transactions"))
        self.radioButton_daily.setText(_translate("MainWindow", "Daily Transactions"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Installment Number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Transaction Amount"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mode Of Payment"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Transaction Date"))
        self.backButton.setText(_translate("MainWindow", "Back"))


    def recentMonTrans(self):
        print("r")
        cursor = mydb.cursor(buffered=True)
        #getting the current date to fetch the recent month
        sql1 = "SELECT transaction_date FROM transactions_table ORDER BY transaction_date DESC LIMIT 1"
        cursor.execute(sql1)
        day = cursor.fetchone()
        i = str(day)
        #extracting the month from the date
        month = i[21:23]
        #if there is no transaction done in the current month
        if not month:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("No Transactions done this month")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return
        sql = "SELECT DISTINCT s.first_name,s.middle_name,s.last_name,t.installment_no,t.transaction_amt,t.mode_of_payment,t.transaction_date " \
              "FROM student_info_table s,transactions_table t WHERE t.student_id = s.student_id AND MONTH(transaction_date)="+str(month)+" " \
              "ORDER BY t.transaction_date "
        cursor.execute(sql)
        recent_values = cursor.fetchall() #tuple list of all values to be displayed
        #adding name, installment_no, transaction_amt, modeOfPayment and transaction_date to the tree widget display
        row = 0
        self.tableWidget.setRowCount(cursor.rowcount)
        for x in recent_values:
            fname = x[0]
            mname = x[1]
            lname = x[2]
            name = fname+" "+mname+" "+lname
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[3])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[4])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(x[5]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[6])))
            row += 1




    def dailyTrans(self):
        print("d")
        #getting today's date
        tdate= date.today()
        print(date)
        cursor = mydb.cursor(buffered=True)
        #query to get today's transactions
        sql = "SELECT DISTINCT s.first_name,s.middle_name,s.last_name,t.installment_no,t.transaction_amt,t.mode_of_payment,t.transaction_date " \
              "FROM student_info_table s,transactions_table t WHERE t.student_id = s.student_id AND t.transaction_date=(%s) ORDER BY t.transaction_date"

        cursor.execute(sql,(tdate,))
        recent_values = cursor.fetchall()
        # adding name, installment_no, transaction_amt, modeOfPayment and transaction_date to the tree widget display
        row = 0
        self.tableWidget.setRowCount(cursor.rowcount)
        for x in recent_values:
            fname = x[0]
            mname = x[1]
            lname = x[2]
            name = fname + " " + mname + " " + lname
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[3])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[4])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(x[5]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[6])))
            row += 1



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
