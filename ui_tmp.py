# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CHADv12.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, glob
sys.path.append("./functions")
from main import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 601, 671))
        self.stackedWidget.setObjectName("stackedWidget")
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.frame_2 = QtWidgets.QFrame(self.SettingsPage)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 600, 671))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255));\n"
"border-radius: 10px\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 90, 581, 401))
        self.frame_3.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.toolBox = QtWidgets.QToolBox(self.frame_3)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 581, 401))
        self.toolBox.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.toolBox.setObjectName("toolBox")
        self.Dir = QtWidgets.QWidget()
        self.Dir.setGeometry(QtCore.QRect(0, 0, 581, 339))
        self.Dir.setStyleSheet("")
        self.Dir.setObjectName("Dir")
        self.del_temp = QtWidgets.QCheckBox(self.Dir)
        self.del_temp.setGeometry(QtCore.QRect(25, 300, 265, 16))
        self.del_temp.setObjectName("del_temp")
        self.btn_dir = QtWidgets.QPushButton(self.Dir)
        self.btn_dir.setGeometry(QtCore.QRect(90, 20, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_dir.setFont(font)
        self.btn_dir.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.btn_dir.setObjectName("btn_dir")
        self.btn_dir.clicked.connect(self.select_dir)                
        self.include_sub = QtWidgets.QCheckBox(self.Dir)
        self.include_sub.setGeometry(QtCore.QRect(300, 30, 91, 32))
        self.include_sub.setObjectName("include_sub")
        self.include_sub.stateChanged.connect(self.update_files)
        self.pathIN = QtWidgets.QTextBrowser(self.Dir)
        self.pathIN.setGeometry(QtCore.QRect(20, 120, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathIN.setFont(font)
        self.pathIN.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN.setObjectName("pathIN")
        self.label_9 = QtWidgets.QLabel(self.Dir)
        self.label_9.setGeometry(QtCore.QRect(24, 100, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Dir)
        self.label_10.setGeometry(QtCore.QRect(300, 100, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.wavs = QtWidgets.QTextBrowser(self.Dir)
        self.wavs.setGeometry(QtCore.QRect(300, 120, 271, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wavs.setFont(font)
        self.wavs.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.wavs.setObjectName("wavs")
        self.toolBox.addItem(self.Dir, "")
        self.Params = QtWidgets.QWidget()
        self.Params.setGeometry(QtCore.QRect(0, 0, 581, 339))
        self.Params.setStyleSheet("")
        self.Params.setObjectName("Params")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Params)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 561, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.model_label = QtWidgets.QLabel(self.frame_4)
        self.model_label.setGeometry(QtCore.QRect(20, 10, 111, 58))
        self.model_label.setObjectName("model_label")
        self.model_sel = QtWidgets.QComboBox(self.frame_4)
        self.model_sel.setGeometry(QtCore.QRect(210, 20, 331, 31))
        self.model_sel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.model_sel.setObjectName("model_sel")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.vad_label = QtWidgets.QLabel(self.frame_5)
        self.vad_label.setGeometry(QtCore.QRect(20, 10, 141, 59))
        self.vad_label.setObjectName("vad_label")
        self.vad_spin = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.vad_spin.setGeometry(QtCore.QRect(440, 20, 101, 31))
        self.vad_spin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vad_spin.setObjectName("vad_spin")
        self.vad_spin.setDecimals(3)
        self.vad_spin.setMinimum(0.078)
        self.vad_spin.setMaximum(0.15)
        self.vad_spin.setSingleStep(0.001)
        self.vad_spin.setProperty("value", 0.08)
        self.vad_spin.setObjectName("vad_spin")        
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.prob_label = QtWidgets.QLabel(self.frame_6)
        self.prob_label.setGeometry(QtCore.QRect(20, 10, 201, 58))
        self.prob_label.setObjectName("prob_label")
        self.prob_spin = QtWidgets.QDoubleSpinBox(self.frame_6)
        self.prob_spin.setGeometry(QtCore.QRect(440, 20, 101, 31))
        self.prob_spin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prob_spin.setObjectName("prob_spin")
        self.prob_spin.setMaximum(1.0)
        self.prob_spin.setSingleStep(0.01)
        self.prob_spin.setProperty("value", 0.4)        
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 91, 58))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_7)
        self.groupBox.setGeometry(QtCore.QRect(220, 30, 331, 21))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.par_0 = QtWidgets.QRadioButton(self.groupBox)
        self.par_0.setGeometry(QtCore.QRect(20, 2, 51, 16))
        self.par_0.setChecked(True)
        self.par_0.setObjectName("par_0")
        self.par_1 = QtWidgets.QRadioButton(self.groupBox)
        self.par_1.setGeometry(QtCore.QRect(105, 2, 51, 16))
        self.par_1.setObjectName("par_1")
        self.par_2 = QtWidgets.QRadioButton(self.groupBox)
        self.par_2.setGeometry(QtCore.QRect(190, 2, 51, 16))
        self.par_2.setObjectName("par_2")
        self.par_3 = QtWidgets.QRadioButton(self.groupBox)
        self.par_3.setGeometry(QtCore.QRect(275, 0, 51, 16))
        self.par_3.setObjectName("par_3")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.toolBox.addItem(self.Params, "")
        self.frame_title_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_title_3.setGeometry(QtCore.QRect(0, 0, 601, 31))
        self.frame_title_3.setStyleSheet("background-color: rgba(1, 32, 15, 100)")
        self.frame_title_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_3.setObjectName("frame_title_3")
        self.btn_min = QtWidgets.QPushButton(self.frame_title_3)
        self.btn_min.setGeometry(QtCore.QRect(540, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min.setFont(font)
        self.btn_min.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color:rgb(240, 135, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 135, 0, 150);\n"
"}")
        self.btn_min.setObjectName("btn_min")
        self.btn_min.clicked.connect(self.minimize)       
        self.btn_exit = QtWidgets.QPushButton(self.frame_title_3)
        self.btn_exit.setGeometry(QtCore.QRect(570, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(235,0,0, 150);\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(self.on_closing)        
        self.title_3 = QtWidgets.QLabel(self.frame_title_3)
        self.title_3.setGeometry(QtCore.QRect(11, -3, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_3.setFont(font)
        self.title_3.setAutoFillBackground(False)
        self.title_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title_3.setObjectName("title_3")
        self.btn_run = QtWidgets.QPushButton(self.frame_2)
        self.btn_run.setGeometry(QtCore.QRect(190, 550, 221, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_run.setObjectName("btn_run")
        self.btn_run.setEnabled(False)  
        self.btn_run.clicked.connect(self.run_main)        

        self.stackedWidget.addWidget(self.SettingsPage)
        self.ResultsPage = QtWidgets.QWidget()
        self.ResultsPage.setObjectName("ResultsPage")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.ResultsPage)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 601, 671))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 600, 671))
        self.frame_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255));\n"
"border-radius: 10px\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setGeometry(QtCore.QRect(10, 90, 581, 401))
        self.frame_9.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.results = QtWidgets.QPlainTextEdit(self.frame_9)
        self.results.setGeometry(QtCore.QRect(10, 120, 551, 231))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.results.setFont(font)
        self.results.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.results.setObjectName("results")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.filelist = QtWidgets.QComboBox(self.frame_9)
        self.filelist.setGeometry(QtCore.QRect(220, 90, 331, 22))
        self.filelist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filelist.setObjectName("filelist")
        self.label = QtWidgets.QLabel(self.frame_9)
        self.label.setGeometry(QtCore.QRect(10, 90, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pathIN_2 = QtWidgets.QTextBrowser(self.frame_9)
        self.pathIN_2.setGeometry(QtCore.QRect(300, 10, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathIN_2.setFont(font)
        self.pathIN_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN_2.setObjectName("pathIN_2")
        self.btn_listen = QtWidgets.QPushButton(self.frame_9)
        self.btn_listen.setGeometry(QtCore.QRect(400, 280, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_listen.setFont(font)
        self.btn_listen.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 144, 0, 255), stop:1 rgba(16, 255, 0, 255));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(16, 254, 0, 255), stop:1 rgba(171, 255, 166, 255))\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_listen.setObjectName("btn_listen")
        self.frame_title_4 = QtWidgets.QFrame(self.frame_8)
        self.frame_title_4.setGeometry(QtCore.QRect(0, 0, 601, 31))
        self.frame_title_4.setStyleSheet("background-color: rgba(1, 32, 15, 100)")
        self.frame_title_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_4.setObjectName("frame_title_4")
        self.btn_min_2 = QtWidgets.QPushButton(self.frame_title_4)
        self.btn_min_2.setGeometry(QtCore.QRect(540, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min_2.setFont(font)
        self.btn_min_2.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color:rgb(240, 135, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 135, 0, 150);\n"
"}")
        self.btn_min_2.setObjectName("btn_min_2")
        self.btn_min_2.clicked.connect(self.minimize)        
        self.btn_exit_2 = QtWidgets.QPushButton(self.frame_title_4)
        self.btn_exit_2.setGeometry(QtCore.QRect(570, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit_2.setFont(font)
        self.btn_exit_2.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(235,0,0, 150);\n"
"}")
        self.btn_exit_2.setObjectName("btn_exit_2")
        self.btn_exit_2.clicked.connect(self.on_closing)        

        self.title_4 = QtWidgets.QLabel(self.frame_title_4)
        self.title_4.setGeometry(QtCore.QRect(11, -3, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_4.setFont(font)
        self.title_4.setAutoFillBackground(False)
        self.title_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title_4.setObjectName("title_4")
        self.btn_xlsx = QtWidgets.QPushButton(self.frame_8)
        self.btn_xlsx.setGeometry(QtCore.QRect(350, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_xlsx.setFont(font)
        self.btn_xlsx.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_xlsx.setObjectName("btn_xlsx")
        self.title_res = QtWidgets.QLabel(self.frame_8)
        self.title_res.setGeometry(QtCore.QRect(20, 50, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_res.setFont(font)
        self.title_res.setAutoFillBackground(False)
        self.title_res.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title_res.setObjectName("title_res")
        self.btn_txt = QtWidgets.QPushButton(self.frame_8)
        self.btn_txt.setGeometry(QtCore.QRect(100, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_txt.setFont(font)
        self.btn_txt.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_txt.setObjectName("btn_txt")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.stackedWidget.addWidget(self.ResultsPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        modelslist = [model.replace("pcen_rnn4_cl2_RMED_allARUs_run0.hdf5", "pcen_rnn4_cl2_RMED_allARUs_run0.hdf5 (default)") for model in os.listdir("./models/") if model.endswith('.hdf5')]
        [self.model_sel.addItem(mdl) for mdl in modelslist]
        self.max_cpus = self.count_processors()
        
        self.del_temp.setText(_translate("MainWindow", "Delete intermediate files"))
        self.btn_dir.setText(_translate("MainWindow", "Select\n"
"Directory"))
        self.include_sub.setText(_translate("MainWindow", "Include\n"
"Subfolders"))
        self.pathIN.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">[Please select a directory]</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Directory with wav files:"))
        self.label_10.setText(_translate("MainWindow", "Files to be processed:"))
        self.wavs.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">[No directory selected]</span></p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Dir), _translate("MainWindow", ">> Directory selection"))
        self.model_label.setText(_translate("MainWindow", "Select model (for \n"
"classification):"))
        self.vad_label.setText(_translate("MainWindow", "VAD threshold chosen: \n"
"[Can take any value \n"
"between 0.078-0.15]"))
        self.prob_label.setText(_translate("MainWindow", "Probability threshold chosen: \n"
"[Can take any value between 0-1]"))
        self.label_2.setText(_translate("MainWindow", "Parallelization:"))
        self.par_0.setText(_translate("MainWindow", "No"))
        self.par_1.setText(_translate("MainWindow", "Low"))
        self.par_2.setText(_translate("MainWindow", "Mid"))
        self.par_3.setText(_translate("MainWindow", "Full"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Params), _translate("MainWindow", ">> Advanced Parameters"))
        self.btn_min.setText(_translate("MainWindow", "_"))
        self.btn_exit.setText(_translate("MainWindow", "X"))
        self.title_3.setText(_translate("MainWindow", "CHA.D. - Chainsaw Detection (v 1.1)"))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.label_4.setText(_translate("MainWindow", "Directory with wav files scanned:"))
        self.label.setText(_translate("MainWindow", "Results per file:"))
        self.pathIN_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">[Please select a directory]</span></p></body></html>"))
        self.btn_listen.setText(_translate("MainWindow", "Click to listen\n"
"detections"))
        self.btn_min_2.setText(_translate("MainWindow", "_"))
        self.btn_exit_2.setText(_translate("MainWindow", "X"))
        self.title_4.setText(_translate("MainWindow", "CHA.D. - Chainsaw Detection (v 1.1)"))
        self.btn_xlsx.setText(_translate("MainWindow", "Save as .xlsx"))
        self.title_res.setText(_translate("MainWindow", "Results"))
        self.btn_txt.setText(_translate("MainWindow", "Save as .txt"))


    def minimize(self):
        self.showMinimized()

    def update_files(self):
        folder = self.pathIN.toPlainText()
        if self.include_sub.isChecked():
            files = glob.glob(f"{folder}/**/*.wav", recursive=True)
        else:
            files = glob.glob(f"{folder}/*.wav", recursive=False)

        if len(files)>0:
            files = "\n".join(files).replace("\\", "/").replace(folder, "./")
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run")
        else:
            files = "No .wav files found in selected directory."
            self.btn_run.setText("Run\n(Select a valid directory)")
            self.btn_run.setEnabled(False)
        self.wavs.setText(files)


    def count_processors(self):
        import multiprocessing
        import numpy as np
        nop=multiprocessing.cpu_count()
        print(str(int(nop)) + ' cpus found')
        return nop

    def parse_cpu_radio(self):
        max_cpus = self.max_cpus
        choice_list = [1, max_cpus//4, max_cpus//2, max_cpus]
        # print(f"parchoice {self.parchoice.get()}, cpus = {self.cpus.get()}")
        cpu_temp = choice_list[self.parchoice.get()]
        self.cpus.set(max([1, cpu_temp]))
        # print(f"parchoice {self.parchoice.get()}, cpus = {self.cpus.get()}")

    def select_dir(self):
        import glob
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if folder:
            self.pathIN.setText(folder)
            self.update_files()
            self.btn_dir.setText("Change\nDirectory")
        #window.label_2.setText(file)


    def on_closing(self):
        import gc

        reply = QtWidgets.QMessageBox.question(self, 'Quit',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            print('Thank you for using our tool!')
            QtCore.QCoreApplication.instance().quit()
            gc.collect()
            exit()


    def copy_citation_(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(citation)
        # self.parent.update() # the text will stay there after the window is closed
        # self.copied_lbl_txt.set("(Copied!)")

    def export_xlsx(self):
        if self.filelist.currentText()=="Select file":
            return
        import os
        fname = f'CoughResults/{self.filelist.currentText().replace(".wav", ".xlsx")}'
        i=1
        if os.path.exists(fname):
            fname = fname.replace(".xlsx", f"_{i}.xlsx")
            while os.path.exists(fname):
                i+=1
                fname = fname.replace(f"_{i-1}.xlsx", f"_{i}.xlsx")
        self.df.to_excel(fname)
        QtWidgets.QMessageBox.information(self, 'Save succesful!',
            f"File saved as\n{fname}", QtWidgets.QMessageBox.Ok)
        
    def export_txt(self):
        if self.filelist.currentText()=="Select file":
            return
        import os
        fname = f'CoughResults/{self.filelist.currentText().replace(".wav", ".txt")}'
        i=1
        if os.path.exists(fname):
            fname = fname.replace(".txt", f"_{i}.txt")
            while os.path.exists(fname):
                i+=1
                fname = fname.replace(f"_{i-1}.txt", f"_{i}.txt")
        with open(fname, 'w+') as file:
            file.write(self.df.to_string())
        QtWidgets.QMessageBox.information(self, 'Save succesful!',
            f"File saved as\n{fname}", QtWidgets.QMessageBox.Ok)


    def initialize_files(self):
        import glob, os, pandas as pd, numpy as np
        self.pathIN_2.setText(pathIN)
        cwd = os.getcwd().replace("\\", "/")
        found = glob.glob(f"{cwd}/CoughResults/*.txt")
        files = glob.glob(f"{pathIN}/**/*.wav", recursive=True)
        self.df = pd.DataFrame()
        self.results.setPlainText("Please select a file to view cough segments detected.")
        self.results.setReadOnly(True)
        self.btn_listen.hide()
        self.btn_xlsx.hide()
        self.btn_txt.hide()

        if len(found)==0:
            self.filelist.addItem("-")
            self.results.setPlainText("No coughs found.")
            self.filelist.setEnabled(False)
        else:
            self.res_text = dict()
            self.extracted_wavs = dict()
            self.filelist.addItem("Select file")
            self.res_text["Select file"]="Please select a file to view cough segments detected."
            for f in found:
                cc = f.replace("\\", "/").split("/")[-1].split("_coughDetections.txt")[0]
                self.filelist.addItem(cc)
                self.df = pd.DataFrame(np.loadtxt(f)[:,1:], columns=["Time (s)", "Confidence"], index=np.loadtxt(f)[:,0].astype(int)) 
                self.res_text[cc] = self.df.to_string()
                self.extracted_wavs[cc] = f.replace(".txt", ".wav") #[fn for fn in files if cc in fn][0]

    def change_results(self):
        self.results.setPlainText(self.res_text[self.filelist.currentText()])
        check=self.filelist.currentText()!="Select file"
        if check:
            self.btn_listen.show()
            self.btn_xlsx.show()
            self.btn_txt.show()
        else:
            self.btn_listen.hide()
            self.btn_xlsx.hide()
            self.btn_txt.hide()
        # self.btn_listen.setEnabled(check)
        # self.btn_xlsx.setEnabled(check)
        # self.btn_txt.setEnabled(check)


    def listen_active_wav(self):
        if self.filelist.currentText()=="Select file":
            return
        from playsound import playsound
        playsound(self.extracted_wavs[self.filelist.currentText()])

    def run_main(self):
        global vpathIN, vvad_th,vprob_th, vcpus , model, del_temp
        vpathIN = self.pathIN.toPlainText()
        vcpus = int(self.num_of_threads.value())
        print("Starting execution. Please wait...")
        self.hide()
        main(vpathIN, vvad_th, \
         vprob_th, vcpus, del_temp = True, model=model, recursive = self.include_sub.isChecked())
        self.stackedWidget.setCurrentIndex(1)
        self.initialize_files()
        self.show()
        #QtCore.QCoreApplication.instance().quit()



class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    #Stack over flow - draggable window
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        try:
            self.setWindowIcon(QtGui.QIcon('/lib/resources/forth_disk.png'))
        except:
            pass
    def mousePressEvent(self, event):                                 # +
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()     



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec())