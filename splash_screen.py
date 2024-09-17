# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenzyZbZD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(680, 400)
        Splash.setMaximumSize(QSize(680, 400))
        icon = QIcon()
        icon.addFile(u"premium-icon-personal-computer-5416362.png", QSize(), QIcon.Normal, QIcon.Off)
        Splash.setWindowIcon(icon)
        Splash.setStyleSheet(u"background-color: rgb(11, 61, 135);")
        self.centralwidget = QWidget(Splash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	color: rgb(213, 255, 251);\n"
"	background-color: rgb(15, 82, 186);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setLineWidth(0)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.dropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 150, 661, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(21)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(155, 198, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(87, 250, 531, 23))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(155, 198, 255);\n"
"	color:rgb(0, 0, 255);\n"
"	border-radius:10px;\n"
"	border-style: none;\n"
"	text-align:center;\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0.119, x2:1, y2:0, stop:0 rgba(8, 0, 48, 255), stop:1 rgba(115, 184, 255, 255));\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0435\u043d\u043d\u044f \u0434\u043e\u0434\u0430\u0442\u043a\u0443 MCV", None))
        self.label.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p><span style=\" font-weight:600;\">MCV: \u043a\u0435\u0440\u0443\u0432\u0430\u043d\u043d\u044f \u043a\u043e\u043c\u043f'\u044e\u0442\u0435\u0440\u043d\u0438\u043c \u0437\u043e\u0440\u043e\u043c</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p align=\"center\">\u0432\u0456\u0434\u0431\u0443\u0432\u0430\u0454\u0442\u044c\u0441\u044f \u0437\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0435\u043d\u043d\u044f...</p></body></html>", None))
    # retranslateUi

