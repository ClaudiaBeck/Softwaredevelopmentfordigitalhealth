# Form implementation generated from reading ui file '/Users/claudiabeck/Desktop/pythonProject/venv/gui/errormsg.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ErrorWindow(object):
    def setupUi(self, ErrorWindow):
        ErrorWindow.setObjectName("ErrorWindow")
        ErrorWindow.resize(293, 183)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        ErrorWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=ErrorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 291, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.labelerror = QtWidgets.QLabel(parent=self.groupBox)
        self.labelerror.setGeometry(QtCore.QRect(20, 50, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelerror.setFont(font)
        self.labelerror.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelerror.setWordWrap(True)
        self.labelerror.setObjectName("labelerror")
        ErrorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ErrorWindow)
        self.statusbar.setObjectName("statusbar")
        ErrorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ErrorWindow)
        QtCore.QMetaObject.connectSlotsByName(ErrorWindow)

    def retranslateUi(self, ErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        ErrorWindow.setWindowTitle(_translate("ErrorWindow", "MainWindow"))
        self.labelerror.setText(_translate("ErrorWindow", "Wrong password and/or user-ID. Please try again."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorWindow = QtWidgets.QMainWindow()
    ui = Ui_ErrorWindow()
    ui.setupUi(ErrorWindow)
    ErrorWindow.show()
    sys.exit(app.exec())
