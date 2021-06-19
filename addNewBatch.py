# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNewBatch.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="local",
    password="",
    database="mpdev"
)

class Ui_AddBatchDialog(object):
    def setupUi(self, AddBatchDialog):
        AddBatchDialog.setObjectName("AddBatchDialog")
        AddBatchDialog.resize(800, 600)
        AddBatchDialog.setMinimumSize(QtCore.QSize(800, 600))
        AddBatchDialog.setMaximumSize(QtCore.QSize(800, 600))
        AddBatchDialog.setStyleSheet("QDialog{\n"
                                     "background-color: #212121;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton{\n"
                                     "background-color: #212121;\n"
                                     "Color: #eeeeee;\n"
                                     "border-radius: 20px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#AddButton{\n"
                                     "border: 2px solid #0d7377;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#AddButton:hover{\n"
                                     "border: 3px solid #32e0c4;\n"
                                     "background-color: #0d7377;\n"
                                     "}\n"
                                     "\n"
                                     "QLabel{\n"
                                     "color: #eeeeee;\n"
                                     "}\n"
                                     "\n"
                                     "QLabel#addNewBatchLabel{\n"
                                     "color: #32e0c4;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#cancelButton{\n"
                                     "border: 2px solid #9a0002;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#cancelButton:hover{\n"
                                     "border: 3px solid rgb(255, 0, 0);\n"
                                     "background-color: #9a0002;\n"
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
                                     "\n"
                                     "QDateEdit{\n"
                                     "border: 2px solid #0d7377;\n"
                                     "}\n"
                                     "\n"
                                     "QDateEdit:hover{\n"
                                     "border: 2px solid #32e0c4;\n"
                                     "}\n"
                                     "")
        self.gridLayout = QtWidgets.QGridLayout(AddBatchDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 140, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.addNewBatchLabel = QtWidgets.QLabel(AddBatchDialog)
        self.addNewBatchLabel.setMinimumSize(QtCore.QSize(300, 41))
        self.addNewBatchLabel.setMaximumSize(QtCore.QSize(300, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.addNewBatchLabel.setFont(font)
        self.addNewBatchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addNewBatchLabel.setObjectName("addNewBatchLabel")
        self.verticalLayout_4.addWidget(self.addNewBatchLabel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectCourseLabel = QtWidgets.QLabel(AddBatchDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectCourseLabel.setFont(font)
        self.selectCourseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectCourseLabel.setObjectName("selectCourseLabel")
        self.verticalLayout.addWidget(self.selectCourseLabel)
        self.courseComboBox = QtWidgets.QComboBox(AddBatchDialog)
        self.courseComboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.courseComboBox.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.courseComboBox.setFont(font)
        self.courseComboBox.setObjectName("courseComboBox")
        self.verticalLayout.addWidget(self.courseComboBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectDateLabel = QtWidgets.QLabel(AddBatchDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectDateLabel.setFont(font)
        self.selectDateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectDateLabel.setObjectName("selectDateLabel")
        self.verticalLayout_2.addWidget(self.selectDateLabel)
        self.dateEdit = QtWidgets.QDateEdit(AddBatchDialog)
        self.dateEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.dateEdit.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(date.today())
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddButton = QtWidgets.QPushButton(AddBatchDialog)
        self.AddButton.setMinimumSize(QtCore.QSize(100, 40))
        self.AddButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddButton.setFont(font)
        self.AddButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout.addWidget(self.AddButton)
        self.cancelButton = QtWidgets.QPushButton(AddBatchDialog)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 40))
        self.cancelButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT course_name FROM courses_table")
        result = mycursor.fetchall()
        for x in result:
            self.courseComboBox.addItem(x[0])

        # Button Calls
        self.AddButton.clicked.connect(self.addBatch)

        self.retranslateUi(AddBatchDialog)
        QtCore.QMetaObject.connectSlotsByName(AddBatchDialog)

    def addBatch(self):
        mycursor = mydb.cursor()
        selectedDate = self.dateEdit.date().toPyDate()
        selectedCourse = self.courseComboBox.currentText()
        mnth = selectedDate.strftime("%b").upper()
        yr = str(selectedDate.year)
        sql = "SELECT course_id, abbreviation FROM courses_table WHERE course_name = '" + selectedCourse + "'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        batchName = result[1] + mnth + yr
        print(result[0])
        query = "INSERT INTO batches_table (course_id, batch_name, start_date) VALUES(%s,%s,%s)"
        val = (result[0], batchName, selectedDate)
        mycursor.execute(query, val)
        c = mycursor.rowcount
        if mycursor.rowcount == 1:
            print("Data inserted successfully!")
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Successfully created a new batch " + batchName)
            msg.setWindowTitle("New Batch")
            msg.exec_()
            query = "CREATE TABLE IF NOT EXISTS bitsfinal." + batchName + "(id INT NOT NULL AUTO_INCREMENT, student_id INT NULL, course_id INT NULL, global_cert ENUM('Yes', 'No') NULL, PRIMARY KEY (`id`), FOREIGN KEY (student_id) REFERENCES student_info_table(student_id), FOREIGN KEY (course_id) REFERENCES courses_table(course_id))"
            mycursor.execute(query)
            mydb.commit()
        else:
            print("Problem occurred while inserting data")


    def retranslateUi(self, AddBatchDialog):
        _translate = QtCore.QCoreApplication.translate
        AddBatchDialog.setWindowTitle(_translate("AddBatchDialog", "Add New Batch"))
        self.addNewBatchLabel.setText(_translate("AddBatchDialog", "ADD NEW BATCH"))
        self.selectCourseLabel.setText(_translate("AddBatchDialog", "Select Course"))
        self.selectDateLabel.setText(_translate("AddBatchDialog", "Select Date"))
        self.dateEdit.setDisplayFormat(_translate("AddBatchDialog", "yyyy-MM-dd"))
        self.AddButton.setText(_translate("AddBatchDialog", "Add"))
        self.cancelButton.setText(_translate("AddBatchDialog", "Cancel"))