#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Do not touch!
# Magick!

 
import argparse, commands, datetime, os, sys
from PyQt4 import QtCore, QtGui

#from aboutwin import Ui_AboutWindow
#from commitwin import Ui_CommitWindow
#from configwin import Ui_ConfigureWindow
#from gitwin import Ui_GitWindow
#from settingswin import Ui_SettingsWindow
#from mainwin import Ui_MainWindow


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


class Ui_ConfigureWindow(object):
    def setupUi(self, ConfigureWindow):
        ConfigureWindow.setObjectName(_fromUtf8("ConfigureWindow"))
        ConfigureWindow.resize(430, 149)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigureWindow.sizePolicy().hasHeightForWidth())
        ConfigureWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(ConfigureWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 150))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_directory = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_directory.sizePolicy().hasHeightForWidth())
        self.label_directory.setSizePolicy(sizePolicy)
        self.label_directory.setMinimumSize(QtCore.QSize(150, 25))
        self.label_directory.setMaximumSize(QtCore.QSize(150, 25))
        self.label_directory.setObjectName(_fromUtf8("label_directory"))
        self.gridLayout.addWidget(self.label_directory, 0, 0, 1, 1)
        self.button_refresh = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh.sizePolicy().hasHeightForWidth())
        self.button_refresh.setSizePolicy(sizePolicy)
        self.button_refresh.setMinimumSize(QtCore.QSize(100, 25))
        self.button_refresh.setMaximumSize(QtCore.QSize(100, 25))
        self.button_refresh.setDefault(True)
        self.button_refresh.setObjectName(_fromUtf8("button_refresh"))
        self.gridLayout.addWidget(self.button_refresh, 4, 0, 1, 1)
        self.lineEdit_directory = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_directory.sizePolicy().hasHeightForWidth())
        self.lineEdit_directory.setSizePolicy(sizePolicy)
        self.lineEdit_directory.setMinimumSize(QtCore.QSize(100, 25))
        self.lineEdit_directory.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_directory.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_directory.setObjectName(_fromUtf8("lineEdit_directory"))
        self.gridLayout.addWidget(self.lineEdit_directory, 0, 1, 1, 4)
        self.button_close = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setMinimumSize(QtCore.QSize(100, 25))
        self.button_close.setMaximumSize(QtCore.QSize(100, 25))
        self.button_close.setDefault(True)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.gridLayout.addWidget(self.button_close, 4, 4, 1, 1)
        self.lineEdit_ignoreList = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ignoreList.sizePolicy().hasHeightForWidth())
        self.lineEdit_ignoreList.setSizePolicy(sizePolicy)
        self.lineEdit_ignoreList.setMinimumSize(QtCore.QSize(300, 25))
        self.lineEdit_ignoreList.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lineEdit_ignoreList.setObjectName(_fromUtf8("lineEdit_ignoreList"))
        self.gridLayout.addWidget(self.lineEdit_ignoreList, 3, 0, 1, 5)
        self.button_apply = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_apply.sizePolicy().hasHeightForWidth())
        self.button_apply.setSizePolicy(sizePolicy)
        self.button_apply.setMinimumSize(QtCore.QSize(100, 25))
        self.button_apply.setMaximumSize(QtCore.QSize(100, 25))
        self.button_apply.setDefault(True)
        self.button_apply.setObjectName(_fromUtf8("button_apply"))
        self.gridLayout.addWidget(self.button_apply, 4, 3, 1, 1)
        self.label_timeSleep = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_timeSleep.sizePolicy().hasHeightForWidth())
        self.label_timeSleep.setSizePolicy(sizePolicy)
        self.label_timeSleep.setMinimumSize(QtCore.QSize(170, 25))
        self.label_timeSleep.setMaximumSize(QtCore.QSize(170, 25))
        self.label_timeSleep.setObjectName(_fromUtf8("label_timeSleep"))
        self.gridLayout.addWidget(self.label_timeSleep, 1, 0, 1, 2)
        self.lineEdit_timeSleep = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_timeSleep.sizePolicy().hasHeightForWidth())
        self.lineEdit_timeSleep.setSizePolicy(sizePolicy)
        self.lineEdit_timeSleep.setMinimumSize(QtCore.QSize(100, 25))
        self.lineEdit_timeSleep.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_timeSleep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_timeSleep.setObjectName(_fromUtf8("lineEdit_timeSleep"))
        self.gridLayout.addWidget(self.lineEdit_timeSleep, 1, 2, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.label_ignoreList = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ignoreList.sizePolicy().hasHeightForWidth())
        self.label_ignoreList.setSizePolicy(sizePolicy)
        self.label_ignoreList.setMinimumSize(QtCore.QSize(300, 25))
        self.label_ignoreList.setMaximumSize(QtCore.QSize(300, 25))
        self.label_ignoreList.setObjectName(_fromUtf8("label_ignoreList"))
        self.gridLayout.addWidget(self.label_ignoreList, 2, 0, 1, 4)
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
        self.label_directory.setText(_translate("ConfigureWindow", "Рабочая директория:", None))
        self.button_refresh.setText(_translate("ConfigureWindow", "Обновить", None))
        self.button_close.setText(_translate("ConfigureWindow", "Закрыть", None))
        self.button_apply.setText(_translate("ConfigureWindow", "Применить", None))
        self.label_timeSleep.setText(_translate("ConfigureWindow", "Интервал обновления, ч:", None))
        self.label_ignoreList.setText(_translate("ConfigureWindow", "Список игнорируемых файлов:", None))


class Ui_GitWindow(object):
    def setupUi(self, GitWindow):
        GitWindow.setObjectName(_fromUtf8("GitWindow"))
        GitWindow.resize(501, 597)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GitWindow.sizePolicy().hasHeightForWidth())
        GitWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(GitWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(410, 380))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_search = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_search.sizePolicy().hasHeightForWidth())
        self.tab_search.setSizePolicy(sizePolicy)
        self.tab_search.setObjectName(_fromUtf8("tab_search"))
        self.gridLayout_23 = QtGui.QGridLayout(self.tab_search)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.tabWidget_search = QtGui.QTabWidget(self.tab_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_search.sizePolicy().hasHeightForWidth())
        self.tabWidget_search.setSizePolicy(sizePolicy)
        self.tabWidget_search.setMinimumSize(QtCore.QSize(0, 100))
        self.tabWidget_search.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tabWidget_search.setObjectName(_fromUtf8("tabWidget_search"))
        self.tab_search_01 = QtGui.QWidget()
        self.tab_search_01.setObjectName(_fromUtf8("tab_search_01"))
        self.gridLayout_17 = QtGui.QGridLayout(self.tab_search_01)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.widget_int = QtGui.QWidget(self.tab_search_01)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_int.sizePolicy().hasHeightForWidth())
        self.widget_int.setSizePolicy(sizePolicy)
        self.widget_int.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_int.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_int.setObjectName(_fromUtf8("widget_int"))
        self.gridLayout_16 = QtGui.QGridLayout(self.widget_int)
        self.gridLayout_16.setMargin(0)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.label_timeFrom = QtGui.QLabel(self.widget_int)
        self.label_timeFrom.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_timeFrom.sizePolicy().hasHeightForWidth())
        self.label_timeFrom.setSizePolicy(sizePolicy)
        self.label_timeFrom.setMinimumSize(QtCore.QSize(30, 25))
        self.label_timeFrom.setMaximumSize(QtCore.QSize(30, 25))
        self.label_timeFrom.setObjectName(_fromUtf8("label_timeFrom"))
        self.gridLayout_16.addWidget(self.label_timeFrom, 1, 0, 1, 1)
        self.timeEdit_from = QtGui.QDateTimeEdit(self.widget_int)
        self.timeEdit_from.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_from.sizePolicy().hasHeightForWidth())
        self.timeEdit_from.setSizePolicy(sizePolicy)
        self.timeEdit_from.setMinimumSize(QtCore.QSize(0, 25))
        self.timeEdit_from.setMaximumSize(QtCore.QSize(16777215, 25))
        self.timeEdit_from.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_from.setDate(QtCore.QDate(2013, 1, 1))
        self.timeEdit_from.setCalendarPopup(True)
        self.timeEdit_from.setObjectName(_fromUtf8("timeEdit_from"))
        self.gridLayout_16.addWidget(self.timeEdit_from, 1, 1, 1, 1)
        self.label_timeTo = QtGui.QLabel(self.widget_int)
        self.label_timeTo.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_timeTo.sizePolicy().hasHeightForWidth())
        self.label_timeTo.setSizePolicy(sizePolicy)
        self.label_timeTo.setMinimumSize(QtCore.QSize(30, 25))
        self.label_timeTo.setMaximumSize(QtCore.QSize(30, 25))
        self.label_timeTo.setObjectName(_fromUtf8("label_timeTo"))
        self.gridLayout_16.addWidget(self.label_timeTo, 1, 2, 1, 1)
        self.timeEdit_to = QtGui.QDateTimeEdit(self.widget_int)
        self.timeEdit_to.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_to.sizePolicy().hasHeightForWidth())
        self.timeEdit_to.setSizePolicy(sizePolicy)
        self.timeEdit_to.setMinimumSize(QtCore.QSize(0, 25))
        self.timeEdit_to.setMaximumSize(QtCore.QSize(16777215, 25))
        self.timeEdit_to.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_to.setDate(QtCore.QDate(2013, 1, 1))
        self.timeEdit_to.setCalendarPopup(True)
        self.timeEdit_to.setObjectName(_fromUtf8("timeEdit_to"))
        self.gridLayout_16.addWidget(self.timeEdit_to, 1, 3, 1, 1)
        self.label_titleInt = QtGui.QLabel(self.widget_int)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_titleInt.sizePolicy().hasHeightForWidth())
        self.label_titleInt.setSizePolicy(sizePolicy)
        self.label_titleInt.setMinimumSize(QtCore.QSize(0, 25))
        self.label_titleInt.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_titleInt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleInt.setObjectName(_fromUtf8("label_titleInt"))
        self.gridLayout_16.addWidget(self.label_titleInt, 0, 0, 1, 4)
        self.gridLayout_17.addWidget(self.widget_int, 0, 0, 1, 1)
        self.tabWidget_search.addTab(self.tab_search_01, _fromUtf8(""))
        self.tab_search_02 = QtGui.QWidget()
        self.tab_search_02.setObjectName(_fromUtf8("tab_search_02"))
        self.gridLayout_19 = QtGui.QGridLayout(self.tab_search_02)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.widget_times = QtGui.QWidget(self.tab_search_02)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_times.sizePolicy().hasHeightForWidth())
        self.widget_times.setSizePolicy(sizePolicy)
        self.widget_times.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_times.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_times.setObjectName(_fromUtf8("widget_times"))
        self.gridLayout_20 = QtGui.QGridLayout(self.widget_times)
        self.gridLayout_20.setMargin(0)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.label_times = QtGui.QLabel(self.widget_times)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_times.sizePolicy().hasHeightForWidth())
        self.label_times.setSizePolicy(sizePolicy)
        self.label_times.setMinimumSize(QtCore.QSize(120, 25))
        self.label_times.setMaximumSize(QtCore.QSize(120, 25))
        self.label_times.setObjectName(_fromUtf8("label_times"))
        self.gridLayout_20.addWidget(self.label_times, 1, 0, 1, 1)
        self.spinBox_times = QtGui.QSpinBox(self.widget_times)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_times.sizePolicy().hasHeightForWidth())
        self.spinBox_times.setSizePolicy(sizePolicy)
        self.spinBox_times.setMinimumSize(QtCore.QSize(120, 25))
        self.spinBox_times.setMaximumSize(QtCore.QSize(16777215, 25))
        self.spinBox_times.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_times.setMinimum(1)
        self.spinBox_times.setMaximum(999)
        self.spinBox_times.setObjectName(_fromUtf8("spinBox_times"))
        self.gridLayout_20.addWidget(self.spinBox_times, 1, 1, 1, 1)
        self.label_titleTimes = QtGui.QLabel(self.widget_times)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_titleTimes.sizePolicy().hasHeightForWidth())
        self.label_titleTimes.setSizePolicy(sizePolicy)
        self.label_titleTimes.setMinimumSize(QtCore.QSize(0, 25))
        self.label_titleTimes.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_titleTimes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleTimes.setObjectName(_fromUtf8("label_titleTimes"))
        self.gridLayout_20.addWidget(self.label_titleTimes, 0, 0, 1, 2)
        self.gridLayout_19.addWidget(self.widget_times, 0, 0, 1, 1)
        self.tabWidget_search.addTab(self.tab_search_02, _fromUtf8(""))
        self.tab_search_03 = QtGui.QWidget()
        self.tab_search_03.setObjectName(_fromUtf8("tab_search_03"))
        self.gridLayout_21 = QtGui.QGridLayout(self.tab_search_03)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.widget_date = QtGui.QWidget(self.tab_search_03)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_date.sizePolicy().hasHeightForWidth())
        self.widget_date.setSizePolicy(sizePolicy)
        self.widget_date.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_date.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_date.setObjectName(_fromUtf8("widget_date"))
        self.gridLayout_18 = QtGui.QGridLayout(self.widget_date)
        self.gridLayout_18.setMargin(0)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.label_date = QtGui.QLabel(self.widget_date)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setMinimumSize(QtCore.QSize(100, 25))
        self.label_date.setMaximumSize(QtCore.QSize(100, 25))
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.gridLayout_18.addWidget(self.label_date, 1, 0, 1, 1)
        self.dateEdit_date = QtGui.QDateEdit(self.widget_date)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_date.setSizePolicy(sizePolicy)
        self.dateEdit_date.setMinimumSize(QtCore.QSize(150, 25))
        self.dateEdit_date.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dateEdit_date.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_date.setDate(QtCore.QDate(2013, 1, 1))
        self.dateEdit_date.setCalendarPopup(True)
        self.dateEdit_date.setObjectName(_fromUtf8("dateEdit_date"))
        self.gridLayout_18.addWidget(self.dateEdit_date, 1, 1, 1, 1)
        self.label_titleDate = QtGui.QLabel(self.widget_date)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_titleDate.sizePolicy().hasHeightForWidth())
        self.label_titleDate.setSizePolicy(sizePolicy)
        self.label_titleDate.setMinimumSize(QtCore.QSize(0, 25))
        self.label_titleDate.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_titleDate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleDate.setObjectName(_fromUtf8("label_titleDate"))
        self.gridLayout_18.addWidget(self.label_titleDate, 0, 0, 1, 2)
        self.gridLayout_21.addWidget(self.widget_date, 0, 0, 1, 1)
        self.tabWidget_search.addTab(self.tab_search_03, _fromUtf8(""))
        self.gridLayout_23.addWidget(self.tabWidget_search, 0, 0, 1, 1)
        self.list_commit = QtGui.QListWidget(self.tab_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_commit.sizePolicy().hasHeightForWidth())
        self.list_commit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.list_commit.setFont(font)
        self.list_commit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.list_commit.setObjectName(_fromUtf8("list_commit"))
        self.gridLayout_23.addWidget(self.list_commit, 2, 0, 1, 1)
        self.widget_buttonGet = QtGui.QWidget(self.tab_search)
        self.widget_buttonGet.setObjectName(_fromUtf8("widget_buttonGet"))
        self.gridLayout_22 = QtGui.QGridLayout(self.widget_buttonGet)
        self.gridLayout_22.setMargin(0)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem, 0, 0, 1, 1)
        self.button_get = QtGui.QPushButton(self.widget_buttonGet)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_get.sizePolicy().hasHeightForWidth())
        self.button_get.setSizePolicy(sizePolicy)
        self.button_get.setMinimumSize(QtCore.QSize(100, 25))
        self.button_get.setMaximumSize(QtCore.QSize(100, 25))
        self.button_get.setDefault(True)
        self.button_get.setObjectName(_fromUtf8("button_get"))
        self.gridLayout_22.addWidget(self.button_get, 0, 1, 1, 1)
        self.gridLayout_23.addWidget(self.widget_buttonGet, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_search, _fromUtf8(""))
        self.tab_status = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_status.sizePolicy().hasHeightForWidth())
        self.tab_status.setSizePolicy(sizePolicy)
        self.tab_status.setObjectName(_fromUtf8("tab_status"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_status)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.widget_buttonsStatus = QtGui.QWidget(self.tab_status)
        self.widget_buttonsStatus.setObjectName(_fromUtf8("widget_buttonsStatus"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget_buttonsStatus)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.button_createCommit = QtGui.QPushButton(self.widget_buttonsStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_createCommit.sizePolicy().hasHeightForWidth())
        self.button_createCommit.setSizePolicy(sizePolicy)
        self.button_createCommit.setMinimumSize(QtCore.QSize(125, 25))
        self.button_createCommit.setMaximumSize(QtCore.QSize(125, 25))
        self.button_createCommit.setDefault(True)
        self.button_createCommit.setObjectName(_fromUtf8("button_createCommit"))
        self.gridLayout_3.addWidget(self.button_createCommit, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.button_status = QtGui.QPushButton(self.widget_buttonsStatus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_status.sizePolicy().hasHeightForWidth())
        self.button_status.setSizePolicy(sizePolicy)
        self.button_status.setMinimumSize(QtCore.QSize(125, 25))
        self.button_status.setMaximumSize(QtCore.QSize(100, 25))
        self.button_status.setDefault(True)
        self.button_status.setObjectName(_fromUtf8("button_status"))
        self.gridLayout_3.addWidget(self.button_status, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.widget_buttonsStatus, 0, 0, 1, 1)
        self.text_status = QtGui.QTextBrowser(self.tab_status)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_status.sizePolicy().hasHeightForWidth())
        self.text_status.setSizePolicy(sizePolicy)
        self.text_status.setMinimumSize(QtCore.QSize(411, 311))
        self.text_status.setObjectName(_fromUtf8("text_status"))
        self.gridLayout_4.addWidget(self.text_status, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_status, _fromUtf8(""))
        self.tab_merge = QtGui.QWidget()
        self.tab_merge.setObjectName(_fromUtf8("tab_merge"))
        self.gridLayout_13 = QtGui.QGridLayout(self.tab_merge)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.label_merge = QtGui.QLabel(self.tab_merge)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_merge.sizePolicy().hasHeightForWidth())
        self.label_merge.setSizePolicy(sizePolicy)
        self.label_merge.setMinimumSize(QtCore.QSize(0, 50))
        self.label_merge.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_merge.setObjectName(_fromUtf8("label_merge"))
        self.gridLayout_13.addWidget(self.label_merge, 0, 0, 1, 1)
        self.tabWidget_merge = QtGui.QTabWidget(self.tab_merge)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_merge.sizePolicy().hasHeightForWidth())
        self.tabWidget_merge.setSizePolicy(sizePolicy)
        self.tabWidget_merge.setMinimumSize(QtCore.QSize(0, 130))
        self.tabWidget_merge.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tabWidget_merge.setObjectName(_fromUtf8("tabWidget_merge"))
        self.tab_merge_01 = QtGui.QWidget()
        self.tab_merge_01.setObjectName(_fromUtf8("tab_merge_01"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_merge_01)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.widget_search = QtGui.QWidget(self.tab_merge_01)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_search.sizePolicy().hasHeightForWidth())
        self.widget_search.setSizePolicy(sizePolicy)
        self.widget_search.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_search.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_search.setObjectName(_fromUtf8("widget_search"))
        self.gridLayout_11 = QtGui.QGridLayout(self.widget_search)
        self.gridLayout_11.setMargin(0)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.box_old = QtGui.QComboBox(self.widget_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_old.sizePolicy().hasHeightForWidth())
        self.box_old.setSizePolicy(sizePolicy)
        self.box_old.setMinimumSize(QtCore.QSize(200, 25))
        self.box_old.setMaximumSize(QtCore.QSize(16777215, 25))
        self.box_old.setObjectName(_fromUtf8("box_old"))
        self.gridLayout_11.addWidget(self.box_old, 1, 1, 1, 1)
        self.label_titleSearch = QtGui.QLabel(self.widget_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_titleSearch.sizePolicy().hasHeightForWidth())
        self.label_titleSearch.setSizePolicy(sizePolicy)
        self.label_titleSearch.setMinimumSize(QtCore.QSize(0, 25))
        self.label_titleSearch.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_titleSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleSearch.setObjectName(_fromUtf8("label_titleSearch"))
        self.gridLayout_11.addWidget(self.label_titleSearch, 0, 0, 1, 2)
        self.label_old01 = QtGui.QLabel(self.widget_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_old01.sizePolicy().hasHeightForWidth())
        self.label_old01.setSizePolicy(sizePolicy)
        self.label_old01.setMinimumSize(QtCore.QSize(100, 25))
        self.label_old01.setMaximumSize(QtCore.QSize(100, 25))
        self.label_old01.setObjectName(_fromUtf8("label_old01"))
        self.gridLayout_11.addWidget(self.label_old01, 1, 0, 1, 1)
        self.box_new = QtGui.QComboBox(self.widget_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_new.sizePolicy().hasHeightForWidth())
        self.box_new.setSizePolicy(sizePolicy)
        self.box_new.setMinimumSize(QtCore.QSize(200, 25))
        self.box_new.setMaximumSize(QtCore.QSize(16777215, 25))
        self.box_new.setObjectName(_fromUtf8("box_new"))
        self.gridLayout_11.addWidget(self.box_new, 2, 1, 1, 1)
        self.label_new01 = QtGui.QLabel(self.widget_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_new01.sizePolicy().hasHeightForWidth())
        self.label_new01.setSizePolicy(sizePolicy)
        self.label_new01.setMinimumSize(QtCore.QSize(100, 25))
        self.label_new01.setMaximumSize(QtCore.QSize(100, 25))
        self.label_new01.setObjectName(_fromUtf8("label_new01"))
        self.gridLayout_11.addWidget(self.label_new01, 2, 0, 1, 1)
        self.gridLayout_12.addWidget(self.widget_search, 0, 0, 1, 1)
        self.tabWidget_merge.addTab(self.tab_merge_01, _fromUtf8(""))
        self.tab_merge_02 = QtGui.QWidget()
        self.tab_merge_02.setObjectName(_fromUtf8("tab_merge_02"))
        self.gridLayout_15 = QtGui.QGridLayout(self.tab_merge_02)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.widget_browse = QtGui.QWidget(self.tab_merge_02)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_browse.sizePolicy().hasHeightForWidth())
        self.widget_browse.setSizePolicy(sizePolicy)
        self.widget_browse.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_browse.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_browse.setObjectName(_fromUtf8("widget_browse"))
        self.gridLayout_14 = QtGui.QGridLayout(self.widget_browse)
        self.gridLayout_14.setMargin(0)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.label_old02 = QtGui.QLabel(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_old02.sizePolicy().hasHeightForWidth())
        self.label_old02.setSizePolicy(sizePolicy)
        self.label_old02.setMinimumSize(QtCore.QSize(100, 25))
        self.label_old02.setMaximumSize(QtCore.QSize(100, 25))
        self.label_old02.setObjectName(_fromUtf8("label_old02"))
        self.gridLayout_14.addWidget(self.label_old02, 1, 0, 1, 1)
        self.lineEdit_old = QtGui.QLineEdit(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_old.sizePolicy().hasHeightForWidth())
        self.lineEdit_old.setSizePolicy(sizePolicy)
        self.lineEdit_old.setMinimumSize(QtCore.QSize(150, 25))
        self.lineEdit_old.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_old.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_old.setObjectName(_fromUtf8("lineEdit_old"))
        self.gridLayout_14.addWidget(self.lineEdit_old, 1, 1, 1, 1)
        self.button_browseOld = QtGui.QPushButton(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browseOld.sizePolicy().hasHeightForWidth())
        self.button_browseOld.setSizePolicy(sizePolicy)
        self.button_browseOld.setMinimumSize(QtCore.QSize(75, 25))
        self.button_browseOld.setMaximumSize(QtCore.QSize(75, 25))
        self.button_browseOld.setDefault(True)
        self.button_browseOld.setObjectName(_fromUtf8("button_browseOld"))
        self.gridLayout_14.addWidget(self.button_browseOld, 1, 2, 1, 1)
        self.label_new02 = QtGui.QLabel(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_new02.sizePolicy().hasHeightForWidth())
        self.label_new02.setSizePolicy(sizePolicy)
        self.label_new02.setMinimumSize(QtCore.QSize(100, 25))
        self.label_new02.setMaximumSize(QtCore.QSize(100, 25))
        self.label_new02.setObjectName(_fromUtf8("label_new02"))
        self.gridLayout_14.addWidget(self.label_new02, 2, 0, 1, 1)
        self.lineEdit_new = QtGui.QLineEdit(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_new.sizePolicy().hasHeightForWidth())
        self.lineEdit_new.setSizePolicy(sizePolicy)
        self.lineEdit_new.setMinimumSize(QtCore.QSize(150, 25))
        self.lineEdit_new.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_new.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_new.setObjectName(_fromUtf8("lineEdit_new"))
        self.gridLayout_14.addWidget(self.lineEdit_new, 2, 1, 1, 1)
        self.button_browseNew = QtGui.QPushButton(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browseNew.sizePolicy().hasHeightForWidth())
        self.button_browseNew.setSizePolicy(sizePolicy)
        self.button_browseNew.setMinimumSize(QtCore.QSize(75, 25))
        self.button_browseNew.setMaximumSize(QtCore.QSize(75, 25))
        self.button_browseNew.setDefault(True)
        self.button_browseNew.setObjectName(_fromUtf8("button_browseNew"))
        self.gridLayout_14.addWidget(self.button_browseNew, 2, 2, 1, 1)
        self.label_titleBrowse = QtGui.QLabel(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.label_titleBrowse.sizePolicy().hasHeightForWidth())
        self.label_titleBrowse.setSizePolicy(sizePolicy)
        self.label_titleBrowse.setMinimumSize(QtCore.QSize(0, 25))
        self.label_titleBrowse.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleBrowse.setObjectName(_fromUtf8("label_titleBrowse"))
        self.gridLayout_14.addWidget(self.label_titleBrowse, 0, 0, 1, 3)
        self.gridLayout_15.addWidget(self.widget_browse, 0, 0, 1, 1)
        self.tabWidget_merge.addTab(self.tab_merge_02, _fromUtf8(""))
        self.gridLayout_13.addWidget(self.tabWidget_merge, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem2, 2, 0, 1, 1)
        self.widget_buttonsApply = QtGui.QWidget(self.tab_merge)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_buttonsApply.sizePolicy().hasHeightForWidth())
        self.widget_buttonsApply.setSizePolicy(sizePolicy)
        self.widget_buttonsApply.setMinimumSize(QtCore.QSize(0, 62))
        self.widget_buttonsApply.setMaximumSize(QtCore.QSize(16777215, 62))
        self.widget_buttonsApply.setObjectName(_fromUtf8("widget_buttonsApply"))
        self.gridLayout_10 = QtGui.QGridLayout(self.widget_buttonsApply)
        self.gridLayout_10.setMargin(0)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        spacerItem3 = QtGui.QSpacerItem(36, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 1, 0, 1, 1)
        self.button_patch = QtGui.QPushButton(self.widget_buttonsApply)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_patch.sizePolicy().hasHeightForWidth())
        self.button_patch.setSizePolicy(sizePolicy)
        self.button_patch.setMinimumSize(QtCore.QSize(150, 25))
        self.button_patch.setMaximumSize(QtCore.QSize(150, 25))
        self.button_patch.setDefault(True)
        self.button_patch.setObjectName(_fromUtf8("button_patch"))
        self.gridLayout_10.addWidget(self.button_patch, 1, 1, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(86, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 2, 0, 1, 2)
        self.button_applyPatch = QtGui.QPushButton(self.widget_buttonsApply)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_applyPatch.sizePolicy().hasHeightForWidth())
        self.button_applyPatch.setSizePolicy(sizePolicy)
        self.button_applyPatch.setMinimumSize(QtCore.QSize(100, 25))
        self.button_applyPatch.setMaximumSize(QtCore.QSize(100, 25))
        self.button_applyPatch.setDefault(True)
        self.button_applyPatch.setObjectName(_fromUtf8("button_applyPatch"))
        self.gridLayout_10.addWidget(self.button_applyPatch, 2, 2, 1, 1)
        self.gridLayout_13.addWidget(self.widget_buttonsApply, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_merge, _fromUtf8(""))
        self.tab_reset = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_reset.sizePolicy().hasHeightForWidth())
        self.tab_reset.setSizePolicy(sizePolicy)
        self.tab_reset.setObjectName(_fromUtf8("tab_reset"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_reset)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_text1 = QtGui.QLabel(self.tab_reset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_text1.sizePolicy().hasHeightForWidth())
        self.label_text1.setSizePolicy(sizePolicy)
        self.label_text1.setMinimumSize(QtCore.QSize(401, 25))
        self.label_text1.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_text1.setObjectName(_fromUtf8("label_text1"))
        self.gridLayout_9.addWidget(self.label_text1, 0, 0, 1, 1)
        self.label_text2 = QtGui.QLabel(self.tab_reset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_text2.sizePolicy().hasHeightForWidth())
        self.label_text2.setSizePolicy(sizePolicy)
        self.label_text2.setMinimumSize(QtCore.QSize(401, 25))
        self.label_text2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text2.setObjectName(_fromUtf8("label_text2"))
        self.gridLayout_9.addWidget(self.label_text2, 1, 0, 1, 1)
        self.label_text3 = QtGui.QLabel(self.tab_reset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_text3.sizePolicy().hasHeightForWidth())
        self.label_text3.setSizePolicy(sizePolicy)
        self.label_text3.setMinimumSize(QtCore.QSize(401, 25))
        self.label_text3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_text3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text3.setObjectName(_fromUtf8("label_text3"))
        self.gridLayout_9.addWidget(self.label_text3, 2, 0, 1, 1)
        self.label_text4 = QtGui.QLabel(self.tab_reset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_text4.sizePolicy().hasHeightForWidth())
        self.label_text4.setSizePolicy(sizePolicy)
        self.label_text4.setMinimumSize(QtCore.QSize(401, 25))
        self.label_text4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_text4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text4.setObjectName(_fromUtf8("label_text4"))
        self.gridLayout_9.addWidget(self.label_text4, 3, 0, 1, 1)
        self.widget_idCommit = QtGui.QWidget(self.tab_reset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_idCommit.sizePolicy().hasHeightForWidth())
        self.widget_idCommit.setSizePolicy(sizePolicy)
        self.widget_idCommit.setObjectName(_fromUtf8("widget_idCommit"))
        self.gridLayout_8 = QtGui.QGridLayout(self.widget_idCommit)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_id = QtGui.QLabel(self.widget_idCommit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id.sizePolicy().hasHeightForWidth())
        self.label_id.setSizePolicy(sizePolicy)
        self.label_id.setMinimumSize(QtCore.QSize(175, 25))
        self.label_id.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.gridLayout_8.addWidget(self.label_id, 0, 0, 1, 1)
        self.lineEdit_id = QtGui.QLineEdit(self.widget_idCommit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_id.setSizePolicy(sizePolicy)
        self.lineEdit_id.setMinimumSize(QtCore.QSize(175, 25))
        self.lineEdit_id.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_id.setObjectName(_fromUtf8("lineEdit_id"))
        self.gridLayout_8.addWidget(self.lineEdit_id, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.widget_idCommit, 4, 0, 1, 1)
        self.widget_typeReset = QtGui.QWidget(self.tab_reset)
        self.widget_typeReset.setObjectName(_fromUtf8("widget_typeReset"))
        self.gridLayout_7 = QtGui.QGridLayout(self.widget_typeReset)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_typeReset = QtGui.QLabel(self.widget_typeReset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_typeReset.sizePolicy().hasHeightForWidth())
        self.label_typeReset.setSizePolicy(sizePolicy)
        self.label_typeReset.setMinimumSize(QtCore.QSize(100, 25))
        self.label_typeReset.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_typeReset.setObjectName(_fromUtf8("label_typeReset"))
        self.gridLayout_7.addWidget(self.label_typeReset, 0, 0, 1, 1)
        self.box_typeReset = QtGui.QComboBox(self.widget_typeReset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_typeReset.sizePolicy().hasHeightForWidth())
        self.box_typeReset.setSizePolicy(sizePolicy)
        self.box_typeReset.setMinimumSize(QtCore.QSize(160, 25))
        self.box_typeReset.setMaximumSize(QtCore.QSize(16777215, 25))
        self.box_typeReset.setObjectName(_fromUtf8("box_typeReset"))
        self.box_typeReset.addItem(_fromUtf8(""))
        self.box_typeReset.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.box_typeReset, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.widget_typeReset, 5, 0, 1, 1)
        self.widget_fileName = QtGui.QWidget(self.tab_reset)
        self.widget_fileName.setObjectName(_fromUtf8("widget_fileName"))
        self.gridLayout_6 = QtGui.QGridLayout(self.widget_fileName)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.box_filename = QtGui.QComboBox(self.widget_fileName)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_filename.sizePolicy().hasHeightForWidth())
        self.box_filename.setSizePolicy(sizePolicy)
        self.box_filename.setMinimumSize(QtCore.QSize(0, 25))
        self.box_filename.setMaximumSize(QtCore.QSize(16777215, 25))
        self.box_filename.setObjectName(_fromUtf8("box_filename"))
        self.gridLayout_6.addWidget(self.box_filename, 0, 1, 1, 1)
        self.label_filename = QtGui.QLabel(self.widget_fileName)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_filename.sizePolicy().hasHeightForWidth())
        self.label_filename.setSizePolicy(sizePolicy)
        self.label_filename.setMinimumSize(QtCore.QSize(120, 25))
        self.label_filename.setMaximumSize(QtCore.QSize(0, 25))
        self.label_filename.setObjectName(_fromUtf8("label_filename"))
        self.gridLayout_6.addWidget(self.label_filename, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.widget_fileName, 6, 0, 1, 1)
        self.widget_buttonsReset = QtGui.QWidget(self.tab_reset)
        self.widget_buttonsReset.setObjectName(_fromUtf8("widget_buttonsReset"))
        self.gridLayout_5 = QtGui.QGridLayout(self.widget_buttonsReset)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.button_refresh = QtGui.QPushButton(self.widget_buttonsReset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_refresh.sizePolicy().hasHeightForWidth())
        self.button_refresh.setSizePolicy(sizePolicy)
        self.button_refresh.setMinimumSize(QtCore.QSize(135, 25))
        self.button_refresh.setMaximumSize(QtCore.QSize(135, 25))
        self.button_refresh.setDefault(True)
        self.button_refresh.setObjectName(_fromUtf8("button_refresh"))
        self.gridLayout_5.addWidget(self.button_refresh, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 1, 1, 1)
        self.button_reset = QtGui.QPushButton(self.widget_buttonsReset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_reset.sizePolicy().hasHeightForWidth())
        self.button_reset.setSizePolicy(sizePolicy)
        self.button_reset.setMinimumSize(QtCore.QSize(100, 25))
        self.button_reset.setMaximumSize(QtCore.QSize(100, 25))
        self.button_reset.setDefault(True)
        self.button_reset.setObjectName(_fromUtf8("button_reset"))
        self.gridLayout_5.addWidget(self.button_reset, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.widget_buttonsReset, 7, 0, 1, 1)
        self.text_reset = QtGui.QTextBrowser(self.tab_reset)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_reset.sizePolicy().hasHeightForWidth())
        self.text_reset.setSizePolicy(sizePolicy)
        self.text_reset.setMinimumSize(QtCore.QSize(401, 131))
        self.text_reset.setObjectName(_fromUtf8("text_reset"))
        self.gridLayout_9.addWidget(self.text_reset, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tab_reset, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.widget_buttonClose = QtGui.QWidget(self.centralwidget)
        self.widget_buttonClose.setObjectName(_fromUtf8("widget_buttonClose"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_buttonClose)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem6 = QtGui.QSpacerItem(40, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 0, 1, 1)
        self.button_close = QtGui.QPushButton(self.widget_buttonClose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setMinimumSize(QtCore.QSize(100, 25))
        self.button_close.setMaximumSize(QtCore.QSize(100, 25))
        self.button_close.setDefault(True)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.gridLayout_2.addWidget(self.button_close, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_buttonClose, 1, 0, 1, 1)
        GitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GitWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_search.setCurrentIndex(0)
        self.tabWidget_merge.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GitWindow)
        #GitWindow.setTabOrder(self.tabWidget, self.tabWidget)
        GitWindow.setTabOrder(self.tabWidget, self.tabWidget_search)
        GitWindow.setTabOrder(self.tabWidget_search, self.timeEdit_from)
        GitWindow.setTabOrder(self.timeEdit_from, self.timeEdit_to)
        GitWindow.setTabOrder(self.timeEdit_to, self.spinBox_times)
        GitWindow.setTabOrder(self.spinBox_times, self.dateEdit_date)
        GitWindow.setTabOrder(self.dateEdit_date, self.button_get)
        GitWindow.setTabOrder(self.button_get, self.list_commit)
        GitWindow.setTabOrder(self.list_commit, self.button_createCommit)
        GitWindow.setTabOrder(self.button_createCommit, self.button_status)
        GitWindow.setTabOrder(self.button_status, self.text_status)
        GitWindow.setTabOrder(self.text_status, self.tabWidget_merge)
        GitWindow.setTabOrder(self.tabWidget_merge, self.box_old)
        GitWindow.setTabOrder(self.box_old, self.box_new)
        GitWindow.setTabOrder(self.box_new, self.lineEdit_old)
        GitWindow.setTabOrder(self.lineEdit_old, self.button_browseOld)
        GitWindow.setTabOrder(self.button_browseOld, self.lineEdit_new)
        GitWindow.setTabOrder(self.lineEdit_new, self.button_browseNew)
        GitWindow.setTabOrder(self.button_browseNew, self.button_patch)
        GitWindow.setTabOrder(self.button_patch, self.button_applyPatch)
        GitWindow.setTabOrder(self.button_applyPatch, self.lineEdit_id)
        GitWindow.setTabOrder(self.lineEdit_id, self.box_typeReset)
        GitWindow.setTabOrder(self.box_typeReset, self.box_filename)
        GitWindow.setTabOrder(self.box_filename, self.button_refresh)
        GitWindow.setTabOrder(self.button_refresh, self.button_reset)
        GitWindow.setTabOrder(self.button_reset, self.text_reset)
        GitWindow.setTabOrder(self.text_reset, self.button_close)

    def retranslateUi(self, GitWindow):
        GitWindow.setWindowTitle(_translate("GitWindow", "Работа с git", None))
        self.label_timeFrom.setText(_translate("GitWindow", "с", None))
        self.timeEdit_from.setDisplayFormat(_translate("GitWindow", "HH:mm dd.MM.yyyy", None))
        self.label_timeTo.setText(_translate("GitWindow", "по", None))
        self.timeEdit_to.setDisplayFormat(_translate("GitWindow", "H:mm dd.MM.yyyy", None))
        self.label_titleInt.setText(_translate("GitWindow", "В указанный интервал", None))
        self.tabWidget_search.setTabText(self.tabWidget_search.indexOf(self.tab_search_01), _translate("GitWindow", "В интервал", None))
        self.label_times.setText(_translate("GitWindow", "Число коммитов", None))
        self.label_titleTimes.setText(_translate("GitWindow", "По количеству коммитов", None))
        self.tabWidget_search.setTabText(self.tabWidget_search.indexOf(self.tab_search_02), _translate("GitWindow", "По числу коммитов", None))
        self.label_date.setText(_translate("GitWindow", "Дата коммита", None))
        self.dateEdit_date.setDisplayFormat(_translate("GitWindow", "dd.MM.yyyy", None))
        self.label_titleDate.setText(_translate("GitWindow", "По дате коммита", None))
        self.tabWidget_search.setTabText(self.tabWidget_search.indexOf(self.tab_search_03), _translate("GitWindow", "По дате", None))
        self.button_get.setText(_translate("GitWindow", "Вывести", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_search), _translate("GitWindow", "Поиск", None))
        self.button_createCommit.setText(_translate("GitWindow", "Создать коммит", None))
        self.button_status.setText(_translate("GitWindow", "Показать статус", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_status), _translate("GitWindow", "Статус", None))
        self.label_merge.setText(_translate("GitWindow", "<html><head/><body><p align=\"center\">Изменения будут применены от <span style=\" font-weight:600; color:#ff0000;\">СТАРОГО</span> файла к <span style=\" font-weight:600; color:#ff0000;\">НОВОМУ</span>.</p><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">НОВЫЙ</span> файл будет <span style=\" font-weight:600;\">ПЕРЕЗАПИСАН</span>.</p></body></html>", None))
        self.label_titleSearch.setText(_translate("GitWindow", "Поиск файлов", None))
        self.label_old01.setText(_translate("GitWindow", "Старый файл", None))
        self.label_new01.setText(_translate("GitWindow", "Новый файл", None))
        self.tabWidget_merge.setTabText(self.tabWidget_merge.indexOf(self.tab_merge_01), _translate("GitWindow", "Поиск", None))
        self.label_old02.setText(_translate("GitWindow", "Старый файл", None))
        self.button_browseOld.setText(_translate("GitWindow", "Обзор", None))
        self.label_new02.setText(_translate("GitWindow", "Новый файл", None))
        self.button_browseNew.setText(_translate("GitWindow", "Обзор", None))
        self.label_titleBrowse.setText(_translate("GitWindow", "Указать файл вручную", None))
        self.tabWidget_merge.setTabText(self.tabWidget_merge.indexOf(self.tab_merge_02), _translate("GitWindow", "Указать", None))
        self.button_patch.setText(_translate("GitWindow", "Редактировать патч", None))
        self.button_applyPatch.setText(_translate("GitWindow", "Принять", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_merge), _translate("GitWindow", "Слияние", None))
        self.label_text1.setText(_translate("GitWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Внимание!</span></p></body></html>", None))
        self.label_text2.setText(_translate("GitWindow", "Откат изменений может нарушить работу Вашей системы.", None))
        self.label_text3.setText(_translate("GitWindow", "Откат к ранним версиям осуществляйте", None))
        self.label_text4.setText(_translate("GitWindow", "на свой страх и риск.", None))
        self.label_id.setText(_translate("GitWindow", "Идентификатор коммита", None))
        self.label_typeReset.setText(_translate("GitWindow", "Тип отката", None))
        self.box_typeReset.setItemText(0, _translate("GitWindow", "Откат всех файлов", None))
        self.box_typeReset.setItemText(1, _translate("GitWindow", "Откат одного файла", None))
        self.label_filename.setText(_translate("GitWindow", "Выберете файл", None))
        self.button_refresh.setText(_translate("GitWindow", "Обновить список", None))
        self.button_reset.setText(_translate("GitWindow", "Откатить", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reset), _translate("GitWindow", "Откат изменений", None))
        self.button_close.setText(_translate("GitWindow", "Закрыть", None))


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName(_fromUtf8("SettingsWindow"))
        SettingsWindow.resize(429, 203)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(SettingsWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 203))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget_lang = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_lang.sizePolicy().hasHeightForWidth())
        self.widget_lang.setSizePolicy(sizePolicy)
        self.widget_lang.setObjectName(_fromUtf8("widget_lang"))
        self.formLayout = QtGui.QFormLayout(self.widget_lang)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_lang = QtGui.QLabel(self.widget_lang)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lang.sizePolicy().hasHeightForWidth())
        self.label_lang.setSizePolicy(sizePolicy)
        self.label_lang.setMinimumSize(QtCore.QSize(100, 25))
        self.label_lang.setMaximumSize(QtCore.QSize(100, 25))
        self.label_lang.setObjectName(_fromUtf8("label_lang"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_lang)
        self.box_lang = QtGui.QComboBox(self.widget_lang)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_lang.sizePolicy().hasHeightForWidth())
        self.box_lang.setSizePolicy(sizePolicy)
        self.box_lang.setMinimumSize(QtCore.QSize(275, 25))
        self.box_lang.setMaximumSize(QtCore.QSize(16777215, 25))
        self.box_lang.setObjectName(_fromUtf8("box_lang"))
        self.box_lang.addItem(_fromUtf8(""))
        self.box_lang.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.box_lang)
        self.gridLayout_3.addWidget(self.widget_lang, 0, 0, 1, 1)
        self.widget_service = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_service.sizePolicy().hasHeightForWidth())
        self.widget_service.setSizePolicy(sizePolicy)
        self.widget_service.setObjectName(_fromUtf8("widget_service"))
        self.formLayout_2 = QtGui.QFormLayout(self.widget_service)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_service = QtGui.QLabel(self.widget_service)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_service.sizePolicy().hasHeightForWidth())
        self.label_service.setSizePolicy(sizePolicy)
        self.label_service.setMinimumSize(QtCore.QSize(100, 25))
        self.label_service.setMaximumSize(QtCore.QSize(100, 25))
        self.label_service.setObjectName(_fromUtf8("label_service"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_service)
        self.lineEdit_service = QtGui.QLineEdit(self.widget_service)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_service.sizePolicy().hasHeightForWidth())
        self.lineEdit_service.setSizePolicy(sizePolicy)
        self.lineEdit_service.setMinimumSize(QtCore.QSize(275, 25))
        self.lineEdit_service.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_service.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_service.setObjectName(_fromUtf8("lineEdit_service"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_service)
        self.gridLayout_3.addWidget(self.widget_service, 1, 0, 1, 1)
        self.widget_config = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_config.sizePolicy().hasHeightForWidth())
        self.widget_config.setSizePolicy(sizePolicy)
        self.widget_config.setObjectName(_fromUtf8("widget_config"))
        self.formLayout_6 = QtGui.QFormLayout(self.widget_config)
        self.formLayout_6.setMargin(0)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_config = QtGui.QLabel(self.widget_config)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config.sizePolicy().hasHeightForWidth())
        self.label_config.setSizePolicy(sizePolicy)
        self.label_config.setMinimumSize(QtCore.QSize(125, 25))
        self.label_config.setMaximumSize(QtCore.QSize(125, 25))
        self.label_config.setObjectName(_fromUtf8("label_config"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_config)
        self.lineEdit_config = QtGui.QLineEdit(self.widget_config)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config.sizePolicy().hasHeightForWidth())
        self.lineEdit_config.setSizePolicy(sizePolicy)
        self.lineEdit_config.setMinimumSize(QtCore.QSize(170, 25))
        self.lineEdit_config.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_config.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_config.setObjectName(_fromUtf8("lineEdit_config"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_config)
        self.gridLayout_3.addWidget(self.widget_config, 2, 0, 1, 1)
        self.widget_browse = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_browse.sizePolicy().hasHeightForWidth())
        self.widget_browse.setSizePolicy(sizePolicy)
        self.widget_browse.setObjectName(_fromUtf8("widget_browse"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_browse)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.button_browse = QtGui.QPushButton(self.widget_browse)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browse.sizePolicy().hasHeightForWidth())
        self.button_browse.setSizePolicy(sizePolicy)
        self.button_browse.setMinimumSize(QtCore.QSize(100, 25))
        self.button_browse.setMaximumSize(QtCore.QSize(100, 25))
        self.button_browse.setObjectName(_fromUtf8("button_browse"))
        self.gridLayout_2.addWidget(self.button_browse, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_browse, 3, 0, 1, 1)
        self.widget_editor = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_editor.sizePolicy().hasHeightForWidth())
        self.widget_editor.setSizePolicy(sizePolicy)
        self.widget_editor.setObjectName(_fromUtf8("widget_editor"))
        self.formLayout_5 = QtGui.QFormLayout(self.widget_editor)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_5.setMargin(0)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_editor = QtGui.QLabel(self.widget_editor)
        self.label_editor.setMinimumSize(QtCore.QSize(140, 25))
        self.label_editor.setMaximumSize(QtCore.QSize(140, 25))
        self.label_editor.setObjectName(_fromUtf8("label_editor"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_editor)
        self.lineEdit_editor = QtGui.QLineEdit(self.widget_editor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_editor.sizePolicy().hasHeightForWidth())
        self.lineEdit_editor.setSizePolicy(sizePolicy)
        self.lineEdit_editor.setMinimumSize(QtCore.QSize(250, 25))
        self.lineEdit_editor.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_editor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_editor.setObjectName(_fromUtf8("lineEdit_editor"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_editor)
        self.gridLayout_3.addWidget(self.widget_editor, 4, 0, 1, 1)
        self.widget_buttons = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_buttons.sizePolicy().hasHeightForWidth())
        self.widget_buttons.setSizePolicy(sizePolicy)
        self.widget_buttons.setObjectName(_fromUtf8("widget_buttons"))
        self.gridLayout = QtGui.QGridLayout(self.widget_buttons)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_default = QtGui.QPushButton(self.widget_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_default.sizePolicy().hasHeightForWidth())
        self.button_default.setSizePolicy(sizePolicy)
        self.button_default.setMinimumSize(QtCore.QSize(125, 25))
        self.button_default.setMaximumSize(QtCore.QSize(125, 25))
        self.button_default.setDefault(True)
        self.button_default.setObjectName(_fromUtf8("button_default"))
        self.gridLayout.addWidget(self.button_default, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.button_apply = QtGui.QPushButton(self.widget_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_apply.sizePolicy().hasHeightForWidth())
        self.button_apply.setSizePolicy(sizePolicy)
        self.button_apply.setMinimumSize(QtCore.QSize(100, 25))
        self.button_apply.setMaximumSize(QtCore.QSize(25, 100))
        self.button_apply.setDefault(True)
        self.button_apply.setObjectName(_fromUtf8("button_apply"))
        self.gridLayout.addWidget(self.button_apply, 0, 2, 1, 1)
        self.button_close = QtGui.QPushButton(self.widget_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setMinimumSize(QtCore.QSize(100, 25))
        self.button_close.setMaximumSize(QtCore.QSize(100, 25))
        self.button_close.setDefault(True)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.gridLayout.addWidget(self.button_close, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.widget_buttons, 5, 0, 1, 1)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)
        SettingsWindow.setTabOrder(self.box_lang, self.lineEdit_service)
        SettingsWindow.setTabOrder(self.lineEdit_service, self.lineEdit_config)
        SettingsWindow.setTabOrder(self.lineEdit_config, self.button_browse)
        SettingsWindow.setTabOrder(self.button_browse, self.lineEdit_editor)
        SettingsWindow.setTabOrder(self.lineEdit_editor, self.button_default)
        SettingsWindow.setTabOrder(self.button_default, self.button_apply)
        SettingsWindow.setTabOrder(self.button_apply, self.button_close)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Настройки", None))
        self.label_lang.setText(_translate("SettingsWindow", "Язык", None))
        self.box_lang.setItemText(0, _translate("SettingsWindow", "English", None))
        self.box_lang.setItemText(1, _translate("SettingsWindow", "Русский", None))
        self.label_service.setText(_translate("SettingsWindow", "Service", None))
        self.label_config.setText(_translate("SettingsWindow", "Настройки git-etc", None))
        self.button_browse.setText(_translate("SettingsWindow", "Обзор", None))
        self.label_editor.setText(_translate("SettingsWindow", "Текстовый редактор", None))
        self.button_default.setText(_translate("SettingsWindow", "По умолчанию", None))
        self.button_apply.setText(_translate("SettingsWindow", "Применить", None))
        self.button_close.setText(_translate("SettingsWindow", "Закрыть", None))


class Ui_NotFound(object):
    def setupUi(self, NotFound):
        NotFound.setObjectName(_fromUtf8("NotFound"))
        NotFound.resize(320, 90)
        self.centralwidget = QtGui.QWidget(NotFound)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_textError = QtGui.QLabel(self.centralwidget)
        self.label_textError.setGeometry(QtCore.QRect(10, 10, 291, 41))
        self.label_textError.setAlignment(QtCore.Qt.AlignCenter)
        self.label_textError.setObjectName(_fromUtf8("label"))
        self.button_ok = QtGui.QPushButton(self.centralwidget)
        self.button_ok.setGeometry(QtCore.QRect(110, 60, 95, 24))
        self.button_ok.setDefault(True)
        self.button_ok.setObjectName(_fromUtf8("button_ok"))
        NotFound.setCentralWidget(self.centralwidget)

        QtCore.QObject.connect(self.button_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), NotFound.close)
        QtCore.QMetaObject.connectSlotsByName(NotFound)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(404, 368)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget_date = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_date.sizePolicy().hasHeightForWidth())
        self.widget_date.setSizePolicy(sizePolicy)
        self.widget_date.setObjectName(_fromUtf8("widget_date"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_date)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_from = QtGui.QWidget(self.widget_date)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_from.sizePolicy().hasHeightForWidth())
        self.widget_from.setSizePolicy(sizePolicy)
        self.widget_from.setObjectName(_fromUtf8("widget_from"))
        self.formLayout = QtGui.QFormLayout(self.widget_from)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.timeEdit_from = QtGui.QDateTimeEdit(self.widget_from)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_from.sizePolicy().hasHeightForWidth())
        self.timeEdit_from.setSizePolicy(sizePolicy)
        self.timeEdit_from.setMinimumSize(QtCore.QSize(150, 25))
        self.timeEdit_from.setMaximumSize(QtCore.QSize(16777215, 25))
        self.timeEdit_from.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_from.setDate(QtCore.QDate(2013, 1, 1))
        self.timeEdit_from.setCalendarPopup(True)
        self.timeEdit_from.setObjectName(_fromUtf8("timeEdit_from"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.timeEdit_from)
        self.label_timeFrom = QtGui.QLabel(self.widget_from)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_timeFrom.sizePolicy().hasHeightForWidth())
        self.label_timeFrom.setSizePolicy(sizePolicy)
        self.label_timeFrom.setMinimumSize(QtCore.QSize(30, 25))
        self.label_timeFrom.setMaximumSize(QtCore.QSize(30, 25))
        self.label_timeFrom.setObjectName(_fromUtf8("label_timeFrom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_timeFrom)
        self.horizontalLayout.addWidget(self.widget_from)
        self.widget_to = QtGui.QWidget(self.widget_date)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_to.sizePolicy().hasHeightForWidth())
        self.widget_to.setSizePolicy(sizePolicy)
        self.widget_to.setObjectName(_fromUtf8("widget_to"))
        self.formLayout_3 = QtGui.QFormLayout(self.widget_to)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.timeEdit_to = QtGui.QDateTimeEdit(self.widget_to)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_to.sizePolicy().hasHeightForWidth())
        self.timeEdit_to.setSizePolicy(sizePolicy)
        self.timeEdit_to.setMinimumSize(QtCore.QSize(150, 25))
        self.timeEdit_to.setMaximumSize(QtCore.QSize(16777215, 25))
        self.timeEdit_to.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_to.setDate(QtCore.QDate(2013, 1, 1))
        self.timeEdit_to.setCalendarPopup(True)
        self.timeEdit_to.setObjectName(_fromUtf8("timeEdit_to"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.timeEdit_to)
        self.label_timeTo = QtGui.QLabel(self.widget_to)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_timeTo.sizePolicy().hasHeightForWidth())
        self.label_timeTo.setSizePolicy(sizePolicy)
        self.label_timeTo.setMinimumSize(QtCore.QSize(30, 25))
        self.label_timeTo.setMaximumSize(QtCore.QSize(30, 25))
        self.label_timeTo.setObjectName(_fromUtf8("label_timeTo"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_timeTo)
        self.horizontalLayout.addWidget(self.widget_to)
        self.gridLayout_3.addWidget(self.widget_date, 1, 0, 1, 1)
        self.widget_buttonGet = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_buttonGet.sizePolicy().hasHeightForWidth())
        self.widget_buttonGet.setSizePolicy(sizePolicy)
        self.widget_buttonGet.setObjectName(_fromUtf8("widget_buttonGet"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_buttonGet)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.button_get = QtGui.QPushButton(self.widget_buttonGet)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_get.sizePolicy().hasHeightForWidth())
        self.button_get.setSizePolicy(sizePolicy)
        self.button_get.setMinimumSize(QtCore.QSize(100, 25))
        self.button_get.setMaximumSize(QtCore.QSize(100, 25))
        self.button_get.setDefault(True)
        self.button_get.setObjectName(_fromUtf8("button_get"))
        self.gridLayout_2.addWidget(self.button_get, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_buttonGet, 2, 0, 1, 1)
        self.widget_service = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_service.sizePolicy().hasHeightForWidth())
        self.widget_service.setSizePolicy(sizePolicy)
        self.widget_service.setObjectName(_fromUtf8("widget_service"))
        self.gridLayout = QtGui.QGridLayout(self.widget_service)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_statusText = QtGui.QLabel(self.widget_service)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_statusText.sizePolicy().hasHeightForWidth())
        self.label_statusText.setSizePolicy(sizePolicy)
        self.label_statusText.setMinimumSize(QtCore.QSize(75, 25))
        self.label_statusText.setMaximumSize(QtCore.QSize(75, 25))
        self.label_statusText.setObjectName(_fromUtf8("label_statusText"))
        self.gridLayout.addWidget(self.label_statusText, 0, 0, 1, 1)
        self.label_statusService = QtGui.QLabel(self.widget_service)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_statusService.sizePolicy().hasHeightForWidth())
        self.label_statusService.setSizePolicy(sizePolicy)
        self.label_statusService.setMinimumSize(QtCore.QSize(0, 25))
        self.label_statusService.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_statusService.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_statusService.setObjectName(_fromUtf8("label_statusService"))
        self.gridLayout.addWidget(self.label_statusService, 0, 1, 1, 1)
        self.button_stopService = QtGui.QPushButton(self.widget_service)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_stopService.sizePolicy().hasHeightForWidth())
        self.button_stopService.setSizePolicy(sizePolicy)
        self.button_stopService.setMinimumSize(QtCore.QSize(80, 25))
        self.button_stopService.setMaximumSize(QtCore.QSize(80, 25))
        self.button_stopService.setDefault(True)
        self.button_stopService.setObjectName(_fromUtf8("button_stopService"))
        self.gridLayout.addWidget(self.button_stopService, 0, 3, 1, 1)
        self.button_startService = QtGui.QPushButton(self.widget_service)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_startService.sizePolicy().hasHeightForWidth())
        self.button_startService.setSizePolicy(sizePolicy)
        self.button_startService.setMinimumSize(QtCore.QSize(80, 25))
        self.button_startService.setMaximumSize(QtCore.QSize(80, 25))
        self.button_startService.setDefault(True)
        self.button_startService.setObjectName(_fromUtf8("button_startService"))
        self.gridLayout.addWidget(self.button_startService, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_service, 0, 0, 1, 1)
        self.list_commit = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_commit.sizePolicy().hasHeightForWidth())
        self.list_commit.setSizePolicy(sizePolicy)
        self.list_commit.setMinimumSize(QtCore.QSize(380, 200))
        self.list_commit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.list_commit.setFont(font)
        self.list_commit.setObjectName(_fromUtf8("list_commit"))
        self.gridLayout_3.addWidget(self.list_commit, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_main = QtGui.QMenu(self.menubar)
        self.menu_main.setObjectName(_fromUtf8("menu_main"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_configure = QtGui.QAction(MainWindow)
        self.action_configure.setObjectName(_fromUtf8("action_configure"))
        self.action_settings = QtGui.QAction(MainWindow)
        self.action_settings.setObjectName(_fromUtf8("action_settings"))
        self.action_git = QtGui.QAction(MainWindow)
        self.action_git.setObjectName(_fromUtf8("action_git"))
        self.menu_main.addAction(self.action_git)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_configure)
        self.menu_main.addAction(self.action_settings)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_main.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_startService, self.button_stopService)
        MainWindow.setTabOrder(self.button_stopService, self.timeEdit_from)
        MainWindow.setTabOrder(self.timeEdit_from, self.timeEdit_to)
        MainWindow.setTabOrder(self.timeEdit_to, self.button_get)
        MainWindow.setTabOrder(self.button_get, self.list_commit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "git2etc", None))
        self.timeEdit_from.setDisplayFormat(_translate("MainWindow", "HH:mm dd.MM.yyyy", None))
        self.label_timeFrom.setText(_translate("MainWindow", "с", None))
        self.timeEdit_to.setDisplayFormat(_translate("MainWindow", "H:mm dd.MM.yyyy", None))
        self.label_timeTo.setText(_translate("MainWindow", "по", None))
        self.button_get.setText(_translate("MainWindow", "Вывести", None))
        self.label_statusText.setText(_translate("MainWindow", "Статус:", None))
        self.label_statusService.setText(_translate("MainWindow", "(unknown)", None))
        self.button_stopService.setText(_translate("MainWindow", "Стоп", None))
        self.button_startService.setText(_translate("MainWindow", "Запуск", None))
        self.menu_main.setTitle(_translate("MainWindow", "&Меню", None))
        self.menu_help.setTitle(_translate("MainWindow", "&Справка", None))
        self.action_exit.setText(_translate("MainWindow", "&Выход", None))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.action_about.setText(_translate("MainWindow", "&О программе", None))
        self.action_configure.setText(_translate("MainWindow", "Настроить &сервис", None))
        self.action_configure.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.action_settings.setText(_translate("MainWindow", "&Настроить git2etc", None))
        self.action_settings.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.action_git.setText(_translate("MainWindow", "Работа с &git", None))
        self.action_git.setShortcut(_translate("MainWindow", "Ctrl+G", None))



def read_config(string):
    """Function to reading service configuration file"""
    config = read_settings("config")
    if (config == 0):
        return 0
    
    with open(config, 'r') as config_file:
        for line in config_file:
            if (line.split("=")[0] == "DIRECTORY"):
                directory = os.path.abspath(os.path.expanduser(str(line.split("=")[1][:-1])))
            elif (line.split("=")[0] == "TIMESLEEP"):
                timesleep = str(line.split("=")[1][:-1])
            elif (line.split("=")[0] == "IGNORELIST"):
                ignorelist = line.split("=")[1]
    
    if (string == "directory"):
        return directory
    elif (string == "timesleep"):
        return timesleep
    elif (string == "ignorelist"):
        return ignorelist


def read_settings(string):
    """Function to reading GUI configuration file"""
    config_gui = os.path.abspath(os.path.expanduser('~/.config/git2etc.conf'))
    config = "/etc/conf.d/git-etc.conf"
    editor = "gvim"
    service = "git-etc.service"
    lang = "ENG"
    
    if (os.path.exists(config_gui)):
        with open(config_gui, 'r') as config_gui_file:
            for line in config_gui_file:
                if (line.split("==")[0] == "CONFIG"):
                    config = os.path.abspath(os.path.expanduser(line.split("==")[1]))
                if (line.split("==")[0] == "EDITOR"):
                    editor = line.split("==")[1]
                if (line.split("==")[0] == "SERVICE"):
                    service = line.split("==")[1]
                if (line.split("==")[0] == "LANGUAGE"):
                    lang = line.split("==")[1]
    
    if (string == "config"):
        return config
    elif (string == "editor"):
        return editor
    elif (string == "service"):
        return service
    elif (string == "lang"):
        return lang



class AboutWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """About Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close)
        
    def keyPressEvent(self, event):
        """Esc-pressed event"""
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class CommitWindow(QtGui.QMainWindow):
    def __init__(self, parent=None, commit=None):
        """Commit Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_CommitWindow()
        self.ui.setupUi(self)
        
        self._commit = commit
        self.setWindowTitle("Commit: "+commit)
        self.set_text()

        QtCore.QObject.connect(self.ui.box_file, QtCore.SIGNAL("currentIndexChanged(int)"), self.set_diff)        
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close)
        QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.open_file)
    
    def open_file(self):
        """Function to open file in graphical editor"""
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        editor = read_settings("editor")
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        
        label = 0
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            if os.path.exists(os.path.join(path, editor)):
                label = 1
                break
        if (label == 0):
            not_found = NotFound(parent=self, text="editor")
            not_found.show()
            return
        
        filename = os.path.join(directory, str(self.ui.box_file.currentText()))
        command_line = editor+" "+filename
        os.system(command_line)
    
    def set_diff(self):
        """Function to definition file difference"""
        config = read_settings("config")
        file_name = str(self.ui.box_file.currentText())
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = "sudo git show "+self._commit+" "+file_name
        file_diff = commands.getoutput(command_line)
        
        output_text = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Monospace'; font-size:10pt; font-weight:400; font-style:normal;">"""+"\n"
        label = 0
        for line in file_diff.split("\n"):
            if (label == 1 and line[0:2] != "@@"):
                if (line[0] == "+"):
                    output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#008000;\">"+line+"</span></p>\n"
                elif (line[0] == "-"):
                    output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">"+line+"</span></p>\n"
                else:
                    output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+line+"</p>\n"
            if (line[0:3] == "---"):
                output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0000ff;\">"+line+"</span></p>\n"
            if (line[0:3] == "+++"):
                output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0000ff;\">"+line+"</span></p>\n"
                output_text = output_text+"<hr align=\"center\">\n"
                label = 1
            if (line[0:2] == "@@"):
                output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00c0c0;\">@@"+line.split("@@")[1]+"@@</span></p>\n"
                output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+line.split("@@")[2]+"</p>\n"
            if (line[0:12] == "Binary files"):
                output_text = output_text+"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0000ff;\">"+"Binary file"+"</span></p>\n"
        output_text = output_text+"</body></html>"
            
        self.ui.text_filediff.setHtml(output_text)
        os.chdir(current_directory)
    
    def set_text(self):
        """Function to insert text into CommitWindow labels"""
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = "sudo git show "+self._commit+" --name-only"
        commit_file = commands.getoutput(command_line)
        
        for line in commit_file.split("\n"):
            if (line[0:6] == "commit"):
                self.ui.label_commit.setText(line[7:])
            if (line[0:5] == "Date:"):
                self.ui.label_date.setText(line[8:])
        
        for line in commit_file.split("\n")[6:]:
            self.ui.box_file.addItem(line)
        
        os.chdir(current_directory)
        self.set_diff()
    
    def keyPressEvent(self, event):
        """Esc-pressed event"""
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class ConfigWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """Configuration Service Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_ConfigureWindow()
        self.ui.setupUi(self)
        
        self.read_config()
        
        QtCore.QObject.connect(self.ui.button_apply, QtCore.SIGNAL("clicked()"), self.setup_config)
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close_win)        
        QtCore.QObject.connect(self.ui.button_refresh, QtCore.SIGNAL("clicked()"), self.read_config)
    
    def close_win(self):
        """Function to close window"""
        self.read_config()
        self.close()
        
    def read_config(self):
        """Function to read service configuration file"""
        self.ui.lineEdit_directory.clear()
        self.ui.lineEdit_timeSleep.clear()
        self.ui.lineEdit_ignoreList.clear()
        
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        
        self.ui.lineEdit_directory.setText(read_config("directory"))
        self.ui.lineEdit_timeSleep.setText(read_config("timesleep"))
        self.ui.lineEdit_ignoreList.setText(read_config("ignorelist"))
    
    def setup_config(self):
        """Function to save service configuration"""
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        
        if (len(self.ui.lineEdit_directory.text()) == 0):
            not_found = NotFound(parent=self, text="nodir")
            not_found.show()
            return
        else:
            directory = self.ui.lineEdit_directory.text()
        
        if (len(self.ui.lineEdit_timeSleep.text()) == 0):
            not_found = NotFound(parent=self, text="notime")
            not_found.show()
            return
        else:
            if (self.ui.lineEdit_timeSleep.text().toInt()[1] == False):
                not_found = NotFound(parent=self, text="notnum")
                not_found.show()
                return
            else:
                if (self.ui.lineEdit_timeSleep.text().toInt()[0] < 1):
                    not_found = NotFound(parent=self, text="lone")
                    not_found.show()
                    return
                else:
                    timesleep = self.ui.lineEdit_timeSleep.text().toInt()[0]
        
        ignorelist = self.ui.lineEdit_ignoreList.text()
        
        with open(config, 'w') as config_file:
            config_file.write("DIRECTORY="+directory)
            config_file.write("\nTIMESLEEP="+str(timesleep))
            config_file.write("\nIGNORELIST="+ignorelist)
        
        self.close()
    
    def keyPressEvent(self, event):
        """Esc-pressed event"""
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class GitWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """Git Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_GitWindow()
        self.ui.setupUi(self)
        
        self.ui.tabWidget.setCurrentIndex(0)
        self.set_tab()
        
        QtCore.QObject.connect(self.ui.box_old, QtCore.SIGNAL("currentIndexChanged(int)"), self.setup_box_files)
        QtCore.QObject.connect(self.ui.box_typeReset, QtCore.SIGNAL("currentIndexChanged(int)"), self.reset_setup)
        QtCore.QObject.connect(self.ui.button_applyPatch, QtCore.SIGNAL("clicked()"), self.apply_patch)
        QtCore.QObject.connect(self.ui.button_browseNew, QtCore.SIGNAL("clicked()"), self.browse_new)
        QtCore.QObject.connect(self.ui.button_browseOld, QtCore.SIGNAL("clicked()"), self.browse_old)
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close_win)
        QtCore.QObject.connect(self.ui.button_createCommit, QtCore.SIGNAL("clicked()"), self.create_commit)
        QtCore.QObject.connect(self.ui.button_get, QtCore.SIGNAL("clicked()"), self.get_text)
        QtCore.QObject.connect(self.ui.button_patch, QtCore.SIGNAL("clicked()"), self.create_patch)
        QtCore.QObject.connect(self.ui.button_refresh, QtCore.SIGNAL("clicked()"), self.reset_setup)
        QtCore.QObject.connect(self.ui.button_reset, QtCore.SIGNAL("clicked()"), self.reset_commit)
        QtCore.QObject.connect(self.ui.button_status, QtCore.SIGNAL("clicked()"), self.get_status)
        QtCore.QObject.connect(self.ui.list_commit, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.commit_details)
        QtCore.QObject.connect(self.ui.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.set_tab)
        QtCore.QObject.connect(self.ui.tabWidget_merge, QtCore.SIGNAL("currentChanged(int)"), self.set_merge)
        QtCore.QObject.connect(self.ui.tabWidget_search, QtCore.SIGNAL("currentChanged(int)"), self.set_mode)
    
    def apply_patch(self):
        """Function to apply created patch in MergeTab"""
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = "sudo git apply < "+self._patch_name
        os.system(command_line)
        os.remove(self._patch_name)
        command_line = "sudo git add -A . && sudo git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        os.chdir(current_directory)
        
        self.set_tab()
    
    def browse_new(self):
        """Function to browse file in MergeTab"""
        lang = read_settings("lang")
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        if (lang == 'RUS'):
            new_file = QtGui.QFileDialog.getOpenFileName(self, u'Новый файл',directory,'Все файлы (*)')
        else:
            new_file = QtGui.QFileDialog.getOpenFileName(self, u'New file',directory,'All files (*)')
        if (len(new_file) > 0):
            self.ui.lineEdit_new.setText(new_file)
    
    def browse_old(self):
        """Function to browse file in MergeTab"""
        lang = read_settings("lang")
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        if (lang == 'RUS'):
            old_file = QtGui.QFileDialog.getOpenFileName(self, u'Старый файл',directory,'Все файлы (*)')
        else:
            old_file = QtGui.QFileDialog.getOpenFileName(self, u'Old file',directory,'All files (*)')
        if (len(old_file) > 0):
            self.ui.lineEdit_old.setText(old_file)
    
    def close_win(self):
        """Function to close window"""
        self.ui.tabWidget.setCurrentIndex(0)        
        
        self.ui.tabWidget_search.setCurrentIndex(0)
        self.ui.timeEdit_from.setDate(QtCore.QDate(2013, 1, 1))
        self.ui.timeEdit_from.setTime(QtCore.QTime(0, 0))
        self.ui.timeEdit_to.setDate(QtCore.QDate.currentDate())
        self.ui.timeEdit_to.setTime(QtCore.QTime.currentTime())
        self.ui.spinBox_times.setValue(1)
        self.ui.dateEdit_date.setDate(QtCore.QDate.currentDate())
        self.ui.list_commit.clear()
        
        self.ui.text_status.clear()
        
        self.ui.tabWidget_merge.setCurrentIndex(0)
        self.ui.box_old.clear()
        self.ui.box_new.clear()
        self.ui.lineEdit_old.clear()
        self.ui.lineEdit_new.clear()
        self.ui.button_applyPatch.setDisabled(1)
        
        self.ui.label_filename.hide()
        self.ui.box_filename.hide()        
        self.ui.box_typeReset.setCurrentIndex(0)
        self.ui.box_filename.clear()
        self.ui.lineEdit_id.clear()
        self.ui.text_reset.clear()
        
        self.close()
    
    def commit_details(self):
        """Function to show CommitWindow"""
        commit = str(self.ui.list_commit.currentItem().text())[8:15]
        
        commit_window = CommitWindow(parent=self, commit=commit)
        commit_window.show()
    
    def create_commit(self):
        """Function to create a new commit"""
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = "sudo git add -A . && sudo git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        command_line = "sudo git status --column"
        self.ui.text_status.setText(commands.getoutput(command_line))
                
        os.chdir(current_directory)
    
    def create_patch(self):
        """Function to create patch in MergeTab"""
        now = datetime.datetime.now()
        self._patch_name = os.path.abspath(os.path.expanduser('~/'))
        self._patch_name = self._patch_name+"/tmp."+str(now.hour)+str(now.minute)+str(now.second)+str(now.microsecond)+".patch"
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        editor = read_settings("editor")
        label = 0
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            if os.path.exists(os.path.join(path, editor)):
                label = 1
                break
        if (label == 0):
            not_found = NotFound(parent=self, text="editor")
            not_found.show()
            return
        
        if (self.ui.tabWidget_merge.currentIndex() == 0):
            new_file = os.path.join(directory, str(self.ui.box_new.currentText()))
            old_file = os.path.join(directory, str(self.ui.box_old.currentText()))
        elif (self.ui.tabWidget_merge.currentIndex() == 1):
            new_file = str(self.ui.lineEdit_new.text())
            old_file = str(self.ui.lineEdit_old.text())
            if ((len(new_file) == 0) or (len(old_file) == 0)):
                not_found = NotFound(parent=self, text="nofile")
                not_found.show()
                return
            fullpath_new = os.path.join(directory, new_file)
            fullpath_old = os.path.join(directory, old_file)
            if ((os.path.exists(new_file) == False) or (os.path.exists(old_file) == False) and ((os.path.exists(fullpath_new) == False) or (os.path.exists(fullpath_old) == False))):
                not_found = NotFound(parent=self, text="fnf")
                not_found.show()
                return
                    
        current_directory = os.getcwd()
        os.chdir(directory)
        os.system("sudo git checkout master > /dev/null")
        command_line = "sudo git add -A . && sudo git add -A . && sudo git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        last_commit = commands.getoutput("sudo git log -1 | grep commit | awk {'print $2'}")
        os.system("sudo git checkout experimental > /dev/null")
        command_line = "sudo cp "+old_file+" "+new_file
        os.system(command_line)
        command_line = "sudo git add -A . && sudo git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        command_line = "sudo git diff "+last_commit+" HEAD "+new_file+" > "+self._patch_name
        os.system(command_line)
        os.system("sudo git checkout master > /dev/null")
        os.system(editor+" "+self._patch_name)
        os.chdir(current_directory)
        self.ui.button_applyPatch.setEnabled(1)
    
    def get_status(self):
        """Function to get current status in git repository in StatusTab"""
        self.ui.text_status.clear()
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = "sudo git status --column"
        gitlog_file = commands.getoutput(command_line)
        self.ui.text_status.setText(gitlog_file)
                
        os.chdir(current_directory)
    
    def get_text(self):
        """Function to get commit list in SearchTab"""
        self.ui.list_commit.clear()
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        
        if (self.ui.tabWidget_search.currentIndex() == 0):
            time_now = datetime.datetime.now()        
            time_to = self.ui.timeEdit_to.dateTime().toPyDateTime()
            time_from = self.ui.timeEdit_from.dateTime().toPyDateTime()
            time_interval_to = time_now - time_to
            time_interval_from = time_now - time_from
            
            # [days, hours, minutes]
            # ti[t/f] = time_interval_[to/from]
            tit = [str(time_interval_to.days), str((time_interval_to.seconds-(time_interval_to.seconds%3600))/3600), str(((time_interval_to.seconds%3600)-(time_interval_to.seconds%3600)%60)/60)]       
            tif = [str(time_interval_from.days), str((time_interval_from.seconds-(time_interval_from.seconds%3600))/3600), str(((time_interval_from.seconds%3600)-(time_interval_from.seconds%3600)%60)/60)]
        
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = "sudo git log --oneline "
            command_line = command_line+"--since=\""+tif[0]+" days "+tif[1]+" hours "+tif[2]+" minutes\" "
            command_line = command_line+"--until=\""+tit[0]+" days "+tit[1]+" hours "+tit[2]+" minutes\" "
            gitlog_file = commands.getoutput(command_line)
        elif (self.ui.tabWidget_search.currentIndex() == 1):
            times = str(self.ui.spinBox_times.value())
            
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = "sudo git log --oneline -"+times
            gitlog_file = commands.getoutput(command_line)
        elif (self.ui.tabWidget_search.currentIndex() == 2):
            date_now = datetime.date.today()        
            date_interval = date_now - self.ui.dateEdit_date.date().toPyDate()
        
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = "sudo git log --oneline "
            command_line = command_line+"--since=\""+str(date_interval.days+1)+" days\" "
            command_line = command_line+"--until=\""+str(date_interval.days)+" days\""
            gitlog_file = commands.getoutput(command_line)

        if (len(gitlog_file) == 0):
            not_found = NotFound(parent=self, text="commitnf")
            not_found.show()
            os.chdir(current_directory)
            return
        
        for line in gitlog_file.split("\n"):
            output_line = "Commit: "+line[0:7]
            output_line = output_line+". Date: "+line[8:12]+"-"+line[12:14]+"-"+line[14:16]
            output_line = output_line+" "+line[16:18]+":"+line[18:20]
            self.ui.list_commit.addItem(output_line)
            
        os.chdir(current_directory)
    
    def reset_commit(self):
        """Function to reset commit (or file changes) in ResetTab"""
        self.ui.text_reset.clear()
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        if (len(str(self.ui.lineEdit_id.text())) < 7):
            not_found = NotFound(parent=self, text="id")
            not_found.show()
            self.ui.lineEdit_id.clear()
            self.ui.box_typeReset.setCurrentIndex(0)
            return
        else:
            commit = str(self.ui.lineEdit_id.text())
        
        current_directory = os.getcwd()
        os.chdir(directory)
        
        if (self.ui.box_typeReset.currentIndex() == 0):
            command_line = "sudo git log --oneline"
            list_commit = commands.getoutput(command_line)
            command_line = "sudo git reset --hard "+commit
            output = commands.getoutput(command_line)
            
            self.ui.lineEdit_id.clear()
            if (output[0:6] == "fatal:"):
                not_found = NotFound(parent=self, text="commitnf")
                not_found.show()
                os.chdir(current_directory)
                return
            
            self.ui.text_reset.setText(list_commit+"/n/n"+output)
        elif (self.ui.box_typeReset.currentIndex() == 1):
            filename = str(self.ui.box_filename.currentText())
            now = datetime.datetime.now()
            patch = "tmp."+str(now.hour)+str(now.minute)+str(now.second)+str(now.microsecond)+".patch"
            
            self.ui.text_reset.setText("[II] Creating commit")
            command_line = "sudo git add -A . && sudo git commit -m `date +%Y%m%d%H%M%S-%N`"
            output = commands.getoutput(command_line)
            self.ui.text_reset.append(output)
            
            self.ui.text_reset.append("[II] Creating patch")
            command_line = "sudo git diff HEAD "+commit+" "+filename+" > "+patch
            os.system(command_line)
            
            self.ui.text_reset.append("[II] Patching")
            command_line = "sudo git apply < "+patch
            output = commands.getoutput(command_line)
            os.remove(patch)
            self.ui.text_reset.append(output+"[II] Done!")
            
            self.ui.text_reset.append("[II] Creating commit")
            command_line = "sudo git add -A . && sudo git commit -m `date +%Y%m%d%H%M%S-%N`"
            output = commands.getoutput(command_line)
            self.ui.text_reset.append(output)
            
            self.ui.lineEdit_id.clear()
            self.ui.box_filename.clear()
            self.ui.box_typeReset.setCurrentIndex(0)
        
        os.chdir(current_directory)
            
    def reset_setup(self):
        """Function to setup text in ResetTab"""
        self.ui.box_filename.clear()
        
        if (self.ui.box_typeReset.currentIndex() == 0):
            self.ui.box_filename.hide()
            self.ui.label_filename.hide()
        elif (self.ui.box_typeReset.currentIndex() == 1):
            config = read_settings("config")
            if (os.path.exists(config) == False):
                not_found = NotFound(parent=self, text="conf")
                not_found.show()
                self.ui.lineEdit_id.clear()
                self.ui.box_typeReset.setCurrentIndex(0)
                return
            directory = read_config("directory")        
            if (os.path.exists(directory) == False):
                not_found = NotFound(parent=self, text="dir")
                not_found.show()
                self.ui.lineEdit_id.clear()
                self.ui.box_typeReset.setCurrentIndex(0)
                return
            if (os.path.exists(directory+"/.git") == False):
                not_found = NotFound(parent=self, text="gitdir")
                not_found.show()
                self.ui.lineEdit_id.clear()
                self.ui.box_typeReset.setCurrentIndex(0)
                return
            if (len(str(self.ui.lineEdit_id.text())) < 7):
                not_found = NotFound(parent=self, text="id")
                not_found.show()
                
                self.ui.lineEdit_id.clear()
                self.ui.box_typeReset.setCurrentIndex(0)
                
                return
            else:
                commit = str(self.ui.lineEdit_id.text())
            
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = "sudo git show "+commit+" --name-only"
            commit_file = commands.getoutput(command_line)
            
            if (commit_file[0:6] == "fatal:"):
                not_found = NotFound(parent=self, text="commitnf")
                not_found.show()
                os.chdir(current_directory)
                self.ui.lineEdit_id.clear()
                self.ui.box_typeReset.setCurrentIndex(0)
                return
            
            for line in commit_file.split("\n")[6:]:
                self.ui.box_filename.addItem(line)
            
            os.chdir(current_directory)
            
            self.ui.box_filename.show()
            self.ui.label_filename.show()
    
    def setup_box_files(self):
        """Function to set active file in MergeTab"""
        current_item = str(self.ui.box_old.currentText())
        if ((current_item[-7:] == ".pacnew") or (current_item[-8:] == ".pacsave") or (current_item[-8:] == ".pacorig") or (current_item[-4:] == ".new") or (current_item[-4:] == ".old") or (current_item[-5:] == ".bckp") or (current_item[-4:] == ".bak")):
            current_item = '.'.join(current_item.split('.')[:-1])
            index = self.ui.box_new.findText(current_item)
            self.ui.box_new.setCurrentIndex(index)
    
    def set_merge(self):
        """Function to setup text in MergeTab"""
        if (self.ui.tabWidget_merge.currentIndex() == 0):            
            self.ui.box_new.clear()
            self.ui.box_old.clear()
            config = read_settings("config")
            if (os.path.exists(config) == False):
                not_found = NotFound(parent=self, text="conf")
                not_found.show()
                return
            directory = read_config("directory")        
            if (os.path.exists(directory) == False):
                not_found = NotFound(parent=self, text="dir")
                not_found.show()
                return
            if (os.path.exists(directory+"/.git") == False):
                not_found = NotFound(parent=self, text="gitdir")
                not_found.show()
                return
            command_line = "sudo ls -lARp --format=single-column "+directory
            list_files = commands.getoutput(command_line)
            preffix = directory
            for files in list_files.split("\n"):
                if (files != ""):
                    if (files[-1] != "/"):
                        if (files[0] == "/"):
                            preffix = files[:-1]+"/"
                        else:
                            if ((files[-7:] == ".pacnew") or (files[-8:] == ".pacsave") or (files[-8:] == ".pacorig") or (files[-4:] == ".new") or (files[-4:] == ".old") or (files[-5:] == ".bckp") or (files[-4:] == ".bak")):
                                line = preffix + files
                                output = line.replace(directory, "")[1:]
                                self.ui.box_new.addItem(output)
                                self.ui.box_old.addItem(output)
                                output = '.'.join(output.split('.')[:-1])
                                self.ui.box_new.addItem(output)
                                self.ui.box_old.addItem(output)
            
            self.setup_box_files()
        elif (self.ui.tabWidget_merge.currentIndex() == 1):
            self.ui.lineEdit_old.clear()
            self.ui.lineEdit_new.clear()
    
    def set_mode(self):
        """Function to set mode in SearchTab"""
        self.ui.list_commit.clear()
        if (self.ui.tabWidget_search.currentIndex() == 0):
            self.ui.timeEdit_from.setDate(QtCore.QDate(2013, 1, 1))
            self.ui.timeEdit_from.setTime(QtCore.QTime(0, 0))
            self.ui.timeEdit_to.setDate(QtCore.QDate.currentDate())
            self.ui.timeEdit_to.setTime(QtCore.QTime.currentTime())
        elif (self.ui.tabWidget_search.currentIndex() == 1):
            self.ui.spinBox_times.setValue(1)            
        elif (self.ui.tabWidget_search.currentIndex() == 2):            
            self.ui.dateEdit_date.setDate(QtCore.QDate.currentDate())
    
    def set_tab(self):
        """Function to set tab"""
        if (self.ui.tabWidget.currentIndex() == 0):
            self.ui.tabWidget.setCurrentIndex(0)
            self.set_mode()
        elif (self.ui.tabWidget.currentIndex() == 1):
            self.ui.text_status.clear()
        elif (self.ui.tabWidget.currentIndex() == 2):
            self.ui.button_applyPatch.setDisabled(1)
            self.ui.tabWidget_merge.setCurrentIndex(0)
            self.set_merge()
        elif (self.ui.tabWidget.currentIndex() == 3):
            self.ui.box_typeReset.setCurrentIndex(0)
            self.ui.label_filename.hide()
            self.ui.box_filename.hide()
            self.ui.box_filename.clear()
            self.ui.lineEdit_id.clear()
            self.ui.text_reset.clear()
    
    def keyPressEvent(self, event):
        """Esc-pressed event"""
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class NotFound(QtGui.QMainWindow):
    def __init__(self, parent=None, text=None):
        """Error Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_NotFound()
        self.ui.setupUi(self)
        
        self.load_text(text)

    def load_text(self, text):
        """Function to setup text in window"""
        lang = read_settings("lang")
        if (lang == "RUS"):
            self.setWindowTitle(u"Ошибка!")
            self.ui.button_ok.setText(u"Ok")
            if (text == "commitnf"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанные коммиты не найдены</p></body></html>")
            elif (text == "conf"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанный файл настроек не существует</p></body></html>")
            elif (text == "dir"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанная директория не существует</p></body></html>")
            elif (text == "editor"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанного редактора не существует</p></body></html>")
            elif (text == "fnf"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанный файл не найден</p></body></html>")
            elif (text == "gitdir"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Git репозиторий не найден</p></body></html>")
            elif (text == "id"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Задан слишком короткий идентификатор</p></body></html>")
            elif (text == "lone"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанное значение меньше 1</p></body></html>")
            elif (text == "noconfig"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Не указано имя файла с настройками</p></body></html>")
            elif (text == "nodir"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Не указана рабочая директория</p></body></html>")
            elif (text == "noeditor"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Не указан текстовый редактор</p></body></html>")
            elif (text == "nofile"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Файл не указан</p></body></html>")
            elif (text == "noservice"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Не указано имя сервиса</p></body></html>")
            elif (text == "notime"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Не указан интервал обновления</p></body></html>")
            elif (text == "notnum"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанное значение не число</p></body></html>")
            else:
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Неизвестная ошибка</p></body></html>")


class SettingsWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """GUI Settings Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        
        self._parent = parent        
        self.set_text()
        
        QtCore.QObject.connect(self.ui.button_apply, QtCore.SIGNAL("clicked()"), self.save_config)
        QtCore.QObject.connect(self.ui.button_browse, QtCore.SIGNAL("clicked()"), self.browse_config)
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close_win)
        QtCore.QObject.connect(self.ui.button_default, QtCore.SIGNAL("clicked()"), self.create_config)
    
    def browse_config(self):
        """Function to browse service configuration file"""
        lang = read_settings("lang")
        if (lang == 'RUS'):
            config = QtGui.QFileDialog.getOpenFileName(self, u'Configuration file','','Все файлы (*)')
        else:
            config = QtGui.QFileDialog.getOpenFileName(self, u'Файл настроек','','All files (*)')
        if (len(config) > 0):
            self.ui.lineEdit_config.setText(config)
    
    def close_win(self):
        """Function to close window"""
        self.set_text()
        self.close()
    
    def create_config(self):
        """Function to create default configuration file"""
        self.ui.lineEdit_service.setText("git-etc.service")
        self.ui.lineEdit_config.setText("/etc/conf.d/git-etc.conf")
        self.ui.lineEdit_editor.setText("gvim")
        self.ui.box_lang.setCurrentIndex(0)
        
        self.save_config()
    
    def save_config(self):
        """Function to save configuration file"""
        config_gui = os.path.abspath(os.path.expanduser('~/.config/git2etc.conf'))
        if (os.path.exists(config_gui)):
            os.remove(config_gui)
        
        if (len(self.ui.lineEdit_service.text()) == 0):
            not_found = NotFound(parent=self, text="noservice")
            not_found.show()
            return
        else:
            service = self.ui.lineEdit_service.text()
        if (len(self.ui.lineEdit_config.text()) == 0):
            not_found = NotFound(parent=self, text="noconfig")
            not_found.show()
            return
        else:
            config = self.ui.lineEdit_config.text()
        if (len(self.ui.lineEdit_editor.text()) == 0):
            not_found = NotFound(parent=self, text="noeditor")
            not_found.show()
            return
        else:
            editor = self.ui.lineEdit_editor.text()
        
        with open(config_gui, 'w') as config_gui_file:
            config_gui_file.write("SERVICE=="+service+"==\n")
            config_gui_file.write("CONFIG=="+config+"==\n")
            config_gui_file.write("EDITOR=="+editor+"==\n")
            if (self.ui.box_lang.currentIndex() == 0):
                config_gui_file.write("LANGUAGE==ENG==\n")
            else:
                config_gui_file.write("LANGUAGE==RUS==\n")
        
        self._parent.set_status()
        self._parent.ui.list_commit.clear()
        self.close()

    def set_text(self):
        """Function to load configuration file"""
        config_gui = os.path.abspath(os.path.expanduser('~/.config/git2etc.conf'))
        if (os.path.exists(config_gui)):
            self.ui.lineEdit_service.setText(read_settings("service"))
            self.ui.lineEdit_config.setText(read_settings("config"))
            self.ui.lineEdit_editor.setText(read_settings("editor"))
            if (read_settings("lang") == "RUS"):
                self.ui.box_lang.setCurrentIndex(1)
            else:
                self.ui.box_lang.setCurrentIndex(0)
        else:
            self.create_config()
    
    def keyPressEvent(self, event):
        """Ecs-pressed event"""
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """Main Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setup()
        self.set_status()
        self.ui.timeEdit_to.setDate(QtCore.QDate.currentDate())
        self.ui.timeEdit_to.setTime(QtCore.QTime.currentTime())
        
        about_window = AboutWindow(parent=self)
        config_window = ConfigWindow(parent=self)
        git_window = GitWindow(parent=self)
        settings_window = SettingsWindow(parent=self)
        
        QtCore.QObject.connect(self.ui.action_about, QtCore.SIGNAL("triggered()"), about_window.show)
        QtCore.QObject.connect(self.ui.action_configure, QtCore.SIGNAL("triggered()"), config_window.show)
        QtCore.QObject.connect(self.ui.action_git, QtCore.SIGNAL("triggered()"), git_window.show)
        QtCore.QObject.connect(self.ui.action_settings, QtCore.SIGNAL("triggered()"), settings_window.show)
        QtCore.QObject.connect(self.ui.action_exit, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.ui.button_get, QtCore.SIGNAL("clicked()"), self.get_text)
        QtCore.QObject.connect(self.ui.button_startService, QtCore.SIGNAL("clicked()"), self.start_service)
        QtCore.QObject.connect(self.ui.button_stopService, QtCore.SIGNAL("clicked()"), self.stop_service)
        QtCore.QObject.connect(self.ui.list_commit, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.commit_details)
    
    def commit_details(self):
        """Function to show CommitWindow"""
        commit = str(self.ui.list_commit.currentItem().text())[8:15]
        
        commit_window = CommitWindow(parent=self, commit=commit)
        commit_window.show()
    
    def get_text(self):
        """Function to get commit list"""
        self.ui.list_commit.clear()
        config = read_settings("config")
        if (os.path.exists(config) == False):
            not_found = NotFound(parent=self, text="conf")
            not_found.show()
            return
        directory = read_config("directory")        
        if (os.path.exists(directory) == False):
            not_found = NotFound(parent=self, text="dir")
            not_found.show()
            return
        if (os.path.exists(directory+"/.git") == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
                
        time_now = datetime.datetime.now()        
        time_to = self.ui.timeEdit_to.dateTime().toPyDateTime()
        time_from = self.ui.timeEdit_from.dateTime().toPyDateTime()
        time_interval_to = time_now - time_to
        time_interval_from = time_now - time_from
        
        # [days, hours, minutes]
        # ti[t/f] = time_interval_[to/from]
        tit = [str(time_interval_to.days), str((time_interval_to.seconds-(time_interval_to.seconds%3600))/3600), str(((time_interval_to.seconds%3600)-(time_interval_to.seconds%3600)%60)/60)]       
        tif = [str(time_interval_from.days), str((time_interval_from.seconds-(time_interval_from.seconds%3600))/3600), str(((time_interval_from.seconds%3600)-(time_interval_from.seconds%3600)%60)/60)]
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = "sudo git log --oneline "
        command_line = command_line+"--since=\""+tif[0]+" days "+tif[1]+" hours "+tif[2]+" minutes\" "
        command_line = command_line+"--until=\""+tit[0]+" days "+tit[1]+" hours "+tit[2]+" minutes\" "
        gitlog_file = commands.getoutput(command_line)
        
        if (len(gitlog_file) == 0):
            not_found = NotFound(parent=self, text="commitnf")
            not_found.show()
            os.chdir(current_directory)
            return
      
        for line in gitlog_file.split("\n"):
            output_line = "Commit: "+line[0:7]
            output_line = output_line+". Date: "+line[8:12]+"-"+line[12:14]+"-"+line[14:16]
            output_line = output_line+" "+line[16:18]+":"+line[18:20]
            self.ui.list_commit.addItem(output_line)
               
        os.chdir(current_directory)
    
    def set_status(self):
        """Function to set service status"""
        service = read_settings("service")
        
        command_line = "systemctl status "+service+" | grep Active" 
        status_service = ' '.join(commands.getoutput(command_line).split()[1:3])
        
        self.ui.label_statusService.setText(status_service)
    
    def setup(self):
        """Function to create configuration file if it doesn't exists"""
        config_gui = os.path.abspath(os.path.expanduser('~/.config/git2etc.conf'))
        if (os.path.exists(config_gui)):
            return
        
        with open(config_gui, 'w') as config_gui_file:
            config_gui_file.write("# Automatically generated by git2etc\n")
            config_gui_file.write("SERVICE==git-etc.service==\n")
            config_gui_file.write("CONFIG==/etc/conf.d/git-etc.conf==\n")
            config_gui_file.write("EDITOR==gvim==\n")
            config_gui_file.write("LANGUAGE==ENG==\n")
    
    def start_service(self):
        """Function to start service"""
        service = read_settings("service")
        
        command_line = "sudo systemctl start "+service
        os.system(command_line)
        self.set_status()
    
    def stop_service(self):
        """Function to stop service"""
        service = read_settings("service")
        
        command_line = "sudo systemctl stop "+service
        os.system(command_line)
        self.set_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='GUI interface for git-etc daemon', 
            epilog='See "man 1 git2etc" for more details')
    parser.add_argument('-v','--version', dest='ver',
            help = 'Show version and exit',
            action='store_true', default = False)
    parser.add_argument('--default', dest='createDefault',
            help = 'Create default configuration file',
            action='store_true', default = False)
    
    args = parser.parse_args()
    if (args.ver):
        print ("                          git2etc")
        print ("GUI interface for git-etc daemon to work with GIT repository")
        print ("Version : 2.0                                  License : GPL")
        print ("                                                  by arcanis")
        print ("                                E-mail : esalexeev@gmail.com")
        sys.exit()
    if (args.createDefault):
        config_gui = os.path.abspath(os.path.expanduser('~/.config/git2etc.conf'))
        if (os.path.exists(config_gui)):
            os.remove(config_gui)
    
    app = QtGui.QApplication(sys.argv)
    codec = QtCore.QTextCodec.codecForName("UTF-8")
    QtCore.QTextCodec.setCodecForCStrings(codec)
    
    git2etc = MainWindow()
    git2etc.show()
    sys.exit(app.exec_())