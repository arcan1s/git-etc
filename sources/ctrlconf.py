#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Do not touch!
# Magick!

 
import argparse, commands, datetime, os, sys
from PyQt4 import QtCore, QtGui

from ctrlconf.aboutwin import Ui_AboutWindow
from ctrlconf.commitwin import Ui_CommitWindow
from ctrlconf.configwin import Ui_ConfigureWindow
from ctrlconf.gitwin import Ui_GitWindow
from ctrlconf.settingswin import Ui_SettingsWindow
from ctrlconf.mainwin import Ui_MainWindow
from ctrlconf.notfound import Ui_NotFound


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
    config_gui = os.path.abspath(os.path.expanduser('~/.config/ctrlconf.conf'))
    config = "/etc/conf.d/git-etc.conf"
    editor = "gvim"
    service = "git-etc.service"
    lang = "ENG"
    sudo = "sudo "
    
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
                if (line.split("==")[0] == "SUDO"):
                    if (line.split("==")[1] == "NO"):
                        sudo = ""
    
    if (string == "config"):
        return config
    elif (string == "editor"):
        return editor
    elif (string == "service"):
        return service
    elif (string == "lang"):
        return lang
    elif (string == "sudo"):
        return sudo



class AboutWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """About Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)
        
        self.load_text()
        
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close)
    
    def load_text(self):
        """Function to load text"""
        lang = read_settings("lang")
        self.setWindowTitle(_translate("AboutWindow", "About", None))
        if (lang == "RUS"):
            self.ui.button_close.setText(_translate("AboutWindow", "Закрыть", None))
            self.ui.text_about.setHtml(_translate("AboutWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Control Config 2.2.2</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Лицензия: GPL</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GUI к демону git-etc, написанный на Python2.7/PyQt4. Позволяет посмотреть список коммитов и изменения в файлах, записанные в коммитах. Также данное приложение позволяет откатить к определенному коммиту все файлы (git reset --hard) или отдельно взятые (git diff &amp;&amp; git apply). Дополнительно предусмотрена возможность слияния старых и новых конфигурационных файлов (используются две ветки репозитория - master и experimental).</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор: Евгений Алексеев aka arcanis</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: esalexeev@gmail.com</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jabber: arcanis@jabber.ru</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ICQ: 407-398-235</p></body></html>", None))
        else:
            self.ui.button_close.setText(_translate("AboutWindow", "Close", None))
            self.ui.text_about.setHtml(_translate("AboutWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Control Config 2.2.2</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License: GPL</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Control Config is GUI for git-etc daemon written on Python2.7/PyQt4. This application allows you to view a list of commits and changes to files recorded in commit messages. Also, this application allows you to roll back to a specific commit all files (git reset --hard) or individual files (git diff && git apply). You may merge old and new configuration files (used two branches repository - master and experimental).</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author: Evgeniy Alexeev aka arcanis</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: esalexeev@gmail.com</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jabber: arcanis@jabber.ru</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ICQ: 407-398-235</p></body></html>", None))
        
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
        
        self.load_text()
        self._commit = commit
        self.setWindowTitle("Commit: "+commit)
        self.set_text()

        QtCore.QObject.connect(self.ui.box_file, QtCore.SIGNAL("currentIndexChanged(int)"), self.set_diff)        
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close)
        QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.open_file)
    
    def load_text(self):
        """Function to load text"""
        lang = read_settings("lang")
        self.setWindowTitle(_translate("CommitWindow", "Commit: ", None))
        self.ui.label_date_name.setText(_translate("CommitWindow", "Date:", None))
        self.ui.text_filediff.setHtml(_translate("CommitWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.ui.label_commit_name.setText(_translate("CommitWindow", "Commit:", None))
        self.ui.label_commit.setText(_translate("CommitWindow", "(unknown)", None))
        self.ui.label_date.setText(_translate("CommitWindow", "(unknown)", None))
        self.ui.label_file_name.setText(_translate("CommitWindow", "File:", None))
        if (lang == "RUS"):
            self.ui.button_close.setText(_translate("CommitWindow", "Закрыть", None))
            self.ui.button_open.setText(_translate("CommitWindow", "Открыть в редакторе", None))
        else:
            self.ui.button_close.setText(_translate("CommitWindow", "Close", None))
            self.ui.button_open.setText(_translate("CommitWindow", "Open in editor", None))
    
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
        sudo = read_settings("sudo")
        
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
        command_line = sudo+editor+" "+filename
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = sudo+"git show "+self._commit+" "+file_name
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = sudo+"git show "+self._commit+" --name-only"
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
        
        self.load_text()
        self.read_config()
        
        QtCore.QObject.connect(self.ui.button_apply, QtCore.SIGNAL("clicked()"), self.setup_config)
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close_win)        
        QtCore.QObject.connect(self.ui.button_refresh, QtCore.SIGNAL("clicked()"), self.read_config)
    
    def close_win(self):
        """Function to close window"""
        self.read_config()
        self.close()
    
    def load_text(self):
        """Function to load text"""
        lang = read_settings("lang")
        if (lang == "RUS"):
            self.setWindowTitle(_translate("ConfigureWindow", "Настроить сервис", None))
            self.ui.label_directory.setText(_translate("ConfigureWindow", "Рабочая директория:", None))
            self.ui.button_refresh.setText(_translate("ConfigureWindow", "Обновить", None))
            self.ui.button_close.setText(_translate("ConfigureWindow", "Закрыть", None))
            self.ui.button_apply.setText(_translate("ConfigureWindow", "Применить", None))
            self.ui.label_timeSleep.setText(_translate("ConfigureWindow", "Интервал обновления, ч:", None))
            self.ui.label_ignoreList.setText(_translate("ConfigureWindow", "Список игнорируемых файлов:", None))
        else:
            self.setWindowTitle(_translate("ConfigureWindow", "Configure service", None))
            self.ui.label_directory.setText(_translate("ConfigureWindow", "Working directory:", None))
            self.ui.button_refresh.setText(_translate("ConfigureWindow", "Refresh", None))
            self.ui.button_close.setText(_translate("ConfigureWindow", "Close", None))
            self.ui.button_apply.setText(_translate("ConfigureWindow", "Apply", None))
            self.ui.label_timeSleep.setText(_translate("ConfigureWindow", "Time interval, hours:", None))
            self.ui.label_ignoreList.setText(_translate("ConfigureWindow", "Ignore list:", None))
        
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
        
        self.load_text()
        self.ui.tabWidget.setCurrentIndex(0)
        self.set_tab()
        
        QtCore.QObject.connect(self.ui.box_file, QtCore.SIGNAL("currentIndexChanged(int)"), self.showOneFile)
        QtCore.QObject.connect(self.ui.box_old, QtCore.SIGNAL("currentIndexChanged(int)"), self.setup_box_files)
        QtCore.QObject.connect(self.ui.box_typeReset, QtCore.SIGNAL("currentIndexChanged(int)"), self.reset_setup)
        QtCore.QObject.connect(self.ui.button_addIgnore, QtCore.SIGNAL("clicked()"), self.add_ignore)
        QtCore.QObject.connect(self.ui.button_applyIgnore, QtCore.SIGNAL("clicked()"), self.apply_ignore)
        QtCore.QObject.connect(self.ui.button_applyPatch, QtCore.SIGNAL("clicked()"), self.apply_patch)
        QtCore.QObject.connect(self.ui.button_browseNew, QtCore.SIGNAL("clicked()"), self.browse_new)
        QtCore.QObject.connect(self.ui.button_browseOld, QtCore.SIGNAL("clicked()"), self.browse_old)
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close_win)
        QtCore.QObject.connect(self.ui.button_createCommit, QtCore.SIGNAL("clicked()"), self.create_commit)
        QtCore.QObject.connect(self.ui.button_deleteIgnore, QtCore.SIGNAL("clicked()"), self.delete_ignore)
        QtCore.QObject.connect(self.ui.button_get, QtCore.SIGNAL("clicked()"), self.get_text)
        QtCore.QObject.connect(self.ui.button_patch, QtCore.SIGNAL("clicked()"), self.create_patch)
        QtCore.QObject.connect(self.ui.button_refresh, QtCore.SIGNAL("clicked()"), self.reset_setup)
        QtCore.QObject.connect(self.ui.button_refreshIgnore, QtCore.SIGNAL("clicked()"), self.refresh_ignore)
        QtCore.QObject.connect(self.ui.button_reset, QtCore.SIGNAL("clicked()"), self.reset_commit)
        QtCore.QObject.connect(self.ui.button_status, QtCore.SIGNAL("clicked()"), self.get_status)
        QtCore.QObject.connect(self.ui.list_commit, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.commit_details)
        QtCore.QObject.connect(self.ui.list_commit_oneFile, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.commit_oneFile_details)
        QtCore.QObject.connect(self.ui.list_ignoreList, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.ui.list_ignoreList.openPersistentEditor)
        QtCore.QObject.connect(self.ui.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.set_tab)
        QtCore.QObject.connect(self.ui.tabWidget_merge, QtCore.SIGNAL("currentChanged(int)"), self.set_merge)
        QtCore.QObject.connect(self.ui.tabWidget_search, QtCore.SIGNAL("currentChanged(int)"), self.set_mode)
    
    def add_ignore(self):
        """Function to add new string in ignore-list"""
        if (self.ui.lineEdit_addIgnore.text().length() == 0):
            not_found = NotFound(parent=self, text="nofile")
            not_found.show()
            return
        else:
            new_item = self.ui.lineEdit_addIgnore.text()
            self.ui.list_ignoreList.addItem(new_item)
            self.ui.lineEdit_addIgnore.clear()
    
    def apply_ignore(self):
        """Function to save ignore list"""
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        items = []
        for item in range(self.ui.list_ignoreList.count()):
            if (self.ui.list_ignoreList.isItemHidden(self.ui.list_ignoreList.item(item)) == False):
                items = items + str(self.ui.list_ignoreList.item(item).text()).split("\n")
        items = '\n'.join(items)
        
        command_line = sudo+"sh -c \"echo \'"+items+"\' > "+os.path.join(directory, ".git/info/exclude")+"\""
        os.system(command_line)
        self.refresh_ignore
    
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = sudo+"git apply < "+self._patch_name
        os.system(command_line)
        os.remove(self._patch_name)
        command_line = sudo+"git add -A . && "+sudo+"git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
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
        
        self.ui.box_file.clear()
        self.ui.list_commit_oneFile.clear()
        
        self.ui.text_status.clear()
        
        self.ui.list_ignoreList.clear()
        
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
    
    def commit_oneFile_details(self):
        """Function to show CommitWindow"""
        commit = str(self.ui.list_commit_oneFile.currentItem().text())[8:15]
        
        commit_window = CommitWindow(parent=self, commit=commit)
        commit_window.show()
    
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = sudo+"git add -A . && "+sudo+"git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        command_line = sudo+"git status --column"
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
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
        sudo = read_settings("sudo")
        
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
        os.system(sudo+"git checkout master > /dev/null")
        command_line = sudo+"git add -A . && "+sudo+"git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        last_commit = commands.getoutput(sudo+"git log -1 | grep commit | awk {'print $2'}")
        os.system(sudo+"git checkout experimental > /dev/null")
        command_line = sudo+"cp "+old_file+" "+new_file
        os.system(command_line)
        command_line = sudo+"git add -A . && "+sudo+"git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        command_line = sudo+"git diff "+last_commit+" HEAD "+new_file+" > "+self._patch_name
        os.system(command_line)
        os.system(sudo+"git checkout master > /dev/null")
        os.system(editor+" "+self._patch_name)
        os.chdir(current_directory)
        self.ui.button_applyPatch.setEnabled(1)
    
    def delete_ignore(self):
        """Function to delete items in ignore list"""
        delete_item = self.ui.list_ignoreList.currentItem()
        self.ui.list_ignoreList.setItemHidden(delete_item, True)
    
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
        current_directory = os.getcwd()
        os.chdir(directory)
        command_line = sudo+"git status --column"
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
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
            command_line = sudo+"git log --oneline "
            command_line = command_line+"--since=\""+tif[0]+" days "+tif[1]+" hours "+tif[2]+" minutes\" "
            command_line = command_line+"--until=\""+tit[0]+" days "+tit[1]+" hours "+tit[2]+" minutes\" "
            gitlog_file = commands.getoutput(command_line)
        elif (self.ui.tabWidget_search.currentIndex() == 1):
            times = str(self.ui.spinBox_times.value())
            
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = sudo+"git log --oneline -"+times
            gitlog_file = commands.getoutput(command_line)
        elif (self.ui.tabWidget_search.currentIndex() == 2):
            date_now = datetime.date.today()        
            date_interval = date_now - self.ui.dateEdit_date.date().toPyDate()
        
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = sudo+"git log --oneline "
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
    
    def load_text(self):
        """Function to load text"""
        lang = read_settings("lang")
        self.ui.timeEdit_from.setDisplayFormat(_translate("GitWindow", "HH:mm dd.MM.yyyy", None))
        self.ui.timeEdit_to.setDisplayFormat(_translate("GitWindow", "H:mm dd.MM.yyyy", None))
        self.ui.dateEdit_date.setDisplayFormat(_translate("GitWindow", "dd.MM.yyyy", None))
        if (lang == "RUS"):
            self.setWindowTitle(_translate("GitWindow", "Работа с git", None))
            self.ui.button_close.setText(_translate("GitWindow", "Закрыть", None))
            self.ui.label_timeFrom.setText(_translate("GitWindow", "с", None))
            self.ui.label_timeTo.setText(_translate("GitWindow", "по", None))
            self.ui.label_titleInt.setText(_translate("GitWindow", "В указанный интервал", None))
            self.ui.tabWidget_search.setTabText(self.ui.tabWidget_search.indexOf(self.ui.tab_search_01), _translate("GitWindow", "В интервал", None))
            self.ui.label_times.setText(_translate("GitWindow", "Число коммитов", None))
            self.ui.label_titleTimes.setText(_translate("GitWindow", "По количеству коммитов", None))
            self.ui.tabWidget_search.setTabText(self.ui.tabWidget_search.indexOf(self.ui.tab_search_02), _translate("GitWindow", "По числу коммитов", None))
            self.ui.label_date.setText(_translate("GitWindow", "Дата коммита", None))
            self.ui.label_titleDate.setText(_translate("GitWindow", "По дате коммита", None))
            self.ui.tabWidget_search.setTabText(self.ui.tabWidget_search.indexOf(self.ui.tab_search_03), _translate("GitWindow", "По дате", None))
            self.ui.button_get.setText(_translate("GitWindow", "Вывести", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_search), _translate("GitWindow", "Поиск", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_oneFile), _translate("GitWindow", "Изменения в файле", None))
            self.ui.button_createCommit.setText(_translate("GitWindow", "Создать коммит", None))
            self.ui.button_status.setText(_translate("GitWindow", "Показать статус", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_status), _translate("GitWindow", "Статус", None))
            self.ui.button_refreshIgnore.setText(_translate("GitWindow", "Обновить", None))
            self.ui.button_addIgnore.setText(_translate("GitWindow", "Добавить", None))
            self.ui.button_deleteIgnore.setText(_translate("GitWindow", "Удалить строку", None))
            self.ui.button_applyIgnore.setText(_translate("GitWindow", "Применить", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_ignore), _translate("GitWindow", "Игнор-лист", None))
            self.ui.label_merge.setText(_translate("GitWindow", "<html><head/><body><p align=\"center\">Изменения будут применены от <span style=\" font-weight:600; color:#ff0000;\">СТАРОГО</span> файла к <span style=\" font-weight:600; color:#ff0000;\">НОВОМУ</span>.</p><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">НОВЫЙ</span> файл будет <span style=\" font-weight:600;\">ПЕРЕЗАПИСАН</span>.</p></body></html>", None))
            self.ui.label_titleSearch.setText(_translate("GitWindow", "Поиск файлов", None))
            self.ui.label_old01.setText(_translate("GitWindow", "Старый файл", None))
            self.ui.label_new01.setText(_translate("GitWindow", "Новый файл", None))
            self.ui.tabWidget_merge.setTabText(self.ui.tabWidget_merge.indexOf(self.ui.tab_merge_01), _translate("GitWindow", "Поиск", None))
            self.ui.label_old02.setText(_translate("GitWindow", "Старый файл", None))
            self.ui.button_browseOld.setText(_translate("GitWindow", "Обзор", None))
            self.ui.label_new02.setText(_translate("GitWindow", "Новый файл", None))
            self.ui.button_browseNew.setText(_translate("GitWindow", "Обзор", None))
            self.ui.label_titleBrowse.setText(_translate("GitWindow", "Указать файл вручную", None))
            self.ui.tabWidget_merge.setTabText(self.ui.tabWidget_merge.indexOf(self.ui.tab_merge_02), _translate("GitWindow", "Указать", None))
            self.ui.button_patch.setText(_translate("GitWindow", "Редактировать патч", None))
            self.ui.button_applyPatch.setText(_translate("GitWindow", "Принять", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_merge), _translate("GitWindow", "Слияние", None))
            self.ui.label_text1.setText(_translate("GitWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Внимание!</span></p></body></html>", None))
            self.ui.label_text2.setText(_translate("GitWindow", "Откат изменений может нарушить работу Вашей системы.", None))
            self.ui.label_text3.setText(_translate("GitWindow", "Откат к другим версиям осуществляйте", None))
            self.ui.label_text4.setText(_translate("GitWindow", "на свой страх и риск.", None))
            self.ui.label_id.setText(_translate("GitWindow", "Идентификатор коммита", None))
            self.ui.label_typeReset.setText(_translate("GitWindow", "Тип отката", None))
            self.ui.box_typeReset.setItemText(0, _translate("GitWindow", "Откат всех файлов", None))
            self.ui.box_typeReset.setItemText(1, _translate("GitWindow", "Откат одного файла", None))
            self.ui.label_filename.setText(_translate("GitWindow", "Выберете файл", None))
            self.ui.button_refresh.setText(_translate("GitWindow", "Обновить список", None))
            self.ui.button_reset.setText(_translate("GitWindow", "Откатить", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_reset), _translate("GitWindow", "Откат изменений", None))
        else:
            self.setWindowTitle(_translate("GitWindow", "git", None))
            self.ui.button_close.setText(_translate("GitWindow", "Close", None))
            self.ui.label_timeFrom.setText(_translate("GitWindow", "from", None))
            self.ui.label_timeTo.setText(_translate("GitWindow", "to", None))
            self.ui.label_titleInt.setText(_translate("GitWindow", "In time interval", None))
            self.ui.tabWidget_search.setTabText(self.ui.tabWidget_search.indexOf(self.ui.tab_search_01), _translate("GitWindow", "In interval", None))
            self.ui.label_times.setText(_translate("GitWindow", "Number of commits", None))
            self.ui.label_titleTimes.setText(_translate("GitWindow", "By number of commits", None))
            self.ui.tabWidget_search.setTabText(self.ui.tabWidget_search.indexOf(self.ui.tab_search_02), _translate("GitWindow", "By number of commits", None))
            self.ui.label_date.setText(_translate("GitWindow", "Date commit", None))
            self.ui.label_titleDate.setText(_translate("GitWindow", "By date commit", None))
            self.ui.tabWidget_search.setTabText(self.ui.tabWidget_search.indexOf(self.ui.tab_search_03), _translate("GitWindow", "By date", None))
            self.ui.button_get.setText(_translate("GitWindow", "Display", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_search), _translate("GitWindow", "Search", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_oneFile), _translate("GitWindow", "Changes in file", None))
            self.ui.button_createCommit.setText(_translate("GitWindow", "Create commit", None))
            self.ui.button_status.setText(_translate("GitWindow", "Show status", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_status), _translate("GitWindow", "Status", None))
            self.ui.button_refreshIgnore.setText(_translate("GitWindow", "Refresh", None))
            self.ui.button_addIgnore.setText(_translate("GitWindow", "Add", None))
            self.ui.button_deleteIgnore.setText(_translate("GitWindow", "Delete string", None))
            self.ui.button_applyIgnore.setText(_translate("GitWindow", "Apply", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_ignore), _translate("GitWindow", "Ignore list", None))
            self.ui.label_merge.setText(_translate("GitWindow", "<html><head/><body><p align=\"center\">Changes will be applied from <span style=\" font-weight:600; color:#ff0000;\">OLD</span> file to <span style=\" font-weight:600; color:#ff0000;\">NEW</span> file.</p><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">NEW</span> file will be <span style=\" font-weight:600;\">OVERWRITTEN</span>.</p></body></html>", None))
            self.ui.label_titleSearch.setText(_translate("GitWindow", "Search files", None))
            self.ui.label_old01.setText(_translate("GitWindow", "Old file", None))
            self.ui.label_new01.setText(_translate("GitWindow", "New file", None))
            self.ui.tabWidget_merge.setTabText(self.ui.tabWidget_merge.indexOf(self.ui.tab_merge_01), _translate("GitWindow", "Search", None))
            self.ui.label_old02.setText(_translate("GitWindow", "Jld file", None))
            self.ui.button_browseOld.setText(_translate("GitWindow", "Browse", None))
            self.ui.label_new02.setText(_translate("GitWindow", "New file", None))
            self.ui.button_browseNew.setText(_translate("GitWindow", "Browse", None))
            self.ui.label_titleBrowse.setText(_translate("GitWindow", "Set path to file", None))
            self.ui.tabWidget_merge.setTabText(self.ui.tabWidget_merge.indexOf(self.ui.tab_merge_02), _translate("GitWindow", "Set path", None))
            self.ui.button_patch.setText(_translate("GitWindow", "Edit patch", None))
            self.ui.button_applyPatch.setText(_translate("GitWindow", "Apply", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_merge), _translate("GitWindow", "Merge", None))
            self.ui.label_text1.setText(_translate("GitWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">Warning!</span></p></body></html>", None))
            self.ui.label_text2.setText(_translate("GitWindow", "Revert changes may affect operation of your system.", None))
            self.ui.label_text3.setText(_translate("GitWindow", "Rolling back to the other versions", None))
            self.ui.label_text4.setText(_translate("GitWindow", "at your own risk.", None))
            self.ui.label_id.setText(_translate("GitWindow", "Commit ID", None))
            self.ui.label_typeReset.setText(_translate("GitWindow", "Merge type", None))
            self.ui.box_typeReset.setItemText(0, _translate("GitWindow", "Full reset", None))
            self.ui.box_typeReset.setItemText(1, _translate("GitWindow", "Оne file reset", None))
            self.ui.label_filename.setText(_translate("GitWindow", "Choose file", None))
            self.ui.button_refresh.setText(_translate("GitWindow", "Refresh list", None))
            self.ui.button_reset.setText(_translate("GitWindow", "Reset", None))
            self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_reset), _translate("GitWindow", "Reset changes", None))
    
    def refresh_ignore(self):
        """Function to refresh ignore list in IgnoreTab"""
        self.ui.list_ignoreList.clear()
        self.ui.lineEdit_addIgnore.clear()
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
        command_line = sudo+"cat "+os.path.join(directory, ".git/info/exclude")
        ignoreList = commands.getoutput(command_line).split("\n")
        
        self.ui.list_ignoreList.addItems(ignoreList)
        self.ui.list_ignoreList.setCurrentRow(0)
    
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
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
            command_line = sudo+"git log --oneline"
            list_commit = commands.getoutput(command_line)
            command_line = sudo+"git reset --hard "+commit
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
            command_line = sudo+"git add -A . && "+sudo+"git commit -m `date +%Y%m%d%H%M%S-%N`"
            output = commands.getoutput(command_line)
            self.ui.text_reset.append(output)
            
            self.ui.text_reset.append("[II] Creating patch")
            command_line = sudo+"git diff HEAD "+commit+" "+filename+" > "+patch
            os.system(command_line)
            
            self.ui.text_reset.append("[II] Patching")
            command_line = sudo+"git apply < "+patch
            output = commands.getoutput(command_line)
            os.remove(patch)
            self.ui.text_reset.append(output+"[II] Done!")
            
            self.ui.text_reset.append("[II] Creating commit")
            command_line = sudo+"git add -A . && "+sudo+"git commit -m `date +%Y%m%d%H%M%S-%N`"
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
            if (os.path.exists(os.path.join(directory, ".git")) == False):
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
            sudo = read_settings("sudo")
            
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = sudo+"git show "+commit+" --name-only"
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
    
    def set_files(self):
        """Function to set file list"""
        self.ui.box_file.clear()
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        command_line = sudo+"ls -lARp --format=single-column --ignore .git "+directory
        list_files = commands.getoutput(command_line)
        preffix = directory
        for files in list_files.split("\n"):
            if (files != ""):
                if (files[-1] != "/"):
                    if (files[0] == "/"):
                        preffix = files[:-1]+"/"
                    else:
                        line = preffix + files
                        output = line.replace(directory, "")[1:]
                        self.ui.box_file.addItem(output)
    
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
            if (os.path.exists(os.path.join(directory, ".git")) == False):
                not_found = NotFound(parent=self, text="gitdir")
                not_found.show()
                return
            sudo = read_settings("sudo")
            command_line = sudo+"ls -lARp --format=single-column "+directory
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
            self.ui.tabWidget_search.setCurrentIndex(0)
            self.set_mode()
        elif (self.ui.tabWidget.currentIndex() == 1):
            self.set_files()
        elif (self.ui.tabWidget.currentIndex() == 2):
            self.ui.text_status.clear()
        elif (self.ui.tabWidget.currentIndex() == 3):
            self.refresh_ignore()
        elif (self.ui.tabWidget.currentIndex() == 4):
            self.ui.button_applyPatch.setDisabled(1)
            self.ui.tabWidget_merge.setCurrentIndex(0)
            self.set_merge()
        elif (self.ui.tabWidget.currentIndex() == 5):
            self.ui.box_typeReset.setCurrentIndex(0)
            self.ui.label_filename.hide()
            self.ui.box_filename.hide()
            self.ui.box_filename.clear()
            self.ui.lineEdit_id.clear()
            self.ui.text_reset.clear()
    
    def showOneFile(self):
        """Function to show commit for one file"""
        self.ui.list_commit_oneFile.clear()
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
        
        current_directory = os.getcwd()
        os.chdir(directory)
        
        command_line = sudo + "git log --oneline " + directory + "/" + str(self.ui.box_file.currentText())
        list_commit = commands.getoutput(command_line)
        for line in list_commit.split("\n"):
            output_line = "Commit: "+line[0:7]
            output_line = output_line+". Date: "+line[8:12]+"-"+line[12:14]+"-"+line[14:16]
            output_line = output_line+" "+line[16:18]+":"+line[18:20]
            self.ui.list_commit_oneFile.addItem(output_line)
        
        os.chdir(current_directory)
    
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
            if (text == "ad"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Ошибка доступа</p></body></html>")
            elif (text == "commitnf"):
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
        else:
            self.setWindowTitle(u"Error!")
            self.ui.button_ok.setText(u"Ok")
            if (text == "ad"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Access denied</p></body></html>")
            elif (text == "commitnf"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Commits not found</p></body></html>")
            elif (text == "conf"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Configuration file doesn't exists</p></body></html>")
            elif (text == "dir"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Directory doesn't exists</p></body></html>")
            elif (text == "editor"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Editor doesn't exists</p></body></html>")
            elif (text == "fnf"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">File not found</p></body></html>")
            elif (text == "gitdir"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Git repository not found</p></body></html>")
            elif (text == "id"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">ID is too short</p></body></html>")
            elif (text == "lone"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Value less than 1</p></body></html>")
            elif (text == "noconfig"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">File name isn't set</p></body></html>")
            elif (text == "nodir"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Directory isn't set</p></body></html>")
            elif (text == "noeditor"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Editor isn't set</p></body></html>")
            elif (text == "nofile"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">File isn't set</p></body></html>")
            elif (text == "noservice"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Service isn't set</p></body></html>")
            elif (text == "notime"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Time interval isn't set</p></body></html>")
            elif (text == "notnum"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Value isn't a number</p></body></html>")
            else:
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Unknown error</p></body></html>")


class SettingsWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """GUI Settings Window definition"""
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        
        self.load_text()
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
        self.ui.checkBox_sudo.setCheckState(2)
        
        self.save_config()
    
    def load_text(self):
        """Function to load text"""
        self.ui.box_lang.setItemText(0, _translate("SettingsWindow", "English", None))
        self.ui.box_lang.setItemText(1, _translate("SettingsWindow", "Русский", None))
        self.ui.label_service.setText(_translate("SettingsWindow", "Service", None))
        lang = read_settings("lang")
        if (lang == "RUS"):
            self.setWindowTitle(_translate("SettingsWindow", "Настройки", None))
            self.ui.button_default.setText(_translate("SettingsWindow", "По умолчанию", None))
            self.ui.button_apply.setText(_translate("SettingsWindow", "Применить", None))
            self.ui.button_close.setText(_translate("SettingsWindow", "Закрыть", None))
            self.ui.label_lang.setText(_translate("SettingsWindow", "Язык", None))
            self.ui.button_browse.setText(_translate("SettingsWindow", "Обзор", None))
            self.ui.label_editor.setText(_translate("SettingsWindow", "Текстовый редактор", None))
            self.ui.label_config.setText(_translate("SettingsWindow", "Настройки сервиса", None))
            self.ui.label_system.setText(_translate("SettingsWindow", "Системные настройки", None))
            self.ui.checkBox_sudo.setText(_translate("SettingsWindow", "Использовать sudo", None))
        else:
            self.setWindowTitle(_translate("SettingsWindow", "Settings", None))
            self.ui.button_default.setText(_translate("SettingsWindow", "Default", None))
            self.ui.button_apply.setText(_translate("SettingsWindow", "Apply", None))
            self.ui.button_close.setText(_translate("SettingsWindow", "Close", None))
            self.ui.label_lang.setText(_translate("SettingsWindow", "Language", None))
            self.ui.button_browse.setText(_translate("SettingsWindow", "Browse", None))
            self.ui.label_editor.setText(_translate("SettingsWindow", "Editor", None))
            self.ui.label_config.setText(_translate("SettingsWindow", "Service settings", None))
            self.ui.label_system.setText(_translate("SettingsWindow", "System settings", None))
            self.ui.checkBox_sudo.setText(_translate("SettingsWindow", "Enable sudo", None))
    
    def save_config(self):
        """Function to save configuration file"""
        config_gui = os.path.abspath(os.path.expanduser('~/.config/ctrlconf.conf'))
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
            if (self.ui.checkBox_sudo.checkState() == 2):
                config_gui_file.write("SUDO==YES==""")
            else:
                config_gui_file.write("SUDO==NO==""")
        
        self._parent.signals()
        
        self.load_text()
        self._parent.load_text()
        self._parent.about_window.load_text()
        self._parent.git_window.load_text()
        self._parent.config_window.load_text()
        
        self._parent.set_status()
        self._parent.ui.list_commit.clear()
        self.close()

    def set_text(self):
        """Function to load configuration file"""
        config_gui = os.path.abspath(os.path.expanduser('~/.config/ctrlconf.conf'))
        if (os.path.exists(config_gui)):
            self.ui.lineEdit_service.setText(read_settings("service"))
            self.ui.lineEdit_config.setText(read_settings("config"))
            self.ui.lineEdit_editor.setText(read_settings("editor"))
            if (read_settings("lang") == "RUS"):
                self.ui.box_lang.setCurrentIndex(1)
            else:
                self.ui.box_lang.setCurrentIndex(0)
            if (read_settings("sudo") == "sudo "):
                self.ui.checkBox_sudo.setCheckState(2)
            else:
                self.ui.checkBox_sudo.setCheckState(0)
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
        
        self.about_window = AboutWindow(parent=self)
        self.config_window = ConfigWindow(parent=self)
        self.git_window = GitWindow(parent=self)
        self.settings_window = SettingsWindow(parent=self)
        
        self.setup()
        self.load_text()
        self.signals()
        self.set_status()
        self.ui.timeEdit_to.setDate(QtCore.QDate.currentDate())
        self.ui.timeEdit_to.setTime(QtCore.QTime.currentTime())
            
        QtCore.QObject.connect(self.ui.action_about, QtCore.SIGNAL("triggered()"), self.about_window.show)
        QtCore.QObject.connect(self.ui.action_configure, QtCore.SIGNAL("triggered()"), self.config_window.show)
        QtCore.QObject.connect(self.ui.action_settings, QtCore.SIGNAL("triggered()"), self.settings_window.show)
        QtCore.QObject.connect(self.ui.action_exit, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.ui.button_startService, QtCore.SIGNAL("clicked()"), self.start_service)
        QtCore.QObject.connect(self.ui.button_stopService, QtCore.SIGNAL("clicked()"), self.stop_service)
        
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
        if (os.path.exists(os.path.join(directory, ".git")) == False):
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
        sudo = read_settings("sudo")
                
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
        command_line = sudo+"git log --oneline "
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
    
    def load_text(self):
        """Function to load text"""
        lang = read_settings("lang")
        self.setWindowTitle(_translate("MainWindow", "Control Config", None))
        self.ui.timeEdit_from.setDisplayFormat(_translate("MainWindow", "HH:mm dd.MM.yyyy", None))
        self.ui.timeEdit_to.setDisplayFormat(_translate("MainWindow", "H:mm dd.MM.yyyy", None))
        self.ui.label_statusService.setText(_translate("MainWindow", "(unknown)", None))
        if (lang == "RUS"):
            self.ui.label_timeFrom.setText(_translate("MainWindow", "с", None))
            self.ui.label_timeTo.setText(_translate("MainWindow", "по", None))
            self.ui.button_get.setText(_translate("MainWindow", "Вывести", None))
            self.ui.label_statusText.setText(_translate("MainWindow", "Статус:", None))
            self.ui.button_stopService.setText(_translate("MainWindow", "Стоп", None))
            self.ui.button_startService.setText(_translate("MainWindow", "Запуск", None))
            self.ui.menu_main.setTitle(_translate("MainWindow", "&Меню", None))
            self.ui.menu_help.setTitle(_translate("MainWindow", "&Справка", None))
            self.ui.action_exit.setText(_translate("MainWindow", "&Выход", None))
            self.ui.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
            self.ui.action_about.setText(_translate("MainWindow", "&О программе", None))
            self.ui.action_configure.setText(_translate("MainWindow", "Настроить &сервис", None))
            self.ui.action_configure.setShortcut(_translate("MainWindow", "Ctrl+S", None))
            self.ui.action_settings.setText(_translate("MainWindow", "&Настройки", None))
            self.ui.action_settings.setShortcut(_translate("MainWindow", "Ctrl+P", None))
            self.ui.action_git.setText(_translate("MainWindow", "Работа с &git", None))
            self.ui.action_git.setShortcut(_translate("MainWindow", "Ctrl+G", None))
        else:
            self.ui.label_timeFrom.setText(_translate("MainWindow", "from", None))
            self.ui.label_timeTo.setText(_translate("MainWindow", "to", None))
            self.ui.button_get.setText(_translate("MainWindow", "Display", None))
            self.ui.label_statusText.setText(_translate("MainWindow", "Status:", None))
            self.ui.button_stopService.setText(_translate("MainWindow", "Stop", None))
            self.ui.button_startService.setText(_translate("MainWindow", "Start", None))
            self.ui.menu_main.setTitle(_translate("MainWindow", "&Menu", None))
            self.ui.menu_help.setTitle(_translate("MainWindow", "&Help", None))
            self.ui.action_exit.setText(_translate("MainWindow", "&Quit", None))
            self.ui.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
            self.ui.action_about.setText(_translate("MainWindow", "&About", None))
            self.ui.action_configure.setText(_translate("MainWindow", "Service setup", None))
            self.ui.action_configure.setShortcut(_translate("MainWindow", "Ctrl+S", None))
            self.ui.action_settings.setText(_translate("MainWindow", "&Settings", None))
            self.ui.action_settings.setShortcut(_translate("MainWindow", "Ctrl+P", None))
            self.ui.action_git.setText(_translate("MainWindow", "&git", None))
            self.ui.action_git.setShortcut(_translate("MainWindow", "Ctrl+G", None))
    
    def set_status(self):
        """Function to set service status"""
        service = read_settings("service")
        sudo = read_settings("sudo")
        
        command_line = sudo+"systemctl status "+service+" | grep Active" 
        status_service = ' '.join(commands.getoutput(command_line).split()[1:3])
        
        self.ui.label_statusService.setText(status_service)
    
    def setup(self):
        """Function to create configuration file if it doesn't exists"""
        config_gui = os.path.abspath(os.path.expanduser('~/.config/ctrlconf.conf'))
        if (os.path.exists(config_gui)):
            return
        
        with open(config_gui, 'w') as config_gui_file:
            config_gui_file.write("# Automatically generated by Control Config\n")
            config_gui_file.write("SERVICE==git-etc.service==\n")
            config_gui_file.write("CONFIG==/etc/conf.d/git-etc.conf==\n")
            config_gui_file.write("EDITOR==gvim==\n")
            config_gui_file.write("LANGUAGE==ENG==\n")
            config_gui_file.write("SUDO==YES==\n")
        
    def signals(self):
        """Function to setup signals that enable"""
        directory = read_config("directory")
        sudo = read_settings("sudo")
        
        QtCore.QObject.disconnect(self.ui.action_git, QtCore.SIGNAL("triggered()"), self.git_window.show)
        QtCore.QObject.disconnect(self.ui.button_get, QtCore.SIGNAL("clicked()"), self.get_text)
        QtCore.QObject.disconnect(self.ui.list_commit, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.commit_details)
        
        if (os.path.exists(os.path.join(directory, ".git"))):
            command_line = "ls "+os.path.join(directory, ".git")
            access = commands.getoutput(command_line)
            if ((access[0:3] == "ls:") and (sudo == "")):
                not_found = NotFound(parent=self, text="ad")
                not_found.show()
            else:
                QtCore.QObject.connect(self.ui.action_git, QtCore.SIGNAL("triggered()"), self.git_window.show)
                QtCore.QObject.connect(self.ui.button_get, QtCore.SIGNAL("clicked()"), self.get_text)
                QtCore.QObject.connect(self.ui.list_commit, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.commit_details)
        else:
            not_found = NotFound(parent=self, text="gitdir")
            not_found.show()
            return
    
    def start_service(self):
        """Function to start service"""
        service = read_settings("service")
        sudo = read_settings("sudo")
        
        command_line = sudo+"systemctl start "+service
        os.system(command_line)
        self.set_status()
    
    def stop_service(self):
        """Function to stop service"""
        service = read_settings("service")
        sudo = read_settings("sudo")
        
        command_line = sudo+"systemctl stop "+service
        os.system(command_line)
        self.set_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='GUI for git-etc daemon', 
            epilog='See "man 1 ctrlconf" for more details')
    parser.add_argument('-v','--version', dest='ver',
            help = 'Show version and exit',
            action='store_true', default = False)
    parser.add_argument('--default', dest='createDefault',
            help = 'Create default configuration file',
            action='store_true', default = False)
    
    args = parser.parse_args()
    if (args.ver):
        print ("                    Control Config")
        print ("GUI for git-etc daemon to work with GIT repository")
        print ("Version : 2.0                        License : GPL")
        print ("                                        by arcanis")
        print ("                      E-mail : esalexeev@gmail.com")
        sys.exit()
    if (args.createDefault):
        config_gui = os.path.abspath(os.path.expanduser('~/.config/ctrlconf.conf'))
        if (os.path.exists(config_gui)):
            os.remove(config_gui)
    
    app = QtGui.QApplication(sys.argv)
    codec = QtCore.QTextCodec.codecForName("UTF-8")
    QtCore.QTextCodec.setCodecForCStrings(codec)
    
    ctrlconf = MainWindow()
    ctrlconf.show()
    sys.exit(app.exec_())
