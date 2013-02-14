# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingswin.ui'
#
# Created: Fri Feb 15 03:42:20 2013
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

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName(_fromUtf8("SettingsWindow"))
        SettingsWindow.resize(391, 152)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(SettingsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_service = QtGui.QLabel(self.centralwidget)
        self.label_service.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.label_service.setObjectName(_fromUtf8("label_service"))
        self.label_config = QtGui.QLabel(self.centralwidget)
        self.label_config.setGeometry(QtCore.QRect(10, 65, 121, 21))
        self.label_config.setObjectName(_fromUtf8("label_config"))
        self.button_apply = QtGui.QPushButton(self.centralwidget)
        self.button_apply.setGeometry(QtCore.QRect(190, 120, 91, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_apply.sizePolicy().hasHeightForWidth())
        self.button_apply.setSizePolicy(sizePolicy)
        self.button_apply.setDefault(True)
        self.button_apply.setObjectName(_fromUtf8("button_apply"))
        self.label_lang = QtGui.QLabel(self.centralwidget)
        self.label_lang.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.label_lang.setObjectName(_fromUtf8("label_lang"))
        self.lineEdit_editor = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_editor.setGeometry(QtCore.QRect(160, 90, 221, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_editor.sizePolicy().hasHeightForWidth())
        self.lineEdit_editor.setSizePolicy(sizePolicy)
        self.lineEdit_editor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_editor.setObjectName(_fromUtf8("lineEdit_editor"))
        self.label_editor = QtGui.QLabel(self.centralwidget)
        self.label_editor.setGeometry(QtCore.QRect(10, 90, 141, 21))
        self.label_editor.setObjectName(_fromUtf8("label_editor"))
        self.button_default = QtGui.QPushButton(self.centralwidget)
        self.button_default.setGeometry(QtCore.QRect(10, 120, 111, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_default.sizePolicy().hasHeightForWidth())
        self.button_default.setSizePolicy(sizePolicy)
        self.button_default.setDefault(True)
        self.button_default.setObjectName(_fromUtf8("button_default"))
        self.box_lang = QtGui.QComboBox(self.centralwidget)
        self.box_lang.setGeometry(QtCore.QRect(170, 10, 211, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_lang.sizePolicy().hasHeightForWidth())
        self.box_lang.setSizePolicy(sizePolicy)
        self.box_lang.setObjectName(_fromUtf8("box_lang"))
        self.box_lang.addItem(_fromUtf8(""))
        self.box_lang.addItem(_fromUtf8(""))
        self.lineEdit_config = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_config.setGeometry(QtCore.QRect(140, 65, 241, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config.sizePolicy().hasHeightForWidth())
        self.lineEdit_config.setSizePolicy(sizePolicy)
        self.lineEdit_config.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_config.setObjectName(_fromUtf8("lineEdit_config"))
        self.button_close = QtGui.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(290, 120, 91, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setDefault(True)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.lineEdit_service = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_service.setGeometry(QtCore.QRect(140, 40, 241, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_service.sizePolicy().hasHeightForWidth())
        self.lineEdit_service.setSizePolicy(sizePolicy)
        self.lineEdit_service.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_service.setObjectName(_fromUtf8("lineEdit_service"))
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)
        SettingsWindow.setTabOrder(self.box_lang, self.lineEdit_service)
        SettingsWindow.setTabOrder(self.lineEdit_service, self.lineEdit_config)
        SettingsWindow.setTabOrder(self.lineEdit_config, self.lineEdit_editor)
        SettingsWindow.setTabOrder(self.lineEdit_editor, self.button_default)
        SettingsWindow.setTabOrder(self.button_default, self.button_apply)
        SettingsWindow.setTabOrder(self.button_apply, self.button_close)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Настройки", None))
        self.label_service.setText(_translate("SettingsWindow", "Service", None))
        self.label_config.setText(_translate("SettingsWindow", "Настройки git-etc", None))
        self.button_apply.setText(_translate("SettingsWindow", "Применить", None))
        self.label_lang.setText(_translate("SettingsWindow", "Язык", None))
        self.label_editor.setText(_translate("SettingsWindow", "Текстовый редактор", None))
        self.button_default.setText(_translate("SettingsWindow", "По умолчанию", None))
        self.box_lang.setItemText(0, _translate("SettingsWindow", "English", None))
        self.box_lang.setItemText(1, _translate("SettingsWindow", "Русский", None))
        self.button_close.setText(_translate("SettingsWindow", "Закрыть", None))

