# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchInStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="local",
    password="",
    database="mpdev"
)

# mydb = mysql.connector.connect(
#     host="bll36yqmvrqimmbruwt6-mysql.services.clever-cloud.com",
#     user="uzpjhgsb2loc6cgj",
#     password="ztsmG1uLx2oVEy0CLEFo",
#     database="bll36yqmvrqimmbruwt6"
# )


class Ui_StudentsSectionWindow(object):
    def setupUi(self, StudentsSectionWindow):
        StudentsSectionWindow.setObjectName("StudentsSectionWindow")
        StudentsSectionWindow.resize(1109, 828)
        StudentsSectionWindow.setStyleSheet("QMainWindow{\n"
                                            "background-color: #212121;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton{\n"
                                            "background-color: #212121;\n"
                                            "Color: #eeeeee;\n"
                                            "border-radius: 20px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#cancelButton{\n"
                                            "color: #eeeeee;\n"
                                            "background-color: #212121;\n"
                                            "border: 2px solid #9a0002;\n"
                                            "border-radius: 25px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#cancelButton:hover{\n"
                                            "border: 3px solid rgb(255, 0, 0);\n"
                                            "background-color: #9a0002;\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit{\n"
                                            "padding-left: 6px;\n"
                                            "padding-right: 6px;\n"
                                            "border: 2px solid #0d7377;\n"
                                            "border-radius: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit:hover{\n"
                                            "border: 3px solid #32e0c4;\n"
                                            "}\n"
                                            "\n"
                                            "QLabel{\n"
                                            "color: #eeeeee;\n"
                                            "}\n"
                                            "\n"
                                            "QLabel#studentsInfoLabel{\n"
                                            "color: #32e0c4;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox{\n"
                                            "border: 2px solid #0d7377;\n"
                                            "border-radius: 5px;\n"
                                            "padding-left: 4px;\n"
                                            "padding-right: 4px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox:hover{\n"
                                            "border: 3px solid #32e0c4;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox QAbstractItemView {\n"
                                            "border: 2px solid #32e0c4;\n"
                                            "selection-background-color: #0d7377;\n"
                                            "}\n"
                                            "")
        self.centralwidget = QtWidgets.QWidget(StudentsSectionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.studentsInfoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.studentsInfoLabel.setFont(font)
        self.studentsInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.studentsInfoLabel.setObjectName("studentsInfoLabel")
        self.verticalLayout_5.addWidget(self.studentsInfoLabel)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchByLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchByLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.searchByLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.searchByLabel.setFont(font)
        self.searchByLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchByLabel.setObjectName("searchByLabel")
        self.verticalLayout.addWidget(self.searchByLabel)
        self.searchByComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchByComboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.searchByComboBox.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchByComboBox.setFont(font)
        self.searchByComboBox.setObjectName("searchByComboBox")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.searchByComboBox.addItem("")
        self.verticalLayout.addWidget(self.searchByComboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.searchLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.searchLabel.setFont(font)
        self.searchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchLabel.setObjectName("searchLabel")
        self.verticalLayout_2.addWidget(self.searchLabel)
        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchInput.setMinimumSize(QtCore.QSize(300, 40))
        self.searchInput.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchInput.setFont(font)
        self.searchInput.setText("")
        self.searchInput.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setObjectName("searchInput")
        self.verticalLayout_2.addWidget(self.searchInput)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.filterLabel = QtWidgets.QLabel(self.centralwidget)
        self.filterLabel.setMinimumSize(QtCore.QSize(300, 40))
        self.filterLabel.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.filterLabel.setFont(font)
        self.filterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filterLabel.setObjectName("filterLabel")
        self.verticalLayout_3.addWidget(self.filterLabel)
        self.filterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.filterComboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.filterComboBox.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filterComboBox.setFont(font)
        self.filterComboBox.setObjectName("filterComboBox")
        self.verticalLayout_3.addWidget(self.filterComboBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.totalStudentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalStudentsLabel.setMinimumSize(QtCore.QSize(320, 40))
        self.totalStudentsLabel.setMaximumSize(QtCore.QSize(320, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.totalStudentsLabel.setFont(font)
        self.totalStudentsLabel.setObjectName("totalStudentsLabel")
        self.horizontalLayout_3.addWidget(self.totalStudentsLabel)
        self.totalCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalCountLabel.setMinimumSize(QtCore.QSize(70, 40))
        self.totalCountLabel.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.totalCountLabel.setFont(font)
        self.totalCountLabel.setObjectName("totalCountLabel")
        self.horizontalLayout_3.addWidget(self.totalCountLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.searchDataTable = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchDataTable.setFont(font)
        self.searchDataTable.setObjectName("searchDataTable")
        self.searchDataTable.setColumnCount(12)
        self.searchDataTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDataTable.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchDataTable.setItem(0, 11, item)
        self.horizontalLayout_5.addWidget(self.searchDataTable)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(180, 50))
        self.cancelButton.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 0, 0, 1, 1)
        StudentsSectionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StudentsSectionWindow)
        self.statusbar.setObjectName("statusbar")
        StudentsSectionWindow.setStatusBar(self.statusbar)
        self.filterComboBox.hide()
        self.filterLabel.hide()
        self.searchDataTable.verticalHeader().setVisible(False)

        self.retranslateUi(StudentsSectionWindow)
        self.loadAll()

        # ALL CONNECTS

        self.searchInput.textChanged.connect(self.searchOnName)
        self.filterComboBox.currentIndexChanged.connect(self.searchCourseOrBatch)
        self.searchByComboBox.currentIndexChanged.connect(self.comboBoxItemChanged)

        # REGEX

        self.myregex3 = QtCore.QRegExp("[A-Za-z ]+")
        self.myregexph = QtCore.QRegExp("[0-9]+")
        self.validate_inputf()

        QtCore.QMetaObject.connectSlotsByName(StudentsSectionWindow)

    # INPUT VALIDATORS

    def validate_inputf(self):
        my_validator = QtGui.QRegExpValidator(self.myregex3, self.searchInput)
        self.searchInput.setValidator(my_validator)

    def validate_inputph(self):
        my_validator = QtGui.QRegExpValidator(self.myregexph, self.searchInput)
        self.searchInput.setValidator(my_validator)

    def searchOnName(self):
        mycursor = mydb.cursor()
        if self.searchByComboBox.currentIndex() == 0:
            searchCharacter = self.searchInput.text()
            sql = "SELECT * FROM student_info_table WHERE first_name LIKE '%" + searchCharacter + "%' or middle_name LIKE '%" + searchCharacter + "%' or last_name LIKE '%" + searchCharacter + "%'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            row = 0
            self.searchDataTable.setRowCount(mycursor.rowcount)
            for x in result:
                fname = x[1]
                mname = x[2]
                lname = x[3]
                sql = "SELECT count(*) FROM student_course_batch WHERE student_id = " + str(x[0])
                mycursor.execute(sql)
                courseCount = mycursor.fetchone()
                fullname = fname + " " + mname + " " + lname
                sql = "SELECT count(referrals) FROM student_info_table WHERE referrals = '" + fullname + "'"
                mycursor.execute(sql)
                referralCount = mycursor.fetchone()
                self.searchDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                self.searchDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(fullname))
                self.searchDataTable.setItem(row, 2, QtWidgets.QTableWidgetItem(x[4]))
                self.searchDataTable.setItem(row, 3, QtWidgets.QTableWidgetItem(x[5]))
                self.searchDataTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[8])))
                self.searchDataTable.setItem(row, 5, QtWidgets.QTableWidgetItem(x[6]))
                self.searchDataTable.setItem(row, 6, QtWidgets.QTableWidgetItem(str(x[7])))
                self.searchDataTable.setItem(row, 7, QtWidgets.QTableWidgetItem(x[9]))
                self.searchDataTable.setItem(row, 8, QtWidgets.QTableWidgetItem(x[10]))
                self.searchDataTable.setItem(row, 9, QtWidgets.QTableWidgetItem(str(courseCount[0])))
                self.searchDataTable.setItem(row, 10, QtWidgets.QTableWidgetItem(str(referralCount[0])))
                if x[11] is None:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem("None"))
                else:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem(x[11]))
                row += 1
            self.totalCountLabel.setText(str(len(result)))
            mycursor.close()
        elif self.searchByComboBox.currentIndex() == 1:
            searchCharacter = self.searchInput.text()
            sql = "SELECT * FROM student_info_table WHERE phone LIKE '%" + searchCharacter + "%'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            row = 0
            self.searchDataTable.setRowCount(mycursor.rowcount)
            for x in result:
                fname = x[1]
                mname = x[2]
                lname = x[3]
                sql = "SELECT count(*) FROM student_course_batch WHERE student_id = " + str(x[0])
                mycursor.execute(sql)
                courseCount = mycursor.fetchone()
                fullname = fname + " " + mname + " " + lname
                sql = "SELECT count(referrals) FROM student_info_table WHERE referrals = '" + fullname + "'"
                mycursor.execute(sql)
                referralCount = mycursor.fetchone()
                self.searchDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                self.searchDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(fullname))
                self.searchDataTable.setItem(row, 2, QtWidgets.QTableWidgetItem(x[4]))
                self.searchDataTable.setItem(row, 3, QtWidgets.QTableWidgetItem(x[5]))
                self.searchDataTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[8])))
                self.searchDataTable.setItem(row, 5, QtWidgets.QTableWidgetItem(x[6]))
                self.searchDataTable.setItem(row, 6, QtWidgets.QTableWidgetItem(str(x[7])))
                self.searchDataTable.setItem(row, 7, QtWidgets.QTableWidgetItem(x[9]))
                self.searchDataTable.setItem(row, 8, QtWidgets.QTableWidgetItem(x[10]))
                self.searchDataTable.setItem(row, 9, QtWidgets.QTableWidgetItem(str(courseCount[0])))
                self.searchDataTable.setItem(row, 10, QtWidgets.QTableWidgetItem(str(referralCount[0])))
                if x[11] is None:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem("None"))
                else:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem(x[11]))
                row += 1
            self.totalCountLabel.setText(str(len(result)))
            mycursor.close()

    def comboBoxItemChanged(self):
        curIndex = self.searchByComboBox.currentIndex()
        if curIndex == 0:
            self.loadAll()
            self.filterComboBox.hide()
            self.filterLabel.hide()
            self.searchLabel.show()
            self.searchInput.show()
            self.validate_inputf()
            self.searchLabel.setText("Enter Name to Search")
        elif curIndex == 1:
            self.loadAll()
            self.filterComboBox.hide()
            self.filterLabel.hide()
            self.searchLabel.show()
            self.searchInput.show()
            self.validate_inputph()
            self.searchLabel.setText("Enter Phone Number to Search")
        elif curIndex == 2 or curIndex == 3:
            if curIndex == 2:
                self.filterComboBox.show()
                self.filterLabel.show()
                self.filterLabel.setText("Select Course")
                self.searchLabel.hide()
                self.searchInput.hide()
                self.loadCourses()
                self.filterComboBox.setCurrentIndex(-1)
                self.totalCountLabel.setText("0")
            else:
                self.filterComboBox.show()
                self.filterLabel.show()
                self.filterLabel.setText("Select Batch")
                self.searchLabel.hide()
                self.searchInput.hide()
                self.loadBatches()
                self.filterComboBox.setCurrentIndex(-1)
                self.totalCountLabel.setText("0")

    def searchCourseOrBatch(self):
        mycursor = mydb.cursor(buffered=True)
        if self.searchByComboBox.currentIndex() == 2:
            course = self.filterComboBox.currentText()
            sql = "SELECT s.* FROM student_course_batch stb, courses_table c, student_info_table s WHERE c.course_id " \
                  "= stb.course_id and s.student_id = stb.student_id and c.course_name = '" + course + "' "
            mycursor.execute(sql)
            result = mycursor.fetchall()
            row = 0
            self.searchDataTable.setRowCount(mycursor.rowcount)
            for x in result:
                fname = x[1]
                mname = x[2]
                lname = x[3]
                sql = "SELECT count(*) FROM student_course_batch WHERE student_id = " + str(x[0])
                mycursor.execute(sql)
                courseCount = mycursor.fetchone()
                fullname = fname + " " + mname + " " + lname
                sql = "SELECT count(referrals) FROM student_info_table WHERE referrals = '" + fullname + "'"
                mycursor.execute(sql)
                referralCount = mycursor.fetchone()
                self.searchDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                self.searchDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(fullname))
                self.searchDataTable.setItem(row, 2, QtWidgets.QTableWidgetItem(x[4]))
                self.searchDataTable.setItem(row, 3, QtWidgets.QTableWidgetItem(x[5]))
                self.searchDataTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[8])))
                self.searchDataTable.setItem(row, 5, QtWidgets.QTableWidgetItem(x[6]))
                self.searchDataTable.setItem(row, 6, QtWidgets.QTableWidgetItem(str(x[7])))
                self.searchDataTable.setItem(row, 7, QtWidgets.QTableWidgetItem(x[9]))
                self.searchDataTable.setItem(row, 8, QtWidgets.QTableWidgetItem(x[10]))
                self.searchDataTable.setItem(row, 9, QtWidgets.QTableWidgetItem(str(courseCount[0])))
                self.searchDataTable.setItem(row, 10, QtWidgets.QTableWidgetItem(str(referralCount[0])))
                if x[11] is None:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem("None"))
                else:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem(x[11]))
                row += 1
            self.totalCountLabel.setText(str(len(result)))
            mycursor.close()
            self.setTableSize()
        elif self.searchByComboBox.currentIndex() == 3:
            mycursor = mydb.cursor()
            batch = self.filterComboBox.currentText()
            sql = "SELECT  s.* FROM student_course_batch stb, batches_table b, student_info_table s WHERE b.batch_id " \
                  "= stb.batch_id and s.student_id = stb.student_id and b.batch_name = '" + batch + "'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            row = 0
            self.searchDataTable.setRowCount(mycursor.rowcount)
            for x in result:
                fname = x[1]
                mname = x[2]
                lname = x[3]
                sql = "SELECT count(*) FROM student_course_batch WHERE student_id = " + str(x[0])
                mycursor.execute(sql)
                courseCount = mycursor.fetchone()
                fullname = fname + " " + mname + " " + lname
                sql = "SELECT count(referrals) FROM student_info_table WHERE referrals = '" + fullname + "'"
                mycursor.execute(sql)
                referralCount = mycursor.fetchone()
                self.searchDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                self.searchDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(fullname))
                self.searchDataTable.setItem(row, 2, QtWidgets.QTableWidgetItem(x[4]))
                self.searchDataTable.setItem(row, 3, QtWidgets.QTableWidgetItem(x[5]))
                self.searchDataTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[8])))
                self.searchDataTable.setItem(row, 5, QtWidgets.QTableWidgetItem(x[6]))
                self.searchDataTable.setItem(row, 6, QtWidgets.QTableWidgetItem(str(x[7])))
                self.searchDataTable.setItem(row, 7, QtWidgets.QTableWidgetItem(x[9]))
                self.searchDataTable.setItem(row, 8, QtWidgets.QTableWidgetItem(x[10]))
                self.searchDataTable.setItem(row, 9, QtWidgets.QTableWidgetItem(str(courseCount[0])))
                self.searchDataTable.setItem(row, 10, QtWidgets.QTableWidgetItem(str(referralCount[0])))
                if x[11] is None:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem("None"))
                else:
                    self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem(x[11]))
                row += 1
            self.totalCountLabel.setText(str(len(result)))
            mycursor.close()
            self.setTableSize()

    def loadCourses(self):
        mycursor = mydb.cursor(buffered=True)
        sql = "SELECT course_name FROM courses_table"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.filterComboBox.clear()
        for x in result:
            self.filterComboBox.addItem(x[0])
        mycursor.close()

    def loadBatches(self):
        mycursor = mydb.cursor(buffered=True)
        sql = "SELECT batch_name FROM batches_table"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        self.filterComboBox.clear()
        for x in result:
            self.filterComboBox.addItem(x[0])
        mycursor.close()

    def loadAll(self):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT * FROM student_info_table")
        lst = mycursor.fetchall()
        row = 0
        self.searchDataTable.setRowCount(mycursor.rowcount)
        for x in lst:
            fname = x[1]
            mname = x[2]
            lname = x[3]
            sql = "SELECT count(*) FROM student_course_batch WHERE student_id = " + str(x[0])
            mycursor.execute(sql)
            courseCount = mycursor.fetchone()
            fullname = fname + " " + mname + " " + lname
            sql = "SELECT count(referrals) FROM student_info_table WHERE referrals = '" + fullname + "'"
            mycursor.execute(sql)
            referralCount = mycursor.fetchone()
            self.searchDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.searchDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(fullname))
            self.searchDataTable.setItem(row, 2, QtWidgets.QTableWidgetItem(x[4]))
            self.searchDataTable.setItem(row, 3, QtWidgets.QTableWidgetItem(x[5]))
            self.searchDataTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[8])))
            self.searchDataTable.setItem(row, 5, QtWidgets.QTableWidgetItem(x[6]))
            self.searchDataTable.setItem(row, 6, QtWidgets.QTableWidgetItem(str(x[7])))
            self.searchDataTable.setItem(row, 7, QtWidgets.QTableWidgetItem(x[9]))
            self.searchDataTable.setItem(row, 8, QtWidgets.QTableWidgetItem(x[10]))
            self.searchDataTable.setItem(row, 9, QtWidgets.QTableWidgetItem(str(courseCount[0])))
            self.searchDataTable.setItem(row, 10, QtWidgets.QTableWidgetItem(str(referralCount[0])))
            if x[11] is None:
                self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem("None"))
            else:
                self.searchDataTable.setItem(row, 11, QtWidgets.QTableWidgetItem(x[11]))
            row += 1
        self.setTableSize()
        self.totalCountLabel.setText(str(len(lst)))


    def setTableSize(self):
        header = self.searchDataTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(11, QtWidgets.QHeaderView.ResizeToContents)


    def retranslateUi(self, StudentsSectionWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentsSectionWindow.setWindowTitle(_translate("StudentsSectionWindow", "MainWindow"))
        self.studentsInfoLabel.setText(_translate("StudentsSectionWindow", "STUDENTS SECTION"))
        self.searchByLabel.setText(_translate("StudentsSectionWindow", "Search By"))
        self.searchByComboBox.setItemText(0, _translate("StudentsSectionWindow", "Name"))
        self.searchByComboBox.setItemText(1, _translate("StudentsSectionWindow", "Phone Number"))
        self.searchByComboBox.setItemText(2, _translate("StudentsSectionWindow", "Course"))
        self.searchByComboBox.setItemText(3, _translate("StudentsSectionWindow", "Batch"))
        self.searchLabel.setText(_translate("StudentsSectionWindow", "Enter Name to Search"))
        self.filterLabel.setText(_translate("StudentsSectionWindow", "Select"))
        self.totalStudentsLabel.setText(_translate("StudentsSectionWindow", "Total Number of Students:  "))
        self.totalCountLabel.setText(_translate("StudentsSectionWindow", "0"))
        item = self.searchDataTable.verticalHeaderItem(0)
        item.setText(_translate("StudentsSectionWindow", "1"))
        item = self.searchDataTable.horizontalHeaderItem(0)
        item.setText(_translate("StudentsSectionWindow", "Id"))
        item = self.searchDataTable.horizontalHeaderItem(1)
        item.setText(_translate("StudentsSectionWindow", "Full Name"))
        item = self.searchDataTable.horizontalHeaderItem(2)
        item.setText(_translate("StudentsSectionWindow", "Phone Number"))
        item = self.searchDataTable.horizontalHeaderItem(3)
        item.setText(_translate("StudentsSectionWindow", "Whatsapp No"))
        item = self.searchDataTable.horizontalHeaderItem(4)
        item.setText(_translate("StudentsSectionWindow", "Address"))
        item = self.searchDataTable.horizontalHeaderItem(5)
        item.setText(_translate("StudentsSectionWindow", "Email"))
        item = self.searchDataTable.horizontalHeaderItem(6)
        item.setText(_translate("StudentsSectionWindow", "Admission Date"))
        item = self.searchDataTable.horizontalHeaderItem(7)
        item.setText(_translate("StudentsSectionWindow", "Education"))
        item = self.searchDataTable.horizontalHeaderItem(8)
        item.setText(_translate("StudentsSectionWindow", "Experience"))
        item = self.searchDataTable.horizontalHeaderItem(9)
        item.setText(_translate("StudentsSectionWindow", "Courses Opted"))
        item = self.searchDataTable.horizontalHeaderItem(10)
        item.setText(_translate("StudentsSectionWindow", "Referrals Count"))
        item = self.searchDataTable.horizontalHeaderItem(11)
        item.setText(_translate("StudentsSectionWindow", "Referred By"))
        __sortingEnabled = self.searchDataTable.isSortingEnabled()
        self.searchDataTable.setSortingEnabled(True)
        self.searchDataTable.setSortingEnabled(__sortingEnabled)
        self.cancelButton.setText(_translate("StudentsSectionWindow", "Back"))
