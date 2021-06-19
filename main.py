# SECTIONS IN THIS FILE
# FUNCTIONS IN REGISTRATION TAB
# FUNCTIONS IN SEARCH TAB
# FUNCTIONS IN BATCHES TAB
# FUNCTIONS IN UPDATE TAB
# FUNCTIONS IN PAYMENT TAB

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Registration import *
#from PyQt5.QtWidgets import QMessageBox
from HomePage import *
from Login import *
from chooseInPayment import *
from AddInstallments import *
from newTransaction import *
from ListOfTrans import *
from chooseInBatches import *
from chooseInRegistration import *
from batchAllotment import *
from Registration import *
from chooseInSearch import *
from searchInStudent import *
from updateStudentInfo import *
from updateInBatch import *
from chooseInUpdate import *
from UpdateCourse import *
# For Company Drives
from AddCompanyDrive_Final import *     # To add a drive
from add_company import *               # To add a company
from viewDrive import *                 # To view the drive
from CompanyDriveMain import *          # The main window to show the options for Company Drive
from report import *                    # To show the report tab
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="local",
    password="",
    database="mpdev"
)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.listTransaction = Ui_ListMainWindow()
        self.newtransaction = Ui_TransactionWindow()
        self.newinstallment = Ui_InstallmentWindow()
        self.payment = Ui_PaymentWindow()
        self.report = Ui_report()
        self.viewdrive = Ui_ViewDrive()
        self.addcompany  = Ui_AddCompany_Dailog()
        self.addcompanydrive  = Ui_AddDrive()
        self.companyDrive = Ui_ComanyDriveMain()
        self.batchAllotment = Ui_BatchAllotmentWindow()
        self.batches = Ui_BatchesWindow()
        self.newRegistration = Ui_NewRegistrationWindow()
        self.registration = Ui_RegistrationWindow()
        self.homeScreen = Ui_MainWindow()
        self.searchSection = Ui_SearchWindow()
        self.studentsSection = Ui_StudentsSectionWindow()
        self.update = Ui_UpdateWindow()
        self.updateStudentInfo = Ui_UpdateStudentInfo()
        self.updateBatch = Ui_UpdateBatchWindow()
        self.updateCourse = Ui_UpdateCourseWindow()
        self.loginpage = Ui_LoginPage()
        self.startLogin()

    # HOME

    def startLogin(self):
        self.loginpage.setupUi(self)
        self.setWindowTitle("Login Page")
        self.loginpage.login_Button.clicked.connect(self.Login)
        self.hide()
        self.showMaximized()


    def startHome(self):
        self.homeScreen.setupUi(self)
        self.setWindowTitle("Home")
        self.homeScreen.registration.clicked.connect(self.startRegistration)
        self.homeScreen.Batches.clicked.connect(self.startBatches)
        self.homeScreen.companydrives.clicked.connect(self.startCompanyDrives)
        self.homeScreen.pushButton_5.clicked.connect(self.startReport)
        self.homeScreen.Payment.clicked.connect(self.startPayment)
        self.homeScreen.Search.clicked.connect(self.startSearch)
        self.homeScreen.Update.clicked.connect(self.startUpdate)
        self.hide()
        self.showMaximized()
        # self.showFullScreen()
    # REGISTRATION

    def startRegistration(self):
        self.registration.setupUi(self)
        self.setWindowTitle("Registration")
        self.registration.newRegistrationButton.clicked.connect(self.startNewRegistration)
        self.registration.cancelButton.clicked.connect(self.startHome)
        self.hide()
        # self.showFullScreen()
        self.showMaximized()
        # maxmizes the Window

    def startNewRegistration(self):
        self.newRegistration.setupUi(self)
        self.setWindowTitle("New Registration")
        self.newRegistration.cancelButton.clicked.connect(self.startRegistration)
        self.hide()
        self.showMaximized()
        # self.showFullScreen()
    # BATCHES

    def startBatches(self):
        self.batches.setupUi(self)
        self.setWindowTitle("Batches")
        self.hide()
        self.showMaximized()
        self.batches.addBatchButton.clicked.connect(self.batches.addBatch)
        self.batches.allotBatchButton.clicked.connect(self.startBatchAllotment)
        self.batches.cancelButton.clicked.connect(self.startHome)

    def startBatchAllotment(self):
        self.batchAllotment.setupUi(self)
        self.hide()
        self.showMaximized()
        self.batchAllotment.cancelButton.clicked.connect(self.startBatches)

    def startCompanyDrives(self):   # This is open the Window of Company Drive with the options
        self.companyDrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Company Drives")
        self.companyDrive.addDrive_Button.clicked.connect(self.addCompanyDrive)
        self.companyDrive.addCompany_Button.clicked.connect(self.addCompany)
        self.companyDrive.viewDrive_Button.clicked.connect(self.viewDriveCall)
        self.companyDrive.backHome_Button.clicked.connect(self.startHome)
        self.hide()
        self.showMaximized()


    # Login Vetting
    def Login(self):
        username = self.loginpage.username_lineEdit.text().strip()
        password = self.loginpage.password_lineEdit.text()

        if not username or not password:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Username or Password cannot be empty!")
            msg.exec_()
            return

        if username != 'bits_pune' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Incorrect Username")
            msg.exec_()
            self.loginpage.username_lineEdit.clear()
            self.loginpage.password_lineEdit.clear()

        elif password !='golden@202bits':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Incorrect Password")
            msg.exec_()
            self.loginpage.password_lineEdit.clear()

        elif username =='bits_pune' and password =='golden@202bits':
            self.startHome()


    # COMPANY DRIVES

    def addCompanyDrive(self):   # This will open the Add Drive Window
        self.addcompanydrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.addcompanydrive.cancel_Button.clicked.connect(self.startCompanyDrives) # if he clicks cancel while adding Drive go back to CompanyDrive  main

    def addCompany(self):  #This show the dialog box to add Company Name to Company List
        self.x = QtWidgets.QDialog()
        self.addcompany.setupUi(self.x)
        self.addcompany.cancelButton.clicked.connect(self.x.hide)
        self.x.show()

    def viewDriveCall(self):   # This Shows all the existing Company Drives.
        self.viewdrive.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.viewdrive.back_Button.clicked.connect(self.startCompanyDrives)

    # REPORT AND STATS

    def startReport(self):
        self.report.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.showMaximized()
        self.report.backHome_Button.clicked.connect(self.startHome)
    # FUNCTIONS IN SEARCH TAB
    # FUNCTIONS IN BATCHES TAB
    # FUNCTIONS IN UPDATE TAB
    # FUNCTIONS IN PAYMENT TAB
    def startPayment(self):
        self.payment.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Payment")
        self.payment.cancelButton.clicked.connect(self.startHome)
        self.payment.installmentButton.clicked.connect(self.addInstallment)
        self.payment.transactionButton.clicked.connect(self.newTransaction)
        self.payment.listTransactionsButton.clicked.connect(self.newListTransaction)
        self.hide()
        self.showMaximized()

    # Add Installment Tab
    def addInstallment(self):
        self.newinstallment.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("Add Installments")
        # self.newinstallment.addButton.clicked.connect(self.addingInstallment)
        # self.newinstallment.submitButton.clicked.connect(self.submitInstallment)
        self.newinstallment.cancelButton.clicked.connect(self.startPayment)
        self.hide()
        self.showMaximized()



    # New transaction tab
    def newTransaction(self):
        self.newtransaction.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("New Transaction")
        self.newtransaction.cancelButton.clicked.connect(self.startPayment)
        # add functions
        self.hide()
        self.showMaximized()

    #List Transaction button call
    def newListTransaction(self):
        self.listTransaction.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle("List Of Transactions")
        self.listTransaction.backButton.clicked.connect(self.startPayment)
        self.hide()
        self.showMaximized()


    # SEARCH

    def startSearch(self):
        self.searchSection.setupUi(self)
        self.setWindowTitle("Search")
        self.hide()
        self.showMaximized()
        self.searchSection.backButton.clicked.connect(self.startHome)
        self.searchSection.studentButton.clicked.connect(self.startSearchInStudents)

    def startSearchInStudents(self):
        self.studentsSection.setupUi(self)
        self.setWindowTitle("Students Section")
        self.hide()
        self.showMaximized()
        self.studentsSection.cancelButton.clicked.connect(self.startSearch)

    # UPDATE

    def startUpdate(self):
        self.update.setupUi(self)
        self.setWindowTitle("Update Section")
        self.hide()
        self.showMaximized()
        self.update.studentButton.clicked.connect(self.startUpdateStudentInfo)
        self.update.batchButton.clicked.connect(self.startUpdateInBatch)
        self.update.courseButton.clicked.connect(self.startUpdateInCourse)
        self.update.backButton.clicked.connect(self.startHome)

    def startUpdateStudentInfo(self):
        self.updateStudentInfo.setupUi(self)
        self.setWindowTitle("Update Student Info")
        self.hide()
        self.showMaximized()
        self.updateStudentInfo.backButton.clicked.connect(self.startUpdate)

    def startUpdateInCourse(self):
        self.updateCourse.setupUi(self)
        self.setWindowTitle("Update in Courses")
        self.hide()
        self.showMaximized()
        self.updateCourse.backButton.clicked.connect(self.startUpdate)
        self.updateCourse.backButton_2.clicked.connect(self.startUpdate)

    def startUpdateInBatch(self):
        self.updateBatch.setupUi(self)
        self.setWindowTitle("Update In Batch")
        self.hide()
        self.showMaximized()
        self.updateBatch.backButton_2.clicked.connect(self.startUpdate)
        self.updateBatch.backButton_3.clicked.connect(self.startUpdate)
        self.updateBatch.backButton_4.clicked.connect(self.startUpdate)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
