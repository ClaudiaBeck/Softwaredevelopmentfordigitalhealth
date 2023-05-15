from PyQt6 import QtCore, QtGui, QtWidgets
from classes.database import *
from searchPatient import SearchPatient
from errormsg1 import ErrorWindow1
# Above we have imported relevant elements from other scripts.

class MainLogin(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(386, 266)
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 371, 241))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 90, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.passwordlabel = QtWidgets.QLabel(parent=self.groupBox)
        self.passwordlabel.setGeometry(QtCore.QRect(20, 140, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setObjectName("passwordlabel")
        self.title = QtWidgets.QLabel(parent=self.groupBox)
        self.title.setGeometry(QtCore.QRect(110, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.lineEdituserID = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdituserID.setGeometry(QtCore.QRect(100, 90, 171, 21))
        self.lineEdituserID.setObjectName("lineEdituserID")
        self.lineEditpassword = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditpassword.setGeometry(QtCore.QRect(100, 140, 171, 21))
        self.lineEditpassword.setObjectName("lineEditpassword")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.userIDlabel = QtWidgets.QLabel(parent=self.groupBox)
        self.userIDlabel.setGeometry(QtCore.QRect(20, 90, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.userIDlabel.setFont(font)
        self.userIDlabel.setObjectName("userIDlabel")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "User-ID:"))
        self.passwordlabel.setText(_translate("LoginWindow", "Password:"))
        self.title.setText(_translate("LoginWindow", "Please log in to EDR"))
        self.pushButton.setText(_translate("LoginWindow", "Login"))
        self.userIDlabel.setText(_translate("LoginWindow", "User-ID:"))

#######
        self.pushButton.clicked.connect(self.login)
        # This connects the push button with the login method. It runs the method when clicking the button.

    def login(self):
        '''Runs the check_username_password function from the database script with username and password as arguments. Returns a boolean. If true: change window.'''
        username_input = self.lineEdituserID.text()
        password_input = self.lineEditpassword.text()
        if check_username_password(username_input, password_input):
            self.changeWindow()
        else:
            self.errormsg()


    def changeWindow(self):
        '''This method changes the login window to the search window upon successful login'''
        self.window = QtWidgets.QMainWindow()
        self.ui = SearchPatient()
        self.ui.setupUi(self.window)
        LoginWindow.hide()
        self.window.show()


    def errormsg(self):
        '''This method shows an errormessage window in front of the login message if login is unsuccessful'''
        self.window = QtWidgets.QMainWindow()
        self.ui = ErrorWindow1()
        self.ui.setupUi(self.window)
        self.window.show()

#######

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = MainLogin()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())