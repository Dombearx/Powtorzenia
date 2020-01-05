# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import test as utils

class Ui_MainWindow(object):

    def __init__(self):
        self.dublicates = []
        self.filename = ""
        self.model = QtGui.QStandardItemModel()
        

    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 20, 321, 361))
        self.listView.setObjectName("listView")
        self.buttonCheck = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCheck.setGeometry(QtCore.QRect(20, 390, 321, 161))
        self.buttonCheck.setObjectName("buttonCheck")
        self.buttonBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBrowse.setGeometry(QtCore.QRect(390, 60, 341, 141))
        self.buttonBrowse.setObjectName("buttonBrowse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.listView.setModel(self.model)

        self.retranslateUi(MainWindow)
        self.attachEvents()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonCheck.setText(_translate("MainWindow", "Sprawdź!"))
        self.buttonBrowse.setText(_translate("MainWindow", "Przeglądaj"))

    def attachEvents(self):
        self.buttonCheck.clicked.connect(self.check)
        self.buttonBrowse.clicked.connect(self.browse)

    def browse(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainWindow,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            self.model.clear()
            item = QtGui.QStandardItem("Wybrany plik: " + self.fileName)
            self.model.appendRow(item)
    
    def check(self):
        self.dublicates = utils.getDublicates(self.fileName)

        for dub, num in self.dublicates:
            i = "Wyraz: " + dub + "\t Liczba wystąpień: " + str(num)
            item = QtGui.QStandardItem(i)
            self.model.appendRow(item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
