from Assistant import Ui_Dialog
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

        self.gui = Ui_Dialog()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.gui.label = QtGui.QMovie("D:\\AI_project\\Voice assistant UI (2022_08_11 05_39_03 UTC).gif")
        self.gui.VoiceAssistantgif.setMovie(self.gui.label)
        self.gui.label.start() 
        startExe.start()
        

 

Guiapp = QApplication(sys.argv)
jarvis_gui = Gui_start()
jarvis_gui.show()
exit(Guiapp.exec_())