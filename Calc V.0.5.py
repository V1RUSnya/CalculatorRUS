# -*- coding: cp1251 -*-
import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 341)
        self.lcd = 0
        def button_cliked(num):
            if num == "x" or num == "%" or num == "+" or num == "-":
                self.opt = num
                if self.MemoryLabel.text() == "":
                    self.lastnumber = self.lcd
                    self.MemoryLabel.setText(str(self.lcd) + " " + self.opt)
                    self.lcd = 0
                    self.lcdNumber.display(int(self.lcd))
                else:
                    self.lcd = 0
                    self.MemoryLabel.setText("")
                    self.lcdNumber.display(int(self.lcd))
            elif num != "=":
                self.lcd = str(self.lcd) + str(num)
                self.lcd = int(self.lcd)
                self.lcdNumber.display(self.lcd)
            else:
                if self.opt == "+":
                    self.lcd = int(self.lastnumber) + int(self.lcd)
                    self.lcdNumber.display(int(self.lcd))
                elif self.opt == "-":
                    self.lcd = int(self.lastnumber) - int(self.lcd)
                    self.lcdNumber.display(int(self.lcd))
                elif self.opt == "x":
                    self.lcd = int(self.lastnumber) * int(self.lcd)
                    self.lcdNumber.display(int(self.lcd))                    
                elif self.opt == "%":
                    self.lcd = int(self.lastnumber) / int(self.lcd)
                    self.lcdNumber.display(int(self.lcd))
                self.MemoryLabel.setText("")
                    
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.But7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But7.setGeometry(QtCore.QRect(0, 100, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But7.setFont(font)
        self.But7.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But7.setDefault(False)
        self.But7.setFlat(False)
        self.But7.setObjectName("But7")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.ButonOfPersent = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButonOfPersent.setGeometry(QtCore.QRect(210, 100, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.ButonOfPersent.setFont(font)
        self.ButonOfPersent.setStyleSheet("background-color: rgb(153, 153, 153)")
        self.ButonOfPersent.setObjectName("ButonOfPersent")
        self.But4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But4.setGeometry(QtCore.QRect(0, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But4.setFont(font)
        self.But4.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But4.setDefault(False)
        self.But4.setFlat(False)
        self.But4.setObjectName("But4")
        self.But6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But6.setGeometry(QtCore.QRect(140, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But6.setFont(font)
        self.But6.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But6.setDefault(False)
        self.But6.setFlat(False)
        self.But6.setObjectName("But6")
        self.But1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But1.setGeometry(QtCore.QRect(0, 220, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But1.setFont(font)
        self.But1.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But1.setDefault(False)
        self.But1.setFlat(False)
        self.But1.setObjectName("But1")
        self.But2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But2.setGeometry(QtCore.QRect(70, 220, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But2.setFont(font)
        self.But2.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But2.setDefault(False)
        self.But2.setFlat(False)
        self.But2.setObjectName("But2")
        self.But9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But9.setGeometry(QtCore.QRect(140, 100, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But9.setFont(font)
        self.But9.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But9.setDefault(False)
        self.But9.setFlat(False)
        self.But9.setObjectName("But9")
        self.But8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But8.setGeometry(QtCore.QRect(70, 100, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But8.setFont(font)
        self.But8.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But8.setDefault(False)
        self.But8.setFlat(False)
        self.But8.setObjectName("But8")
        self.But5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But5.setGeometry(QtCore.QRect(70, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But5.setFont(font)
        self.But5.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But5.setDefault(False)
        self.But5.setFlat(False)
        self.But5.setObjectName("But5")
        self.ButDot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButDot.setGeometry(QtCore.QRect(140, 280, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.ButDot.setFont(font)
        self.ButDot.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.ButDot.setDefault(False)
        self.ButDot.setFlat(False)
        self.ButDot.setObjectName("ButDot")
        self.But0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But0.setGeometry(QtCore.QRect(0, 280, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But0.setFont(font)
        self.But0.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But0.setDefault(False)
        self.But0.setFlat(False)
        self.But0.setObjectName("But0")
        self.But3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.But3.setGeometry(QtCore.QRect(140, 220, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.But3.setFont(font)
        self.But3.setStyleSheet("background-color: rgb(255, 128, 0)")
        self.But3.setDefault(False)
        self.But3.setFlat(False)
        self.But3.setObjectName("But3")
        self.ButtonRavno = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonRavno.setGeometry(QtCore.QRect(210, 280, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.ButtonRavno.setFont(font)
        self.ButtonRavno.setStyleSheet("background-color: rgb(153, 153, 153)")
        self.ButtonRavno.setObjectName("ButtonRavno")
        self.ButtonPlus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonPlus.setGeometry(QtCore.QRect(210, 240, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.ButtonPlus.setFont(font)
        self.ButtonPlus.setStyleSheet("background-color: rgb(153, 153, 153)")
        self.ButtonPlus.setObjectName("ButtonPlus")
        self.ButtonMinus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonMinus.setGeometry(QtCore.QRect(210, 200, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.ButtonMinus.setFont(font)
        self.ButtonMinus.setStyleSheet("background-color: rgb(153, 153, 153)")
        self.ButtonMinus.setObjectName("ButtonMinus")
        self.ButtonOfX = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonOfX.setGeometry(QtCore.QRect(210, 150, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.ButtonOfX.setFont(font)
        self.ButtonOfX.setStyleSheet("background-color: rgb(153, 153, 153)")
        self.ButtonOfX.setObjectName("ButtonOfX")
        self.MemoryLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.MemoryLabel.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.MemoryLabel.setStyleSheet("color: white;")
        self.MemoryLabel.setObjectName("MemoryLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.But1.clicked.connect(lambda: button_cliked(1))
        self.But2.clicked.connect(lambda: button_cliked(2))
        self.But3.clicked.connect(lambda: button_cliked(3))
        self.But4.clicked.connect(lambda: button_cliked(4))
        self.But5.clicked.connect(lambda: button_cliked(5))
        self.But6.clicked.connect(lambda: button_cliked(6))
        self.But7.clicked.connect(lambda: button_cliked(7))
        self.But8.clicked.connect(lambda: button_cliked(8))
        self.But9.clicked.connect(lambda: button_cliked(9))
        self.ButtonPlus.clicked.connect(lambda: button_cliked("+"))
        self.ButtonMinus.clicked.connect(lambda: button_cliked("-"))
        self.ButtonOfX.clicked.connect(lambda: button_cliked("x"))
        self.ButonOfPersent.clicked.connect(lambda: button_cliked("%"))
        self.ButtonRavno.clicked.connect(lambda: button_cliked("="))
        self.MemoryLabel.setText("")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.But7.setText(_translate("MainWindow", "7"))
        self.ButonOfPersent.setText(_translate("MainWindow", "%"))
        self.But4.setText(_translate("MainWindow", "4"))
        self.But6.setText(_translate("MainWindow", "6"))
        self.But1.setText(_translate("MainWindow", "1"))
        self.But2.setText(_translate("MainWindow", "2"))
        self.But9.setText(_translate("MainWindow", "9"))
        self.But8.setText(_translate("MainWindow", "8"))
        self.But5.setText(_translate("MainWindow", "5"))
        self.ButDot.setText(_translate("MainWindow", "."))
        self.But0.setText(_translate("MainWindow", "0"))
        self.But3.setText(_translate("MainWindow", "3"))
        self.ButtonRavno.setText(_translate("MainWindow", "="))
        self.ButtonPlus.setText(_translate("MainWindow", "+"))
        self.ButtonMinus.setText(_translate("MainWindow", "-"))
        self.ButtonOfX.setText(_translate("MainWindow", "X"))
        self.MemoryLabel.setText(_translate("MainWindow", ""))
  
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
