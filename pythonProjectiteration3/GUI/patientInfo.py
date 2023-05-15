from PyQt6 import QtCore, QtGui, QtWidgets
from classes.database import *

class PatientInfo(object):
    def __init__(self):
        self.name = None
        self.address = None
        self.phone = None
        self.email = None
        self.cprnumber = None
        # Above we initialize and declare 5 empty variables we are going to use later.

    def setupUi(self, Patientinfowindow, cpr):
        # We have added cpr as an argument here because (see line 89).
        Patientinfowindow.setObjectName("Patientinfowindow")
        Patientinfowindow.resize(501, 447)
        self.centralwidget = QtWidgets.QWidget(parent=Patientinfowindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 481, 411))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.title = QtWidgets.QLabel(parent=self.groupBox)
        self.title.setGeometry(QtCore.QRect(180, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.name_label = QtWidgets.QLabel(parent=self.groupBox)
        self.name_label.setGeometry(QtCore.QRect(20, 70, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.cpr_label = QtWidgets.QLabel(parent=self.groupBox)
        self.cpr_label.setGeometry(QtCore.QRect(20, 110, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cpr_label.setFont(font)
        self.cpr_label.setObjectName("cpr_label")
        self.address_label = QtWidgets.QLabel(parent=self.groupBox)
        self.address_label.setGeometry(QtCore.QRect(20, 160, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.phone_label = QtWidgets.QLabel(parent=self.groupBox)
        self.phone_label.setGeometry(QtCore.QRect(20, 210, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 330, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.patientname = QtWidgets.QLabel(parent=self.groupBox)
        self.patientname.setGeometry(QtCore.QRect(160, 70, 301, 16))
        self.patientname.setObjectName("patientname")
        self.patientcpr = QtWidgets.QLabel(parent=self.groupBox)
        self.patientcpr.setGeometry(QtCore.QRect(160, 110, 301, 16))
        self.patientcpr.setObjectName("patientcpr")
        self.patientaddress = QtWidgets.QLabel(parent=self.groupBox)
        self.patientaddress.setGeometry(QtCore.QRect(160, 160, 301, 16))
        self.patientaddress.setObjectName("patientaddress")
        self.patientphone = QtWidgets.QLabel(parent=self.groupBox)
        self.patientphone.setGeometry(QtCore.QRect(160, 210, 301, 16))
        self.patientphone.setObjectName("patientphone")
        self.email_label = QtWidgets.QLabel(parent=self.groupBox)
        self.email_label.setGeometry(QtCore.QRect(20, 260, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.patientemail = QtWidgets.QLabel(parent=self.groupBox)
        self.patientemail.setGeometry(QtCore.QRect(160, 260, 291, 16))
        self.patientemail.setObjectName("patientemail")
        Patientinfowindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Patientinfowindow)
        self.statusbar.setObjectName("statusbar")
        Patientinfowindow.setStatusBar(self.statusbar)

        self.updateInfo(cpr)
        # The variables from above that are used for the text labels are updated.
        # It is important that we update the variables before we retranslate the UI because these variables are used when retranslating.

        self.retranslateUi(Patientinfowindow)
        QtCore.QMetaObject.connectSlotsByName(Patientinfowindow)

######

    def retranslateUi(self, Patientinfowindow):
        _translate = QtCore.QCoreApplication.translate
        Patientinfowindow.setWindowTitle(_translate("Patientinfowindow", "MainWindow"))
        self.title.setText(_translate("Patientinfowindow", "Patient information"))
        self.name_label.setText(_translate("Patientinfowindow", "Name:"))
        self.cpr_label.setText(_translate("Patientinfowindow", "CPR-number:"))
        self.address_label.setText(_translate("Patientinfowindow", "Address:"))
        self.phone_label.setText(_translate("Patientinfowindow", "Phone number:"))
        self.pushButton.setText(_translate("Patientinfowindow", "View journal"))

        # Below we have added the variables in the respective labels (before it was just: "TextLabel").
        # 'self' is used in front of the variables to refer back to the same class and make sure that it is the variables from above that we using and not random variables.
        self.patientname.setText(_translate("Patientinfowindow", self.name))
        self.patientcpr.setText(_translate("Patientinfowindow", self.cprnumber))
        self.patientaddress.setText(_translate("Patientinfowindow", self.address))
        self.patientphone.setText(_translate("Patientinfowindow", self.phone))
        self.email_label.setText(_translate("Patientinfowindow", "E-mail:"))
        self.patientemail.setText(_translate("Patientinfowindow", self.email))


    def updateInfo(self, cpr):
        '''This function stores the results from the fetch_patientinfo method from the database script in 5 variables that make sense.'''
        name, address, phone, email, cprnumber = fetch_patientinfo(cpr)
        # The variables are used to define what needs to be put into the textlabels on the GUI.
        self.name = name
        # Explanation: We are setting the variables from the beginning of the script (which was set to None) equal to the 'name' variable (in this method) that was returned from the fetch_patientinfo method.
        self.address = address
        self.phone = phone
        self.email = email
        self.cprnumber = cprnumber

######

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Patientinfowindow = QtWidgets.QMainWindow()
    ui = Patientinfowindow()
    ui.setupUi(Patientinfowindow)
    Patientinfowindow.show()
    sys.exit(app.exec())