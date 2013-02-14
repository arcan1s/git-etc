# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commitwin.ui'
#
# Created: Thu Feb 14 20:23:43 2013
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

class Ui_CommitWindow(object):
    def setupUi(self, CommitWindow):
        CommitWindow.setObjectName(_fromUtf8("CommitWindow"))
        CommitWindow.resize(662, 358)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CommitWindow.sizePolicy().hasHeightForWidth())
        CommitWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(CommitWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_commit_name = QtGui.QLabel(self.centralwidget)
        self.label_commit_name.setGeometry(QtCore.QRect(10, 10, 81, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_commit_name.sizePolicy().hasHeightForWidth())
        self.label_commit_name.setSizePolicy(sizePolicy)
        self.label_commit_name.setObjectName(_fromUtf8("label_commit_name"))
        self.label_commit = QtGui.QLabel(self.centralwidget)
        self.label_commit.setGeometry(QtCore.QRect(130, 10, 521, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_commit.sizePolicy().hasHeightForWidth())
        self.label_commit.setSizePolicy(sizePolicy)
        self.label_commit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_commit.setObjectName(_fromUtf8("label_commit"))
        self.label_date = QtGui.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(130, 30, 521, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.label_date_name = QtGui.QLabel(self.centralwidget)
        self.label_date_name.setGeometry(QtCore.QRect(10, 30, 81, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_name.sizePolicy().hasHeightForWidth())
        self.label_date_name.setSizePolicy(sizePolicy)
        self.label_date_name.setObjectName(_fromUtf8("label_date_name"))
        self.box_file = QtGui.QComboBox(self.centralwidget)
        self.box_file.setGeometry(QtCore.QRect(130, 60, 521, 24))
        self.box_file.setObjectName(_fromUtf8("box_file"))
        self.label_file_name = QtGui.QLabel(self.centralwidget)
        self.label_file_name.setGeometry(QtCore.QRect(10, 60, 81, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_file_name.sizePolicy().hasHeightForWidth())
        self.label_file_name.setSizePolicy(sizePolicy)
        self.label_file_name.setObjectName(_fromUtf8("label_file_name"))
        self.text_filediff = QtGui.QTextBrowser(self.centralwidget)
        self.text_filediff.setGeometry(QtCore.QRect(10, 90, 641, 231))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filediff.sizePolicy().hasHeightForWidth())
        self.text_filediff.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.text_filediff.setFont(font)
        self.text_filediff.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.text_filediff.setObjectName(_fromUtf8("text_filediff"))
        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(10, 325, 151, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_open.sizePolicy().hasHeightForWidth())
        self.button_open.setSizePolicy(sizePolicy)
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.button_close = QtGui.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(550, 325, 101, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        CommitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CommitWindow)
        QtCore.QMetaObject.connectSlotsByName(CommitWindow)

    def retranslateUi(self, CommitWindow):
        CommitWindow.setWindowTitle(_translate("CommitWindow", "Commit: ", None))
        self.label_commit_name.setText(_translate("CommitWindow", "Commit:", None))
        self.label_commit.setText(_translate("CommitWindow", "(unknown)", None))
        self.label_date.setText(_translate("CommitWindow", "(unknown)", None))
        self.label_date_name.setText(_translate("CommitWindow", "Date:", None))
        self.label_file_name.setText(_translate("CommitWindow", "File:", None))
        self.text_filediff.setHtml(_translate("CommitWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_open.setText(_translate("CommitWindow", "Открыть в редакторе", None))
        self.button_close.setText(_translate("CommitWindow", "Закрыть", None))

