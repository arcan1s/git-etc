# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notfound.ui'
#
# Created: Wed Sep 18 16:52:11 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_NotFound(object):
    def setupUi(self, NotFound):
        NotFound.setObjectName(_fromUtf8("NotFound"))
        NotFound.resize(320, 89)
        NotFound.setMinimumSize(QtCore.QSize(320, 89))
        self.centralwidget = QtGui.QWidget(NotFound)
        self.centralwidget.setMinimumSize(QtCore.QSize(320, 89))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_textError = QtGui.QLabel(self.centralwidget)
        self.label_textError.setMinimumSize(QtCore.QSize(0, 50))
        self.label_textError.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_textError.setAlignment(QtCore.Qt.AlignCenter)
        self.label_textError.setObjectName(_fromUtf8("label_textError"))
        self.gridLayout.addWidget(self.label_textError, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_ok = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ok.sizePolicy().hasHeightForWidth())
        self.button_ok.setSizePolicy(sizePolicy)
        self.button_ok.setMinimumSize(QtCore.QSize(100, 25))
        self.button_ok.setMaximumSize(QtCore.QSize(100, 25))
        self.button_ok.setDefault(True)
        self.button_ok.setObjectName(_fromUtf8("button_ok"))
        self.horizontalLayout.addWidget(self.button_ok)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        NotFound.setCentralWidget(self.centralwidget)

        self.retranslateUi(NotFound)
        QtCore.QObject.connect(self.button_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), NotFound.close)
        QtCore.QMetaObject.connectSlotsByName(NotFound)

    def retranslateUi(self, NotFound):
        NotFound.setWindowTitle(_translate("NotFound", "Ошибка!", None))
        self.label_textError.setText(_translate("NotFound", "<html><head/><body><p align=\"justify\">null</p></body></html>", None))
        self.button_ok.setText(_translate("NotFound", "Ok", None))

