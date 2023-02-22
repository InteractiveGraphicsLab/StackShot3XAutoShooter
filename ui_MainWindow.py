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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 555)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(11)
        self.tabWidget.setFont(font1)
        self.Action = QWidget()
        self.Action.setObjectName(u"Action")
        self.verticalLayout_8 = QVBoxLayout(self.Action)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.actionsPanelLayout = QVBoxLayout()
        self.actionsPanelLayout.setObjectName(u"actionsPanelLayout")
        self.actionsPanelLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.actionsPanelLayout.setContentsMargins(-1, -1, 0, -1)
        self.actionsLabel = QLabel(self.Action)
        self.actionsLabel.setObjectName(u"actionsLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionsLabel.sizePolicy().hasHeightForWidth())
        self.actionsLabel.setSizePolicy(sizePolicy)
        self.actionsLabel.setFont(font1)

        self.actionsPanelLayout.addWidget(self.actionsLabel)

        self.actionsText = QPlainTextEdit(self.Action)
        self.actionsText.setObjectName(u"actionsText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.actionsText.sizePolicy().hasHeightForWidth())
        self.actionsText.setSizePolicy(sizePolicy1)
        self.actionsText.setMinimumSize(QSize(300, 400))
        self.actionsText.setMaximumSize(QSize(300, 16777215))

        self.actionsPanelLayout.addWidget(self.actionsText)


        self.horizontalLayout_11.addLayout(self.actionsPanelLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.imageSrcFolderLayout = QVBoxLayout()
        self.imageSrcFolderLayout.setSpacing(0)
        self.imageSrcFolderLayout.setObjectName(u"imageSrcFolderLayout")
        self.imageSrcFolderLayout.setContentsMargins(-1, -1, -1, 10)
        self.imageSrcFolderLabel = QLabel(self.Action)
        self.imageSrcFolderLabel.setObjectName(u"imageSrcFolderLabel")
        self.imageSrcFolderLabel.setMinimumSize(QSize(200, 25))
        self.imageSrcFolderLabel.setMaximumSize(QSize(200, 25))

        self.imageSrcFolderLayout.addWidget(self.imageSrcFolderLabel)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.imageSrcFolderReferenceButton = QPushButton(self.Action)
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

        self.horizontalLayout_10.addWidget(self.imageSrcFolderReferenceButton)

        self.imageSrcFolderPath = QLabel(self.Action)
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

        self.horizontalLayout_10.addWidget(self.imageSrcFolderPath)


        self.imageSrcFolderLayout.addLayout(self.horizontalLayout_10)


        self.verticalLayout_6.addLayout(self.imageSrcFolderLayout)

        self.imageSaveFolderLayout = QVBoxLayout()
        self.imageSaveFolderLayout.setSpacing(0)
        self.imageSaveFolderLayout.setObjectName(u"imageSaveFolderLayout")
        self.imageSaveFolderLayout.setContentsMargins(-1, -1, -1, 10)
        self.imageSaveFolderLabel = QLabel(self.Action)
        self.imageSaveFolderLabel.setObjectName(u"imageSaveFolderLabel")
        self.imageSaveFolderLabel.setMinimumSize(QSize(200, 25))
        self.imageSaveFolderLabel.setMaximumSize(QSize(200, 25))

        self.imageSaveFolderLayout.addWidget(self.imageSaveFolderLabel)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.imageSaveFolderReferenceButton = QPushButton(self.Action)
        self.imageSaveFolderReferenceButton.setObjectName(u"imageSaveFolderReferenceButton")
        sizePolicy2.setHeightForWidth(self.imageSaveFolderReferenceButton.sizePolicy().hasHeightForWidth())
        self.imageSaveFolderReferenceButton.setSizePolicy(sizePolicy2)
        self.imageSaveFolderReferenceButton.setMinimumSize(QSize(80, 25))
        self.imageSaveFolderReferenceButton.setMaximumSize(QSize(80, 25))
        self.imageSaveFolderReferenceButton.setIconSize(QSize(16, 16))
        self.imageSaveFolderReferenceButton.setAutoDefault(False)
        self.imageSaveFolderReferenceButton.setFlat(False)

        self.horizontalLayout_8.addWidget(self.imageSaveFolderReferenceButton)

        self.imageSaveFolderPath = QLabel(self.Action)
        self.imageSaveFolderPath.setObjectName(u"imageSaveFolderPath")
        self.imageSaveFolderPath.setMinimumSize(QSize(250, 25))
        self.imageSaveFolderPath.setMaximumSize(QSize(16777215, 25))
        self.imageSaveFolderPath.setFrameShape(QFrame.StyledPanel)
        self.imageSaveFolderPath.setFrameShadow(QFrame.Plain)
        self.imageSaveFolderPath.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_8.addWidget(self.imageSaveFolderPath)


        self.imageSaveFolderLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addLayout(self.imageSaveFolderLayout)

        self.metashapeProjectFolderLayout = QVBoxLayout()
        self.metashapeProjectFolderLayout.setSpacing(0)
        self.metashapeProjectFolderLayout.setObjectName(u"metashapeProjectFolderLayout")
        self.metashapeProjectFolderLayout.setContentsMargins(-1, -1, -1, 10)
        self.metashapeProjectFolderLabel = QLabel(self.Action)
        self.metashapeProjectFolderLabel.setObjectName(u"metashapeProjectFolderLabel")
        self.metashapeProjectFolderLabel.setMinimumSize(QSize(200, 25))
        self.metashapeProjectFolderLabel.setMaximumSize(QSize(105, 25))

        self.metashapeProjectFolderLayout.addWidget(self.metashapeProjectFolderLabel)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.metashapeProjectFolderPathReferenceButton = QPushButton(self.Action)
        self.metashapeProjectFolderPathReferenceButton.setObjectName(u"metashapeProjectFolderPathReferenceButton")
        sizePolicy2.setHeightForWidth(self.metashapeProjectFolderPathReferenceButton.sizePolicy().hasHeightForWidth())
        self.metashapeProjectFolderPathReferenceButton.setSizePolicy(sizePolicy2)
        self.metashapeProjectFolderPathReferenceButton.setMinimumSize(QSize(80, 25))
        self.metashapeProjectFolderPathReferenceButton.setMaximumSize(QSize(80, 25))
        self.metashapeProjectFolderPathReferenceButton.setIconSize(QSize(16, 16))
        self.metashapeProjectFolderPathReferenceButton.setAutoDefault(False)
        self.metashapeProjectFolderPathReferenceButton.setFlat(False)

        self.horizontalLayout_9.addWidget(self.metashapeProjectFolderPathReferenceButton)

        self.metashapeProjectFolderPath = QLabel(self.Action)
        self.metashapeProjectFolderPath.setObjectName(u"metashapeProjectFolderPath")
        self.metashapeProjectFolderPath.setMinimumSize(QSize(250, 25))
        self.metashapeProjectFolderPath.setMaximumSize(QSize(16777215, 25))
        self.metashapeProjectFolderPath.setFrameShape(QFrame.StyledPanel)
        self.metashapeProjectFolderPath.setFrameShadow(QFrame.Plain)
        self.metashapeProjectFolderPath.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_9.addWidget(self.metashapeProjectFolderPath)


        self.metashapeProjectFolderLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addLayout(self.metashapeProjectFolderLayout)

        self.bracketsLayout = QVBoxLayout()
        self.bracketsLayout.setSpacing(0)
        self.bracketsLayout.setObjectName(u"bracketsLayout")
        self.bracketsLayout.setContentsMargins(-1, -1, -1, 10)
        self.bracketsLabel = QLabel(self.Action)
        self.bracketsLabel.setObjectName(u"bracketsLabel")
        self.bracketsLabel.setFont(font1)

        self.bracketsLayout.addWidget(self.bracketsLabel)

        self.brackets = QSpinBox(self.Action)
        self.brackets.setObjectName(u"brackets")
        self.brackets.setMinimum(1)

        self.bracketsLayout.addWidget(self.brackets)


        self.verticalLayout_6.addLayout(self.bracketsLayout)

        self.doFocusStacking = QCheckBox(self.Action)
        self.doFocusStacking.setObjectName(u"doFocusStacking")
        self.doFocusStacking.setChecked(True)

        self.verticalLayout_6.addWidget(self.doFocusStacking)

        self.doMetashape = QCheckBox(self.Action)
        self.doMetashape.setObjectName(u"doMetashape")
        self.doMetashape.setChecked(True)

        self.verticalLayout_6.addWidget(self.doMetashape)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.startButton = QPushButton(self.Action)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(80, 0))
        self.startButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.startButton)

        self.stopButton = QPushButton(self.Action)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(80, 0))
        self.stopButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.stopButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.Action, "")
        self.Configuration = QWidget()
        self.Configuration.setObjectName(u"Configuration")
        self.formLayout = QFormLayout(self.Configuration)
        self.formLayout.setObjectName(u"formLayout")
        self.heliconfocusCommandPathLabel = QLabel(self.Configuration)
        self.heliconfocusCommandPathLabel.setObjectName(u"heliconfocusCommandPathLabel")
        self.heliconfocusCommandPathLabel.setMinimumSize(QSize(200, 25))
        self.heliconfocusCommandPathLabel.setMaximumSize(QSize(105, 25))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.heliconfocusCommandPathLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.heliconFocusCommandPathReferenceButton = QPushButton(self.Configuration)
        self.heliconFocusCommandPathReferenceButton.setObjectName(u"heliconFocusCommandPathReferenceButton")
        sizePolicy2.setHeightForWidth(self.heliconFocusCommandPathReferenceButton.sizePolicy().hasHeightForWidth())
        self.heliconFocusCommandPathReferenceButton.setSizePolicy(sizePolicy2)
        self.heliconFocusCommandPathReferenceButton.setMinimumSize(QSize(80, 25))
        self.heliconFocusCommandPathReferenceButton.setMaximumSize(QSize(80, 25))
        self.heliconFocusCommandPathReferenceButton.setIconSize(QSize(16, 16))
        self.heliconFocusCommandPathReferenceButton.setAutoDefault(False)
        self.heliconFocusCommandPathReferenceButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.heliconFocusCommandPathReferenceButton)

        self.heliconfocusCommandPath = QLabel(self.Configuration)
        self.heliconfocusCommandPath.setObjectName(u"heliconfocusCommandPath")
        self.heliconfocusCommandPath.setMinimumSize(QSize(0, 25))
        self.heliconfocusCommandPath.setMaximumSize(QSize(16777215, 25))
        self.heliconfocusCommandPath.setFrameShape(QFrame.StyledPanel)
        self.heliconfocusCommandPath.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.heliconfocusCommandPath)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.metashapeCommandPathLabel = QLabel(self.Configuration)
        self.metashapeCommandPathLabel.setObjectName(u"metashapeCommandPathLabel")
        self.metashapeCommandPathLabel.setMinimumSize(QSize(200, 25))
        self.metashapeCommandPathLabel.setMaximumSize(QSize(105, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.metashapeCommandPathLabel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.metashapeCommandPathReferenceButton = QPushButton(self.Configuration)
        self.metashapeCommandPathReferenceButton.setObjectName(u"metashapeCommandPathReferenceButton")
        sizePolicy2.setHeightForWidth(self.metashapeCommandPathReferenceButton.sizePolicy().hasHeightForWidth())
        self.metashapeCommandPathReferenceButton.setSizePolicy(sizePolicy2)
        self.metashapeCommandPathReferenceButton.setMinimumSize(QSize(80, 25))
        self.metashapeCommandPathReferenceButton.setMaximumSize(QSize(80, 25))
        self.metashapeCommandPathReferenceButton.setIconSize(QSize(16, 16))
        self.metashapeCommandPathReferenceButton.setAutoDefault(False)
        self.metashapeCommandPathReferenceButton.setFlat(False)

        self.horizontalLayout_6.addWidget(self.metashapeCommandPathReferenceButton)

        self.metashapeCommandPath = QLabel(self.Configuration)
        self.metashapeCommandPath.setObjectName(u"metashapeCommandPath")
        self.metashapeCommandPath.setMinimumSize(QSize(0, 25))
        self.metashapeCommandPath.setMaximumSize(QSize(16777215, 25))
        self.metashapeCommandPath.setFrameShape(QFrame.StyledPanel)
        self.metashapeCommandPath.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_6.addWidget(self.metashapeCommandPath)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.tabWidget.addTab(self.Configuration, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.imageSrcFolderReferenceButton.setDefault(False)
        self.imageSaveFolderReferenceButton.setDefault(False)
        self.metashapeProjectFolderPathReferenceButton.setDefault(False)
        self.heliconFocusCommandPathReferenceButton.setDefault(False)
        self.metashapeCommandPathReferenceButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionsLabel.setText(QCoreApplication.translate("MainWindow", u"Actions Panel", None))
        self.actionsText.setPlainText("")
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Action), QCoreApplication.translate("MainWindow", u"Action", None))
        self.heliconfocusCommandPathLabel.setText(QCoreApplication.translate("MainWindow", u"HeliconFocus Command PATH", None))
        self.heliconFocusCommandPathReferenceButton.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.heliconfocusCommandPath.setText(QCoreApplication.translate("MainWindow", u"Not Selected.", None))
        self.metashapeCommandPathLabel.setText(QCoreApplication.translate("MainWindow", u"Metashape Command PATH", None))
        self.metashapeCommandPathReferenceButton.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.metashapeCommandPath.setText(QCoreApplication.translate("MainWindow", u"Not Selected.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configuration), QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

