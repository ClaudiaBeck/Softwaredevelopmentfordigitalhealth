from PyQt6 import QtCore, QtGui, QtWidgets
from classes.database import *
from patientInfo import PatientInfo
from errormsg2 import ErrorWindow2

class SearchPatient(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(374, 252)
        self.centralwidget = QtWidgets.QWidget(parent=SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -20, 371, 251))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.title = QtWidgets.QLabel(parent=self.groupBox)
        self.title.setGeometry(QtCore.QRect(100, 50, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.CPRlabel = QtWidgets.QLabel(parent=self.groupBox)
        self.CPRlabel.setGeometry(QtCore.QRect(20, 110, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CPRlabel.setFont(font)
        self.CPRlabel.setObjectName("CPRlabel")
        self.lineEditCPR = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditCPR.setGeometry(QtCore.QRect(130, 110, 201, 21))
        self.lineEditCPR.setObjectName("lineEditCPR")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 113, 32))
        self.pushButton.setObjectName("pushButton")
        SearchWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.title.setText(_translate("SearchWindow", "Search for patient in EDR"))
        self.CPRlabel.setText(_translate("SearchWindow", "CPR-number:"))
        self.pushButton.setText(_translate("SearchWindow", "Search"))

######
        self.pushButton.clicked.connect(self.search)
        # This connects the pushbutton with the search method and runs it.

    def search(self):
        '''This function runs the search_patient function from the database script with CPR number as argument. If true: run the patientinfo method.'''
        CPR_number = self.lineEditCPR.text()
        if search_patient(CPR_number):
            self.patientinfo(CPR_number)
        else:
            self.errormsg2()


    def patientinfo(self, CPR_number):
        '''This method changes the search window into the patient information window and makes sure that we pass the CPR number as an argument in the setupui argument.'''
        self.window = QtWidgets.QMainWindow()
        self.ui = PatientInfo()
        self.ui.setupUi(self.window, CPR_number)
        self.window.show()


    def errormsg2(self):
        '''This method shows an errormessage window in front of the seach window if an invalid CPR-number has been entered'''
        self.window = QtWidgets.QMainWindow()
        self.ui = ErrorWindow2()
        self.ui.setupUi(self.window)
        self.window.show()
######


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec())