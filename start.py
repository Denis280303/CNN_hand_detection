import platform
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from splash_screen import Ui_Splash
from ui import Ui_MainWindow

counter = 0
class Splash(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash()
        self.ui.setupUi(self)
        ## Remove tittle bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(75)
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_2.setText("відбувається завантаження..."))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_2.setText("останні налаштування..."))

        self.show()
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


#app = QtWidgets.QApplication(sys.argv)
#load_window = Splash()
#sys.exit(app.exec_())