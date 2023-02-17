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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

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
        self.actionsLabel = QLabel(self.centralwidget)
        self.actionsLabel.setObjectName(u"actionsLabel")
        self.actionsLabel.setGeometry(QRect(20, 30, 81, 21))
        font = QFont()
        font.setPointSize(16)
        self.actionsLabel.setFont(font)
        self.imageTmpPathLabel = QLabel(self.centralwidget)
        self.imageTmpPathLabel.setObjectName(u"imageTmpPathLabel")
        self.imageTmpPathLabel.setGeometry(QRect(510, 30, 161, 31))
        self.imageTmpPathLabel.setFont(font)
        self.imageSavePathLabel = QLabel(self.centralwidget)
        self.imageSavePathLabel.setObjectName(u"imageSavePathLabel")
        self.imageSavePathLabel.setGeometry(QRect(510, 110, 161, 31))
        self.imageSavePathLabel.setFont(font)
        self.imageTmpPath = QLineEdit(self.centralwidget)
        self.imageTmpPath.setObjectName(u"imageTmpPath")
        self.imageTmpPath.setGeometry(QRect(510, 60, 271, 31))
        self.imageSavePath = QLineEdit(self.centralwidget)
        self.imageSavePath.setObjectName(u"imageSavePath")
        self.imageSavePath.setGeometry(QRect(510, 140, 271, 31))
        self.bracketsLabel = QLabel(self.centralwidget)
        self.bracketsLabel.setObjectName(u"bracketsLabel")
        self.bracketsLabel.setGeometry(QRect(510, 190, 111, 31))
        self.bracketsLabel.setFont(font)
        self.brackets = QSpinBox(self.centralwidget)
        self.brackets.setObjectName(u"brackets")
        self.brackets.setGeometry(QRect(510, 220, 51, 31))
        self.brackets.setMinimum(1)
        self.doFocusStacking = QCheckBox(self.centralwidget)
        self.doFocusStacking.setObjectName(u"doFocusStacking")
        self.doFocusStacking.setGeometry(QRect(510, 270, 161, 31))
        self.doFocusStacking.setFont(font)
        self.doFocusStacking.setCheckable(True)
        self.doFocusStacking.setChecked(True)
        self.doFocusStacking.setTristate(False)
        self.focusStackingCommand = QLineEdit(self.centralwidget)
        self.focusStackingCommand.setObjectName(u"focusStackingCommand")
        self.focusStackingCommand.setGeometry(QRect(510, 340, 271, 31))
        self.focusStackingCommandLabel = QLabel(self.centralwidget)
        self.focusStackingCommandLabel.setObjectName(u"focusStackingCommandLabel")
        self.focusStackingCommandLabel.setGeometry(QRect(510, 310, 251, 31))
        self.focusStackingCommandLabel.setFont(font)
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
        self.actionsLabel.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.imageTmpPathLabel.setText(QCoreApplication.translate("MainWindow", u"Image Tmp Path", None))
        self.imageSavePathLabel.setText(QCoreApplication.translate("MainWindow", u"Image Save Path", None))
        self.bracketsLabel.setText(QCoreApplication.translate("MainWindow", u"Brackets", None))
        self.doFocusStacking.setText(QCoreApplication.translate("MainWindow", u"FocusStacking", None))
        self.focusStackingCommandLabel.setText(QCoreApplication.translate("MainWindow", u"Focus Stacking Command", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

