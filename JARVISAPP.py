from GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QTimer, QDate
from PyQt5.uic import loadUiType
import sys 
import Jarvis


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        Jarvis.wishMe()
        Jarvis.startExec()
        while True:
            Jarvis.takeCommand()

startExe = MainThread()  


class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)


    def startTask(self):
        self.gui.label1 = QtGui.QMovie("D://AI_project//Jarvis UI6.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start() 
        

        self.gui.label2 = QtGui.QMovie("D://AI_project//Jarvis UI5.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start() 
        

        self.gui.label3 = QtGui.QMovie("D://AI_project//Jarvis UI9.gif")
        self.gui.gif_3.setMovie(self.gui.label3)
        self.gui.label3.start() 

        startExe.start()

Guiapp = QApplication(sys.argv)
jarvis_gui = Gui_start()
jarvis_gui.show()
exit(Guiapp.exec_())