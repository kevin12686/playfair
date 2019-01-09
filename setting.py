# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Setting_Dialog(object):
    def setupUi(self, Setting_Dialog):
        Setting_Dialog.setObjectName("Setting_Dialog")
        Setting_Dialog.setWindowModality(QtCore.Qt.NonModal)
        Setting_Dialog.setEnabled(True)
        Setting_Dialog.resize(310, 135)
        Setting_Dialog.setMinimumSize(QtCore.QSize(310, 135))
        Setting_Dialog.setMaximumSize(QtCore.QSize(310, 135))
        Setting_Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Setting_Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verticalLayoutWidget = QtWidgets.QWidget(Setting_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(6, 1, 294, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.plainTextEdit_letter = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_letter.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.plainTextEdit_letter.setFont(font)
        self.plainTextEdit_letter.setObjectName("plainTextEdit_letter")
        self.horizontalLayout.addWidget(self.plainTextEdit_letter, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_setting_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.pushButton_setting_ok.setFont(font)
        self.pushButton_setting_ok.setObjectName("pushButton_setting_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_setting_ok)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(Setting_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Setting_Dialog)

    def retranslateUi(self, Setting_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Setting_Dialog.setWindowTitle(_translate("Setting_Dialog", "Setting"))
        self.label.setText(_translate("Setting_Dialog", "Fake Letter"))
        self.pushButton_setting_ok.setText(_translate("Setting_Dialog", "OK"))

