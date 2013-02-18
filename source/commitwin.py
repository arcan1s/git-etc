# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commitwin.ui'
#
# Created: Mon Feb 18 02:18:51 2013
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
        AboutWindow.resize(418, 298)
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
        self.text_about.setMinimumSize(QtCore.QSize(410, 260))
        self.text_about.setObjectName(_fromUtf8("text_about"))
        self.gridLayout.addWidget(self.text_about, 0, 0, 1, 3)
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)
        AboutWindow.setTabOrder(self.text_about, self.button_close)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About", None))
        self.button_close.setText(_translate("AboutWindow", "Закрыть", None))
        self.text_about.setHtml(_translate("AboutWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">git2etc 2.0.0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Лицензия: GPL</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GUI интерфейс к демону git-etc, написанный на python2.7/PyQt4. Позволяет посмотреть список коммитов и изменения в файлах, записанные в коммитах. Также данное приложение позволяет откатить к определенному коммиту все файлы (git reset --hard) или отдельно взятые (git diff &amp;&amp; git apply). Дополнительно предусмотрена возможность слияния старых и новых конфигурационных файлов (используются две ветки репозитория - master и experimental).</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор: Евгений Алексеев aka arcanis</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: esalexeev@gmail.com</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jabber: arcanis@jabber.ru</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ICQ: 407-398-235</p></body></html>", None))


class Ui_CommitWindow(object):
    def setupUi(self, CommitWindow):
        CommitWindow.setObjectName(_fromUtf8("CommitWindow"))
        CommitWindow.resize(662, 316)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CommitWindow.sizePolicy().hasHeightForWidth())
        CommitWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(CommitWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_date_name = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_name.sizePolicy().hasHeightForWidth())
        self.label_date_name.setSizePolicy(sizePolicy)
        self.label_date_name.setMinimumSize(QtCore.QSize(150, 20))
        self.label_date_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_date_name.setObjectName(_fromUtf8("label_date_name"))
        self.gridLayout.addWidget(self.label_date_name, 1, 0, 1, 1)
        self.button_close = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setMinimumSize(QtCore.QSize(100, 20))
        self.button_close.setMaximumSize(QtCore.QSize(100, 25))
        self.button_close.setDefault(True)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.gridLayout.addWidget(self.button_close, 5, 2, 1, 1)
        self.text_filediff = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_filediff.sizePolicy().hasHeightForWidth())
        self.text_filediff.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.text_filediff.setFont(font)
        self.text_filediff.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.text_filediff.setObjectName(_fromUtf8("text_filediff"))
        self.gridLayout.addWidget(self.text_filediff, 4, 0, 1, 3)
        self.label_commit_name = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_commit_name.sizePolicy().hasHeightForWidth())
        self.label_commit_name.setSizePolicy(sizePolicy)
        self.label_commit_name.setMinimumSize(QtCore.QSize(150, 20))
        self.label_commit_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_commit_name.setObjectName(_fromUtf8("label_commit_name"))
        self.gridLayout.addWidget(self.label_commit_name, 0, 0, 1, 1)
        self.label_commit = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_commit.sizePolicy().hasHeightForWidth())
        self.label_commit.setSizePolicy(sizePolicy)
        self.label_commit.setMinimumSize(QtCore.QSize(250, 20))
        self.label_commit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_commit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_commit.setObjectName(_fromUtf8("label_commit"))
        self.gridLayout.addWidget(self.label_commit, 0, 1, 1, 2)
        self.label_date = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setMinimumSize(QtCore.QSize(250, 20))
        self.label_date.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.gridLayout.addWidget(self.label_date, 1, 1, 1, 2)
        self.box_file = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_file.sizePolicy().hasHeightForWidth())
        self.box_file.setSizePolicy(sizePolicy)
        self.box_file.setMinimumSize(QtCore.QSize(250, 20))
        self.box_file.setMaximumSize(QtCore.QSize(16777215, 25))
        self.box_file.setObjectName(_fromUtf8("box_file"))
        self.gridLayout.addWidget(self.box_file, 3, 1, 1, 2)
        self.label_file_name = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_file_name.sizePolicy().hasHeightForWidth())
        self.label_file_name.setSizePolicy(sizePolicy)
        self.label_file_name.setMinimumSize(QtCore.QSize(150, 20))
        self.label_file_name.setMaximumSize(QtCore.QSize(150, 25))
        self.label_file_name.setObjectName(_fromUtf8("label_file_name"))
        self.gridLayout.addWidget(self.label_file_name, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)
        self.button_open = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_open.sizePolicy().hasHeightForWidth())
        self.button_open.setSizePolicy(sizePolicy)
        self.button_open.setMinimumSize(QtCore.QSize(150, 20))
        self.button_open.setMaximumSize(QtCore.QSize(150, 25))
        self.button_open.setDefault(True)
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.gridLayout.addWidget(self.button_open, 5, 0, 1, 2)
        CommitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CommitWindow)
        QtCore.QMetaObject.connectSlotsByName(CommitWindow)
        CommitWindow.setTabOrder(self.box_file, self.text_filediff)
        CommitWindow.setTabOrder(self.text_filediff, self.button_open)
        CommitWindow.setTabOrder(self.button_open, self.button_close)

    def retranslateUi(self, CommitWindow):
        CommitWindow.setWindowTitle(_translate("CommitWindow", "Commit: ", None))
        self.label_date_name.setText(_translate("CommitWindow", "Date:", None))
        self.button_close.setText(_translate("CommitWindow", "Закрыть", None))
        self.text_filediff.setHtml(_translate("CommitWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_commit_name.setText(_translate("CommitWindow", "Commit:", None))
        self.label_commit.setText(_translate("CommitWindow", "(unknown)", None))
        self.label_date.setText(_translate("CommitWindow", "(unknown)", None))
        self.label_file_name.setText(_translate("CommitWindow", "File:", None))
        self.button_open.setText(_translate("CommitWindow", "Открыть в редакторе", None))

