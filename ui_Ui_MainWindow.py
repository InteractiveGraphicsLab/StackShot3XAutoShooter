# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.actionsText = QPlainTextEdit(self.centralwidget)
        self.actionsText.setObjectName(u"actionsText")
        self.actionsText.setGeometry(QRect(20, 60, 461, 421))
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(710, 530, 75, 23))
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(620, 530, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 81, 21))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 30, 161, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 110, 161, 31))
        self.label_3.setFont(font)
        self.imageTmpPath = QLineEdit(self.centralwidget)
        self.imageTmpPath.setObjectName(u"imageTmpPath")
        self.imageTmpPath.setGeometry(QRect(510, 60, 271, 31))
        self.imageSavePath = QLineEdit(self.centralwidget)
        self.imageSavePath.setObjectName(u"imageSavePath")
        self.imageSavePath.setGeometry(QRect(510, 140, 271, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(510, 190, 111, 31))
        self.label_4.setFont(font)
        self.brackets = QSpinBox(self.centralwidget)
        self.brackets.setObjectName(u"brackets")
        self.brackets.setGeometry(QRect(510, 220, 51, 31))
        self.brackets.setMinimum(1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Image Tmp Path", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Image Save Path", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Brackets", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
