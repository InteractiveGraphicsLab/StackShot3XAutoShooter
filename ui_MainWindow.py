# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
        MainWindow.resize(800, 630)
        self.actionPreference = QAction(MainWindow)
        self.actionPreference.setObjectName(u"actionPreference")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.actionsText = QPlainTextEdit(self.centralwidget)
        self.actionsText.setObjectName(u"actionsText")
        self.actionsText.setGeometry(QRect(20, 50, 461, 421))
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(710, 560, 75, 23))
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(620, 560, 75, 23))
        self.actionsLabel = QLabel(self.centralwidget)
        self.actionsLabel.setObjectName(u"actionsLabel")
        self.actionsLabel.setGeometry(QRect(20, 20, 81, 21))
        font = QFont()
        font.setPointSize(16)
        self.actionsLabel.setFont(font)
        self.imageTmpPathLabel = QLabel(self.centralwidget)
        self.imageTmpPathLabel.setObjectName(u"imageTmpPathLabel")
        self.imageTmpPathLabel.setGeometry(QRect(500, 20, 161, 31))
        self.imageTmpPathLabel.setFont(font)
        self.imageSavePathLabel = QLabel(self.centralwidget)
        self.imageSavePathLabel.setObjectName(u"imageSavePathLabel")
        self.imageSavePathLabel.setGeometry(QRect(500, 100, 161, 31))
        self.imageSavePathLabel.setFont(font)
        self.imageTmpPath = QLineEdit(self.centralwidget)
        self.imageTmpPath.setObjectName(u"imageTmpPath")
        self.imageTmpPath.setGeometry(QRect(500, 50, 281, 31))
        self.imageSavePath = QLineEdit(self.centralwidget)
        self.imageSavePath.setObjectName(u"imageSavePath")
        self.imageSavePath.setGeometry(QRect(500, 130, 281, 31))
        self.bracketsLabel = QLabel(self.centralwidget)
        self.bracketsLabel.setObjectName(u"bracketsLabel")
        self.bracketsLabel.setGeometry(QRect(500, 180, 111, 31))
        self.bracketsLabel.setFont(font)
        self.brackets = QSpinBox(self.centralwidget)
        self.brackets.setObjectName(u"brackets")
        self.brackets.setGeometry(QRect(500, 210, 51, 31))
        self.brackets.setMinimum(1)
        self.doFocusStacking = QCheckBox(self.centralwidget)
        self.doFocusStacking.setObjectName(u"doFocusStacking")
        self.doFocusStacking.setGeometry(QRect(500, 260, 161, 31))
        self.doFocusStacking.setFont(font)
        self.doFocusStacking.setCheckable(True)
        self.doFocusStacking.setChecked(True)
        self.doFocusStacking.setTristate(False)
        self.heliconFocusCommandPath = QLineEdit(self.centralwidget)
        self.heliconFocusCommandPath.setObjectName(u"heliconFocusCommandPath")
        self.heliconFocusCommandPath.setGeometry(QRect(500, 330, 281, 31))
        self.heliconFocusCommandPathLabel = QLabel(self.centralwidget)
        self.heliconFocusCommandPathLabel.setObjectName(u"heliconFocusCommandPathLabel")
        self.heliconFocusCommandPathLabel.setGeometry(QRect(500, 300, 281, 31))
        self.heliconFocusCommandPathLabel.setFont(font)
        self.doMetashape = QCheckBox(self.centralwidget)
        self.doMetashape.setObjectName(u"doMetashape")
        self.doMetashape.setGeometry(QRect(500, 380, 161, 31))
        self.doMetashape.setFont(font)
        self.doMetashape.setCheckable(True)
        self.doMetashape.setChecked(True)
        self.doMetashape.setTristate(False)
        self.metashapeCommandPath = QLineEdit(self.centralwidget)
        self.metashapeCommandPath.setObjectName(u"metashapeCommandPath")
        self.metashapeCommandPath.setGeometry(QRect(500, 450, 281, 31))
        self.metashapeCommandPathLabel = QLabel(self.centralwidget)
        self.metashapeCommandPathLabel.setObjectName(u"metashapeCommandPathLabel")
        self.metashapeCommandPathLabel.setGeometry(QRect(500, 420, 281, 31))
        self.metashapeCommandPathLabel.setFont(font)
        self.metashapeProjectPath = QLineEdit(self.centralwidget)
        self.metashapeProjectPath.setObjectName(u"metashapeProjectPath")
        self.metashapeProjectPath.setGeometry(QRect(500, 520, 281, 31))
        self.metashapeProjectPathLabel = QLabel(self.centralwidget)
        self.metashapeProjectPathLabel.setObjectName(u"metashapeProjectPathLabel")
        self.metashapeProjectPathLabel.setGeometry(QRect(500, 490, 281, 31))
        self.metashapeProjectPathLabel.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuEdit.addAction(self.actionPreference)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPreference.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.actionsLabel.setText(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.imageTmpPathLabel.setText(QCoreApplication.translate("MainWindow", u"Image Tmp Path", None))
        self.imageSavePathLabel.setText(QCoreApplication.translate("MainWindow", u"Image Save Path", None))
        self.bracketsLabel.setText(QCoreApplication.translate("MainWindow", u"Brackets", None))
        self.doFocusStacking.setText(QCoreApplication.translate("MainWindow", u"FocusStacking", None))
        self.heliconFocusCommandPathLabel.setText(QCoreApplication.translate("MainWindow", u"HeliconFocus Command Path", None))
        self.doMetashape.setText(QCoreApplication.translate("MainWindow", u"Metashape", None))
        self.metashapeCommandPathLabel.setText(QCoreApplication.translate("MainWindow", u"Metashape Command Path", None))
        self.metashapeProjectPathLabel.setText(QCoreApplication.translate("MainWindow", u"Metashape Project Path", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

