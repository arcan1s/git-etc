#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Do not touch!
# Magick!

 
import commands, datetime, os, shutil, sys
from PyQt4 import QtCore, QtGui

from configwin import Ui_ConfigureWindow
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



class ConfigWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_ConfigureWindow()
        self.ui.setupUi(self)
        
        self.read_config()
        
        QtCore.QObject.connect(self.ui.button_apply, QtCore.SIGNAL("clicked()"), self.setup_config)
        QtCore.QObject.connect(self.ui.button_close, QtCore.SIGNAL("clicked()"), self.close)        
        QtCore.QObject.connect(self.ui.button_refresh, QtCore.SIGNAL("clicked()"), self.read_config)
        
    def read_config(self):
        config = "/home/arcanis/Documents/github/git-etc/source/git-etc.conf"
        
        self.ui.lineEdit_directory.clear()
        self.ui.lineEdit_timeSleep.clear()
        self.ui.lineEdit_ignoreList.clear()
        
        with open(config, 'r') as config_file:
            for line in config_file:
                if (line.split("=")[0] == "DIRECTORY"):
                    directory = str(line.split("=")[1][:-1])
                    self.ui.lineEdit_directory.setText(directory)
                elif (line.split("=")[0] == "TIMESLEEP"):
                    timesleep = str(line.split("=")[1][:-1])
                    self.ui.lineEdit_timeSleep.setText(timesleep)
                elif (line.split("=")[0] == "IGNORELIST"):
                    ignorelist = line.split("=")[1]
                    self.ui.lineEdit_ignoreList.setText(ignorelist)
    
    def setup_config(self):
        config = "/home/arcanis/Documents/github/git-etc/source/git-etc.conf"
        
        if (len(self.ui.lineEdit_directory.text()) == 0):
            text_error = u"<html><head/><body><p align=\"center\">Не указана рабочая директория</p></body></html>"
            not_found = NotFound(parent=self, text=text_error)
            not_found.show()
            return
        else:
            directory = self.ui.lineEdit_directory.text()
        
        if (len(self.ui.lineEdit_timeSleep.text()) == 0):
            text_error = u"<html><head/><body><p align=\"center\">Не указан интервал обновления</p></body></html>"
            not_found = NotFound(parent=self, text=text_error)
            not_found.show()
            return
        else:
            if (self.ui.lineEdit_timeSleep.text().toInt()[1] == False):
                text_error = u"<html><head/><body><p align=\"center\">" + self.ui.lineEdit_timeSleep.text() + u" не число</p></body></html>"
                not_found = NotFound(parent=self, text=text_error)
                not_found.show()
                return
            else:
                if (self.ui.lineEdit_timeSleep.text().toInt()[0] < 1):
                    text_error = u"<html><head/><body><p align=\"center\">" + self.ui.lineEdit_timeSleep.text() + u" отрицательное</p></body></html>"
                    not_found = NotFound(parent=self, text=text_error)
                    not_found.show()
                    return
                else:
                    timesleep = self.ui.lineEdit_timeSleep.text().toInt()[0]
        
        ignorelist = self.ui.lineEdit_ignoreList.text()
        
        with open(config, 'w') as config_file:
            config_file.write("DIRECTORY="+directory)
            config_file.write("\nTIMESLEEP="+str(timesleep))
            config_file.write("\nIGNORELIST="+ignorelist)
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class NotFound(QtGui.QMainWindow):
    def __init__(self, parent=None, text=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_NotFound()
        self.ui.setupUi(self)
        
        self.load_text()
        
        if (text != None):
            self.ui.label_textError.setText(text)

    def load_text(self):
        self.setWindowTitle(u"Ошибка!")
        self.ui.label_textError.setText(u"<html><head/><body><p align=\"justify\"><br></p></body></html>")
        self.ui.button_ok.setText(u"Ok")


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.set_status()
        self.ui.timeEdit_to.setDate(QtCore.QDate.currentDate())
        self.ui.timeEdit_to.setTime(QtCore.QTime.currentTime())
        
        config_window = ConfigWindow(parent=self)
        
        QtCore.QObject.connect(self.ui.action_configure, QtCore.SIGNAL("triggered()"), config_window.show)
        QtCore.QObject.connect(self.ui.action_exit, QtCore.SIGNAL("triggered()"), self.close)
        QtCore.QObject.connect(self.ui.button_get, QtCore.SIGNAL("clicked()"), self.get_text)
        QtCore.QObject.connect(self.ui.button_startService, QtCore.SIGNAL("clicked()"), self.start_service)
        QtCore.QObject.connect(self.ui.button_stopService, QtCore.SIGNAL("clicked()"), self.stop_service)
    
    def get_text(self):
        config = "/home/arcanis/Documents/github/git-etc/source/git-etc.conf"
        
        with open(config, 'r') as config_file:
            for line in config_file:
                if (line.split("=")[0] == "DIRECTORY"):
                    directory = str(line.split("=")[1][:-1])
                
        time_now = datetime.datetime.now()        
        time_to = self.ui.timeEdit_to.dateTime().toPyDateTime()
        time_from = self.ui.timeEdit_from.dateTime().toPyDateTime()
        time_interval_to = time_now - time_to
        time_interval_from = time_now - time_from
        
        # [days, hours, minutes]
        # ti[t/f] = time_interval_[to/from]
        tit = [str(time_interval_to.days), str((time_interval_to.seconds-(time_interval_to.seconds%3600))/3600), str(((time_interval_to.seconds%3600)-(time_interval_to.seconds%3600)%60)/60)]       
        tif = [str(time_interval_from.days), str((time_interval_from.seconds-(time_interval_from.seconds%3600))/3600), str(((time_interval_from.seconds%3600)-(time_interval_from.seconds%3600)%60)/60)]
        
        os.chdir(directory)
        print os.getcwd()
        command_line = "git log --oneline "
        command_line = command_line+"--since=\""+tif[0]+" days "+tif[1]+" hours "+tif[2]+" minutes\" "
        command_line = command_line+"--until=\""+tit[0]+" days "+tit[1]+" hours "+tit[2]+" minutes\""
        #for line in commands.getoutput(command_line):
            #print line
    
    def set_status(self):
        status_service = commands.getoutput("systemctl status test_git-etc.service | grep Active | awk {'print $2;'}")
        status_service = status_service + ' '
        status_service = status_service + commands.getoutput("systemctl status test_git-etc.service | grep Active | awk {'print $3;'}")
        
        self.ui.label_statusService.setText(status_service)
    
    def start_service(self):
        print "Starting service"
        os.system('sudo systemctl start test_git-etc.service')
        self.set_status()
    
    def stop_service(self):
        print "Stoping service"
        os.system('sudo systemctl stop test_git-etc.service')
        self.set_status()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    codec = QtCore.QTextCodec.codecForName("UTF-8")
    QtCore.QTextCodec.setCodecForCStrings(codec)
    
    git2etc = MainWindow()
    git2etc.show()
    sys.exit(app.exec_())
