# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutwin.ui'
#
# Created: Mon Feb 18 02:20:08 2013
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

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName(_fromUtf8("AboutWindow"))
        AboutWindow.resize(321, 243)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutWindow.sizePolicy().hasHeightForWidth())
        AboutWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(AboutWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_close = QtGui.QPushButton(self.centralwidget)
        self.button_close.setMinimumSize(QtCore.QSize(100, 20))
        self.button_close.setMaximumSize(QtCore.QSize(100, 25))
        self.button_close.setDefault(True)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.gridLayout.addWidget(self.button_close, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.text_about = QtGui.QTextBrowser(self.centralwidget)
        self.text_about.setObjectName(_fromUtf8("text_about"))
        self.gridLayout.addWidget(self.text_about, 0, 0, 1, 3)
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)
        AboutWindow.setTabOrder(self.text_about, self.button_close)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About", None))
        self.button_close.setText(_translate("AboutWindow", "Закрыть", None))

