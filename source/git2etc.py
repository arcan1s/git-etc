#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Do not touch!
# Magick!

 
import commands, datetime, os, shutil, sys
from PyQt4 import QtCore, QtGui

from commitwin import Ui_CommitWindow
from configwin import Ui_ConfigureWindow
from gitwin import Ui_GitWindow
from settingswin import Ui_SettingsWindow
from mainwin import Ui_MainWindow


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



def read_config(string):
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



class CommitWindow(QtGui.QMainWindow):
    def __init__(self, parent=None, commit=None):
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
        
        command_line = editor+" "+directory+"/"+str(self.ui.box_file.currentText())
        os.system(command_line)
    
    def set_diff(self):
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
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class ConfigWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_ConfigureWindow()
        self.ui.setupUi(self)
        
        self.read_config()
        
        QtCore.QObject.connect(self.ui.button_apply, QtCore.SIGNAL("clicked()"), self.setup_config)
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close_win)        
        QtCore.QObject.connect(self.ui.button_refresh, QtCore.SIGNAL("clicked()"), self.read_config)
    
    def close_win(self):
        self.read_config()
        self.close()
        
    def read_config(self):
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
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class GitWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
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
        commit = str(self.ui.list_commit.currentItem().text())[8:15]
        
        commit_window = CommitWindow(parent=self, commit=commit)
        commit_window.show()
    
    def create_commit(self):
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
        gitlog_file = commands.getoutput(command_line)
        self.ui.text_status.setText(gitlog_file)
                
        os.chdir(current_directory)
    
    def create_patch(self):
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
            new_file = str(self.ui.box_new.currentText())
            old_file = str(self.ui.box_old.currentText())
        elif (self.ui.tabWidget_merge.currentIndex() == 1):
            new_file = str(self.ui.lineEdit_new.text())
            old_file = str(self.ui.lineEdit_old.text())
            if ((len(new_file) == 0) or (len(old_file) == 0)):
                not_found = NotFound(parent=self, text="nofile")
                not_found.show()
                return
            if ((os.path.exists(new_file) == False) or (os.path.exists(old_file) == False)):
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
        command_line = "sudo git add -A . && sudo git add -A . && sudo git commit -m `date +%Y%m%d%H%M%S-%N` > /dev/null"
        os.system(command_line)
        command_line = "sudo git diff "+last_commit+" HEAD "+new_file+" > "+self._patch_name
        os.system(command_line)
        os.system("sudo git checkout master > /dev/null")
        os.system(editor+" "+self._patch_name)
        os.chdir(current_directory)
        self.ui.button_applyPatch.setEnabled(1)
    
    def get_status(self):
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
            
            for line in gitlog_file.split("\n"):
                output_line = "Commit: "+line[0:7]
                output_line = output_line+". Date: "+line[8:12]+"-"+line[12:14]+"-"+line[14:16]
                output_line = output_line+" "+line[16:18]+":"+line[18:20]
                self.ui.list_commit.addItem(output_line)
                
            os.chdir(current_directory)
        elif (self.ui.tabWidget_search.currentIndex() == 1):
            times = str(self.ui.spinBox_times.value())
            
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = "sudo git log --oneline -"+times
            gitlog_file = commands.getoutput(command_line)
            
            for line in gitlog_file.split("\n"):
                output_line = "Commit: "+line[0:7]
                output_line = output_line+". Date: "+line[8:12]+"-"+line[12:14]+"-"+line[14:16]
                output_line = output_line+" "+line[16:18]+":"+line[18:20]
                self.ui.list_commit.addItem(output_line)
                
            os.chdir(current_directory)
        elif (self.ui.tabWidget_search.currentIndex() == 2):
            date_now = datetime.date.today()        
            date_interval = date_now - self.ui.dateEdit_date.date().toPyDate()
        
            current_directory = os.getcwd()
            os.chdir(directory)
            command_line = "sudo git log --oneline "
            command_line = command_line+"--since=\""+str(date_interval.days+1)+" days\" "
            command_line = command_line+"--until=\""+str(date_interval.days)+" days\""
            gitlog_file = commands.getoutput(command_line)
            
            for line in gitlog_file.split("\n"):
                output_line = "Commit: "+line[0:7]
                output_line = output_line+". Date: "+line[8:12]+"-"+line[12:14]+"-"+line[14:16]
                output_line = output_line+" "+line[16:18]+":"+line[18:20]
                self.ui.list_commit.addItem(output_line)
                
            os.chdir(current_directory)
    
    def reset_commit(self):
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
        current_item = str(self.ui.box_old.currentText())
        if ((current_item[-7:] == ".pacnew") or (current_item[-8:] == ".pacsave") or (current_item[-8:] == ".pacorig") or (current_item[-4:] == ".new") or (current_item[-4:] == ".old") or (current_item[-5:] == ".bckp")):
            current_item = '.'.join(current_item.split('.')[:-1])
            index = self.ui.box_new.findText(current_item)
            self.ui.box_new.setCurrentIndex(index)
    
    def set_merge(self):
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
                            if ((files[-7:] == ".pacnew") or (files[-8:] == ".pacsave") or (files[-8:] == ".pacorig") or (files[-4:] == ".new") or (files[-4:] == ".old") or (files[-5:] == ".bckp")):
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
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class NotFound(QtGui.QMainWindow):
    def __init__(self, parent=None, text=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_NotFound()
        self.ui.setupUi(self)
        
        self.load_text(text)

    def load_text(self, text):
        lang = read_settings("lang")
        if (lang == "RUS"):
            self.setWindowTitle(u"Ошибка!")
            self.ui.button_ok.setText(u"Ok")
            if (text == "commitnf"):
                self.ui.label_textError.setText(u"<html><head/><body><p align=\"center\">Указанный коммит не найден</p></body></html>")
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
        lang = read_settings("lang")
        if (lang == 'RUS'):
            config = QtGui.QFileDialog.getOpenFileName(self, u'Configuration file','','Все файлы (*)')
        else:
            config = QtGui.QFileDialog.getOpenFileName(self, u'Файл настроек','','All files (*)')
        if (len(config) > 0):
            self.ui.lineEdit_config.setText(config)
    
    def close_win(self):
        self.set_text()
        self.close()
    
    def create_config(self):
        self.ui.lineEdit_service.setText("git-etc.service")
        self.ui.lineEdit_config.setText("/etc/conf.d/git-etc.conf")
        self.ui.lineEdit_editor.setText("gvim")
        self.ui.box_lang.setCurrentIndex(0)
        
        self.save_config()
    
    def save_config(self):
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
        config_gui = os.path.abspath(os.path.expanduser('~/.config/git2etc.conf'))
        if (os.path.exists(config_gui)):
            self.ui.lineEdit_service.setText("service")
            self.ui.lineEdit_config.setText(read_settings("config"))
            self.ui.lineEdit_editor.setText(read_settings("editor"))
            if (read_settings("lang") == "RUS"):
                self.ui.box_lang.setCurrentIndex(1)
            else:
                self.ui.box_lang.setCurrentIndex(0)
        else:
            self.create_config()
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setup()
        self.set_status()
        self.ui.timeEdit_to.setDate(QtCore.QDate.currentDate())
        self.ui.timeEdit_to.setTime(QtCore.QTime.currentTime())
        
        config_window = ConfigWindow(parent=self)
        git_window = GitWindow(parent=self)
        settings_window = SettingsWindow(parent=self)
        
        QtCore.QObject.connect(self.ui.action_configure, QtCore.SIGNAL("triggered()"), config_window.show)
        QtCore.QObject.connect(self.ui.action_git, QtCore.SIGNAL("triggered()"), git_window.show)
        QtCore.QObject.connect(self.ui.action_settings, QtCore.SIGNAL("triggered()"), settings_window.show)
        QtCore.QObject.connect(self.ui.action_exit, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.ui.button_get, QtCore.SIGNAL("clicked()"), self.get_text)
        QtCore.QObject.connect(self.ui.button_startService, QtCore.SIGNAL("clicked()"), self.start_service)
        QtCore.QObject.connect(self.ui.button_stopService, QtCore.SIGNAL("clicked()"), self.stop_service)
        QtCore.QObject.connect(self.ui.list_commit, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.commit_details)
    
    def commit_details(self):
        commit = str(self.ui.list_commit.currentItem().text())[8:15]
        
        commit_window = CommitWindow(parent=self, commit=commit)
        commit_window.show()
    
    def get_text(self):
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
      
        for line in gitlog_file.split("\n"):
            output_line = "Commit: "+line[0:7]
            output_line = output_line+". Date: "+line[8:12]+"-"+line[12:14]+"-"+line[14:16]
            output_line = output_line+" "+line[16:18]+":"+line[18:20]
            self.ui.list_commit.addItem(output_line)
               
        os.chdir(current_directory)
    
    def set_status(self):
        service = read_settings("service")
        
        command_line = "systemctl status "+service+" | grep Active | awk {'print $2;'}"
        status_service = commands.getoutput(command_line)
        status_service = status_service + ' '
        command_line = "systemctl status "+service+" | grep Active | awk {'print $3;'}"
        status_service = status_service + commands.getoutput(command_line)
        
        self.ui.label_statusService.setText(status_service)
    
    def setup(self):
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
        service = read_settings("service")
        
        command_line = "sudo systemctl start "+service
        os.system(command_line)
        self.set_status()
    
    def stop_service(self):
        service = read_settings("service")
        
        command_line = "sudo systemctl stop "+service
        os.system(command_line)
        self.set_status()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    codec = QtCore.QTextCodec.codecForName("UTF-8")
    QtCore.QTextCodec.setCodecForCStrings(codec)
    
    git2etc = MainWindow()
    git2etc.show()
    sys.exit(app.exec_())