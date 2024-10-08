# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(462, 600))
        MainWindow.setMaximumSize(QtCore.QSize(462, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Denis/Desktop/PLATFORMER/MCV/Virual-Mouse-main/src/premium-icon-personal-computer-5416362.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: #0F52BA")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 20, 481, 81))
        self.frame.setStyleSheet("background-color: #87CEEB;\n"
"border-radius: 10px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #0818A8;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: #0818A8;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 241, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/Denis/Desktop/PLATFORMER/MCV/Virual-Mouse-main/src/premium-icon-personal-computer-5416362.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButtonMouse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMouse.setGeometry(QtCore.QRect(20, 470, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonMouse.setFont(font)
        self.pushButtonMouse.setStyleSheet("QPushButton{\n"
"    color: #0818A8;\n"
"    background-color:#87CEEB;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#40B5AD;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"}\n"
"")
        self.pushButtonMouse.setObjectName("pushButtonMouse")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 140, 241, 231))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/Denis/Desktop/PLATFORMER/MCV/Virual-Mouse-main/src/premium-icon-personal-computer-5416362.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-160, 140, 241, 231))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Denis/Desktop/PLATFORMER/MCV/Virual-Mouse-main/src/premium-icon-personal-computer-5416362.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonGraphic = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGraphic.setGeometry(QtCore.QRect(240, 470, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonGraphic.setFont(font)
        self.pushButtonGraphic.setStyleSheet("QPushButton{\n"
"    color: #0818A8;\n"
"    background-color:#87CEEB;\n"
"    border-radius: 30;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:#40B5AD;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"}\n"
"")
        self.pushButtonGraphic.setObjectName("pushButtonGraphic")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, 570, 481, 31))
        self.frame_2.setStyleSheet("background-color: #87CEEB;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(130, 0, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ДОДАТОК MCV"))
        self.label.setText(_translate("MainWindow", "MCV"))
        self.label_2.setText(_translate("MainWindow", "management computer vision"))
        self.pushButtonMouse.setText(_translate("MainWindow", "КЕРУВАННЯ МИШОЮ"))
        self.pushButtonGraphic.setText(_translate("MainWindow", "ГРАФІКА ЖЕСТАМИ"))
        self.label_8.setText(_translate("MainWindow", "Розроблено Козловським Денисом ©"))


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""
