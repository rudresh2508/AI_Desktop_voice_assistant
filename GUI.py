# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Jarvis Gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\AI_project\I7.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(56, 70, 701, 411))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:\AI_project\JARVIS_BG.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 410, 111, 61))
        self.pushButton.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 24pt \"Viner Hand ITC\";\n"
"background-color: transparent")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 410, 111, 61))
        self.pushButton_2.setStyleSheet("color: rgb(0, 255, 255);\n"
"font: 24pt \"Viner Hand ITC\";\n"
"background-color: transparent")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(60, 80, 361, 71))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap("D:\AI_project\Jarvis UI6.gif"))
        self.gif_1.setObjectName("gif_1")
        self.gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.gif_2.setGeometry(QtCore.QRect(600, 80, 141, 121))
        self.gif_2.setText("")
        self.gif_2.setPixmap(QtGui.QPixmap("D:\AI_project\Jarvis UI5.gif"))
        self.gif_2.setScaledContents(True)
        self.gif_2.setObjectName("gif_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 200, 47, 13))
        self.label_3.setObjectName("label_3")
        self.gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.gif_3.setGeometry(QtCore.QRect(210, 160, 381, 251))
        self.gif_3.setText("")
        self.gif_3.setPixmap(QtGui.QPixmap("D:\AI_project\Jarvis UI9.gif"))
        self.gif_3.setScaledContents(False)
        self.gif_3.setObjectName("gif_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())