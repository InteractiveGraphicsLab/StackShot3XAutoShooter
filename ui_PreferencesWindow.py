# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreferencesWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_PreferencesWindow(object):
    def setupUi(self, PreferencesWindow):
        if not PreferencesWindow.objectName():
            PreferencesWindow.setObjectName(u"PreferencesWindow")
        PreferencesWindow.setEnabled(True)
        PreferencesWindow.resize(485, 400)
        self.horizontalLayout_3 = QHBoxLayout(PreferencesWindow)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(PreferencesWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.General = QWidget()
        self.General.setObjectName(u"General")
        self.formLayout_2 = QFormLayout(self.General)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.bracketsLabel = QLabel(self.General)
        self.bracketsLabel.setObjectName(u"bracketsLabel")
        self.bracketsLabel.setMinimumSize(QSize(105, 0))
        self.bracketsLabel.setMaximumSize(QSize(105, 16777215))
        self.bracketsLabel.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.bracketsLabel)

        self.bracketsSpinBox = QSpinBox(self.General)
        self.bracketsSpinBox.setObjectName(u"bracketsSpinBox")
        self.bracketsSpinBox.setMinimum(1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.bracketsSpinBox)

        self.imageSrcFolderLabel = QLabel(self.General)
        self.imageSrcFolderLabel.setObjectName(u"imageSrcFolderLabel")
        self.imageSrcFolderLabel.setMinimumSize(QSize(105, 25))
        self.imageSrcFolderLabel.setMaximumSize(QSize(105, 25))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.imageSrcFolderLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imageSrcFolderPath = QLabel(self.General)
        self.imageSrcFolderPath.setObjectName(u"imageSrcFolderPath")
        self.imageSrcFolderPath.setMinimumSize(QSize(0, 25))
        self.imageSrcFolderPath.setMaximumSize(QSize(16777215, 25))
        self.imageSrcFolderPath.setFrameShape(QFrame.StyledPanel)
        self.imageSrcFolderPath.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.imageSrcFolderPath)

        self.imageSrcFolderReferenceButton = QPushButton(self.General)
        self.imageSrcFolderReferenceButton.setObjectName(u"imageSrcFolderReferenceButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageSrcFolderReferenceButton.sizePolicy().hasHeightForWidth())
        self.imageSrcFolderReferenceButton.setSizePolicy(sizePolicy)
        self.imageSrcFolderReferenceButton.setMinimumSize(QSize(80, 25))
        self.imageSrcFolderReferenceButton.setMaximumSize(QSize(80, 25))
        self.imageSrcFolderReferenceButton.setIconSize(QSize(16, 16))
        self.imageSrcFolderReferenceButton.setAutoDefault(False)
        self.imageSrcFolderReferenceButton.setFlat(False)

        self.horizontalLayout.addWidget(self.imageSrcFolderReferenceButton)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.imageSaveFolderLabel = QLabel(self.General)
        self.imageSaveFolderLabel.setObjectName(u"imageSaveFolderLabel")
        self.imageSaveFolderLabel.setMinimumSize(QSize(105, 25))
        self.imageSaveFolderLabel.setMaximumSize(QSize(105, 25))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.imageSaveFolderLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageSaveFolderPath = QLabel(self.General)
        self.imageSaveFolderPath.setObjectName(u"imageSaveFolderPath")
        self.imageSaveFolderPath.setMinimumSize(QSize(0, 25))
        self.imageSaveFolderPath.setMaximumSize(QSize(16777215, 25))
        self.imageSaveFolderPath.setFrameShape(QFrame.StyledPanel)
        self.imageSaveFolderPath.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.imageSaveFolderPath)

        self.imageSaveFolderReferenceButton = QPushButton(self.General)
        self.imageSaveFolderReferenceButton.setObjectName(u"imageSaveFolderReferenceButton")
        sizePolicy.setHeightForWidth(self.imageSaveFolderReferenceButton.sizePolicy().hasHeightForWidth())
        self.imageSaveFolderReferenceButton.setSizePolicy(sizePolicy)
        self.imageSaveFolderReferenceButton.setMinimumSize(QSize(80, 25))
        self.imageSaveFolderReferenceButton.setMaximumSize(QSize(80, 25))
        self.imageSaveFolderReferenceButton.setIconSize(QSize(16, 16))
        self.imageSaveFolderReferenceButton.setAutoDefault(False)
        self.imageSaveFolderReferenceButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.imageSaveFolderReferenceButton)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.tabWidget.addTab(self.General, "")
        self.FocusStacking = QWidget()
        self.FocusStacking.setObjectName(u"FocusStacking")
        self.tabWidget.addTab(self.FocusStacking, "")
        self.Metashape = QWidget()
        self.Metashape.setObjectName(u"Metashape")
        self.tabWidget.addTab(self.Metashape, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(PreferencesWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(PreferencesWindow)

        self.tabWidget.setCurrentIndex(0)
        self.imageSrcFolderReferenceButton.setDefault(False)
        self.imageSaveFolderReferenceButton.setDefault(False)


        QMetaObject.connectSlotsByName(PreferencesWindow)
    # setupUi

    def retranslateUi(self, PreferencesWindow):
        PreferencesWindow.setWindowTitle(QCoreApplication.translate("PreferencesWindow", u"Preferences", None))
        self.bracketsLabel.setText(QCoreApplication.translate("PreferencesWindow", u"Brackets", None))
        self.imageSrcFolderLabel.setText(QCoreApplication.translate("PreferencesWindow", u"Image src folder", None))
        self.imageSrcFolderPath.setText(QCoreApplication.translate("PreferencesWindow", u"Not Selected.", None))
        self.imageSrcFolderReferenceButton.setText(QCoreApplication.translate("PreferencesWindow", u"Reference", None))
        self.imageSaveFolderLabel.setText(QCoreApplication.translate("PreferencesWindow", u"Image save folder", None))
        self.imageSaveFolderPath.setText(QCoreApplication.translate("PreferencesWindow", u"Not Selected.", None))
        self.imageSaveFolderReferenceButton.setText(QCoreApplication.translate("PreferencesWindow", u"Reference", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.General), QCoreApplication.translate("PreferencesWindow", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FocusStacking), QCoreApplication.translate("PreferencesWindow", u"FocusStacking", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Metashape), QCoreApplication.translate("PreferencesWindow", u"Metashape", None))
    # retranslateUi

