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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(672, 540)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.actionsPanelLabel = QLabel(self.centralwidget)
        self.actionsPanelLabel.setObjectName(u"actionsPanelLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionsPanelLabel.sizePolicy().hasHeightForWidth())
        self.actionsPanelLabel.setSizePolicy(sizePolicy)
        self.actionsPanelLabel.setFont(font)

        self.verticalLayout.addWidget(self.actionsPanelLabel)

        self.actionsPanel = QPlainTextEdit(self.centralwidget)
        self.actionsPanel.setObjectName(u"actionsPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.actionsPanel.sizePolicy().hasHeightForWidth())
        self.actionsPanel.setSizePolicy(sizePolicy1)
        self.actionsPanel.setMinimumSize(QSize(300, 400))
        self.actionsPanel.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.actionsPanel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(135, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.saveActionButton = QPushButton(self.centralwidget)
        self.saveActionButton.setObjectName(u"saveActionButton")
        self.saveActionButton.setMaximumSize(QSize(80, 16777215))
        self.saveActionButton.setFont(font)

        self.horizontalLayout_5.addWidget(self.saveActionButton)

        self.horizontalSpacer_3 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.loadActionButton = QPushButton(self.centralwidget)
        self.loadActionButton.setObjectName(u"loadActionButton")
        self.loadActionButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.loadActionButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageSrcFolderLabel = QLabel(self.centralwidget)
        self.imageSrcFolderLabel.setObjectName(u"imageSrcFolderLabel")
        self.imageSrcFolderLabel.setMinimumSize(QSize(200, 25))
        self.imageSrcFolderLabel.setMaximumSize(QSize(200, 25))

        self.verticalLayout_2.addWidget(self.imageSrcFolderLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageSrcFolderReferenceButton = QPushButton(self.centralwidget)
        self.imageSrcFolderReferenceButton.setObjectName(u"imageSrcFolderReferenceButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imageSrcFolderReferenceButton.sizePolicy().hasHeightForWidth())
        self.imageSrcFolderReferenceButton.setSizePolicy(sizePolicy2)
        self.imageSrcFolderReferenceButton.setMinimumSize(QSize(80, 25))
        self.imageSrcFolderReferenceButton.setMaximumSize(QSize(80, 25))
        self.imageSrcFolderReferenceButton.setIconSize(QSize(16, 16))
        self.imageSrcFolderReferenceButton.setAutoDefault(False)
        self.imageSrcFolderReferenceButton.setFlat(False)

        self.horizontalLayout.addWidget(self.imageSrcFolderReferenceButton)

        self.imageSrcFolderPath = QLabel(self.centralwidget)
        self.imageSrcFolderPath.setObjectName(u"imageSrcFolderPath")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.imageSrcFolderPath.sizePolicy().hasHeightForWidth())
        self.imageSrcFolderPath.setSizePolicy(sizePolicy3)
        self.imageSrcFolderPath.setMinimumSize(QSize(0, 25))
        self.imageSrcFolderPath.setMaximumSize(QSize(16777215, 25))
        self.imageSrcFolderPath.setFrameShape(QFrame.StyledPanel)
        self.imageSrcFolderPath.setFrameShadow(QFrame.Plain)
        self.imageSrcFolderPath.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.imageSrcFolderPath)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.imageSaveFolderLabel = QLabel(self.centralwidget)
        self.imageSaveFolderLabel.setObjectName(u"imageSaveFolderLabel")
        self.imageSaveFolderLabel.setMinimumSize(QSize(200, 25))
        self.imageSaveFolderLabel.setMaximumSize(QSize(200, 25))

        self.verticalLayout_3.addWidget(self.imageSaveFolderLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageSaveFolderReferenceButton = QPushButton(self.centralwidget)
        self.imageSaveFolderReferenceButton.setObjectName(u"imageSaveFolderReferenceButton")
        sizePolicy2.setHeightForWidth(self.imageSaveFolderReferenceButton.sizePolicy().hasHeightForWidth())
        self.imageSaveFolderReferenceButton.setSizePolicy(sizePolicy2)
        self.imageSaveFolderReferenceButton.setMinimumSize(QSize(80, 25))
        self.imageSaveFolderReferenceButton.setMaximumSize(QSize(80, 25))
        self.imageSaveFolderReferenceButton.setIconSize(QSize(16, 16))
        self.imageSaveFolderReferenceButton.setAutoDefault(False)
        self.imageSaveFolderReferenceButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.imageSaveFolderReferenceButton)

        self.imageSaveFolderPath = QLabel(self.centralwidget)
        self.imageSaveFolderPath.setObjectName(u"imageSaveFolderPath")
        self.imageSaveFolderPath.setMinimumSize(QSize(250, 25))
        self.imageSaveFolderPath.setMaximumSize(QSize(16777215, 25))
        self.imageSaveFolderPath.setFrameShape(QFrame.StyledPanel)
        self.imageSaveFolderPath.setFrameShadow(QFrame.Plain)
        self.imageSaveFolderPath.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.imageSaveFolderPath)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.metashapeProjectFolderLabel = QLabel(self.centralwidget)
        self.metashapeProjectFolderLabel.setObjectName(u"metashapeProjectFolderLabel")
        self.metashapeProjectFolderLabel.setMinimumSize(QSize(200, 25))
        self.metashapeProjectFolderLabel.setMaximumSize(QSize(105, 25))

        self.verticalLayout_4.addWidget(self.metashapeProjectFolderLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.metashapeProjectFolderPathReferenceButton = QPushButton(self.centralwidget)
        self.metashapeProjectFolderPathReferenceButton.setObjectName(u"metashapeProjectFolderPathReferenceButton")
        sizePolicy2.setHeightForWidth(self.metashapeProjectFolderPathReferenceButton.sizePolicy().hasHeightForWidth())
        self.metashapeProjectFolderPathReferenceButton.setSizePolicy(sizePolicy2)
        self.metashapeProjectFolderPathReferenceButton.setMinimumSize(QSize(80, 25))
        self.metashapeProjectFolderPathReferenceButton.setMaximumSize(QSize(80, 25))
        self.metashapeProjectFolderPathReferenceButton.setIconSize(QSize(16, 16))
        self.metashapeProjectFolderPathReferenceButton.setAutoDefault(False)
        self.metashapeProjectFolderPathReferenceButton.setFlat(False)

        self.horizontalLayout_3.addWidget(self.metashapeProjectFolderPathReferenceButton)

        self.metashapeProjectFolderPath = QLabel(self.centralwidget)
        self.metashapeProjectFolderPath.setObjectName(u"metashapeProjectFolderPath")
        self.metashapeProjectFolderPath.setMinimumSize(QSize(250, 25))
        self.metashapeProjectFolderPath.setMaximumSize(QSize(16777215, 25))
        self.metashapeProjectFolderPath.setFrameShape(QFrame.StyledPanel)
        self.metashapeProjectFolderPath.setFrameShadow(QFrame.Plain)
        self.metashapeProjectFolderPath.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.metashapeProjectFolderPath)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.bracketsLabel = QLabel(self.centralwidget)
        self.bracketsLabel.setObjectName(u"bracketsLabel")
        self.bracketsLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.bracketsLabel)

        self.brackets = QSpinBox(self.centralwidget)
        self.brackets.setObjectName(u"brackets")
        self.brackets.setMinimum(1)

        self.verticalLayout_5.addWidget(self.brackets)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.doFocusStacking = QCheckBox(self.centralwidget)
        self.doFocusStacking.setObjectName(u"doFocusStacking")
        self.doFocusStacking.setChecked(True)

        self.verticalLayout_6.addWidget(self.doFocusStacking)

        self.doMetashape = QCheckBox(self.centralwidget)
        self.doMetashape.setObjectName(u"doMetashape")
        self.doMetashape.setChecked(True)

        self.verticalLayout_6.addWidget(self.doMetashape)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(80, 0))
        self.startButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.startButton)

        self.horizontalSpacer_4 = QSpacerItem(6, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(80, 0))
        self.stopButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.stopButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.imageSrcFolderReferenceButton.setDefault(False)
        self.imageSaveFolderReferenceButton.setDefault(False)
        self.metashapeProjectFolderPathReferenceButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionsPanelLabel.setText(QCoreApplication.translate("MainWindow", u"Actions Panel", None))
        self.actionsPanel.setPlainText("")
        self.saveActionButton.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.loadActionButton.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.imageSrcFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Image src folder", None))
        self.imageSrcFolderReferenceButton.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.imageSrcFolderPath.setText(QCoreApplication.translate("MainWindow", u"Not Selected.", None))
        self.imageSaveFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Image save folder", None))
        self.imageSaveFolderReferenceButton.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.imageSaveFolderPath.setText(QCoreApplication.translate("MainWindow", u"Not Selected.", None))
        self.metashapeProjectFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Metashape Project Folder", None))
        self.metashapeProjectFolderPathReferenceButton.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.metashapeProjectFolderPath.setText(QCoreApplication.translate("MainWindow", u"Not Selected.", None))
        self.bracketsLabel.setText(QCoreApplication.translate("MainWindow", u"Brackets", None))
        self.doFocusStacking.setText(QCoreApplication.translate("MainWindow", u"Focus Stacking", None))
        self.doMetashape.setText(QCoreApplication.translate("MainWindow", u"Metashape", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"stop", None))
    # retranslateUi

