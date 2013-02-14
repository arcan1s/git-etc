# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configwin.ui'
#
# Created: Thu Feb 14 03:39:31 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ConfigureWindow(object):
    def setupUi(self, ConfigureWindow):
        ConfigureWindow.setObjectName(_fromUtf8("ConfigureWindow"))
        ConfigureWindow.resize(391, 140)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigureWindow.sizePolicy().hasHeightForWidth())
        ConfigureWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(ConfigureWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_timeSleep = QtGui.QLabel(self.centralwidget)
        self.label_timeSleep.setGeometry(QtCore.QRect(10, 35, 181, 21))
        self.label_timeSleep.setObjectName(_fromUtf8("label_timeSleep"))
        self.lineEdit_timeSleep = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_timeSleep.setGeometry(QtCore.QRect(200, 35, 181, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_timeSleep.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeSleep.setSizePolicy(sizePolicy)
        self.lineEdit_timeSleep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_timeSleep.setObjectName(_fromUtf8("lineEdit_timeSleep"))
        self.button_refresh = QtGui.QPushButton(self.centralwidget)
        self.button_refresh.setGeometry(QtCore.QRect(175, 105, 101, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh.sizePolicy().hasHeightForWidth())
        self.button_refresh.setSizePolicy(sizePolicy)
        self.button_refresh.setDefault(True)
        self.button_refresh.setObjectName(_fromUtf8("button_refresh"))
        self.label_directory = QtGui.QLabel(self.centralwidget)
        self.label_directory.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.label_directory.setObjectName(_fromUtf8("label_directory"))
        self.lineEdit_ignoreList = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_ignoreList.setGeometry(QtCore.QRect(10, 80, 371, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ignoreList.sizePolicy().hasHeightForWidth())
        self.lineEdit_ignoreList.setSizePolicy(sizePolicy)
        self.lineEdit_ignoreList.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_ignoreList.setObjectName(_fromUtf8("lineEdit_ignoreList"))
        self.button_apply = QtGui.QPushButton(self.centralwidget)
        self.button_apply.setGeometry(QtCore.QRect(280, 105, 101, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_apply.sizePolicy().hasHeightForWidth())
        self.button_apply.setSizePolicy(sizePolicy)
        self.button_apply.setDefault(True)
        self.button_apply.setObjectName(_fromUtf8("button_apply"))
        self.label_ignoreList = QtGui.QLabel(self.centralwidget)
        self.label_ignoreList.setGeometry(QtCore.QRect(10, 60, 201, 21))
        self.label_ignoreList.setObjectName(_fromUtf8("label_ignoreList"))
        self.lineEdit_directory = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_directory.setGeometry(QtCore.QRect(170, 10, 211, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_directory.sizePolicy().hasHeightForWidth())
        self.lineEdit_directory.setSizePolicy(sizePolicy)
        self.lineEdit_directory.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_directory.setObjectName(_fromUtf8("lineEdit_directory"))
        self.button_close = QtGui.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(10, 105, 101, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setDefault(True)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        ConfigureWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConfigureWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfigureWindow)
        ConfigureWindow.setTabOrder(self.lineEdit_directory, self.lineEdit_timeSleep)
        ConfigureWindow.setTabOrder(self.lineEdit_timeSleep, self.lineEdit_ignoreList)
        ConfigureWindow.setTabOrder(self.lineEdit_ignoreList, self.button_refresh)
        ConfigureWindow.setTabOrder(self.button_refresh, self.button_apply)
        ConfigureWindow.setTabOrder(self.button_apply, self.button_close)

    def retranslateUi(self, ConfigureWindow):
        ConfigureWindow.setWindowTitle(_translate("ConfigureWindow", "Настроить сервис", None))
        self.label_timeSleep.setText(_translate("ConfigureWindow", "Интервал обновления, ч:", None))
        self.button_refresh.setText(_translate("ConfigureWindow", "Обновить", None))
        self.label_directory.setText(_translate("ConfigureWindow", "Рабочая директория:", None))
        self.button_apply.setText(_translate("ConfigureWindow", "Применить", None))
        self.label_ignoreList.setText(_translate("ConfigureWindow", "Список игнорируемых файлов:", None))
        self.button_close.setText(_translate("ConfigureWindow", "Закрыть", None))

