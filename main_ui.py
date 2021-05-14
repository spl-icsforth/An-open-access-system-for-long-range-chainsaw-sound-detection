# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CHADv.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 3, 159, 255), stop:1 rgba(3, 0, 76, 255));\n"
"\n"
"border-radius: 10px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_min = QtWidgets.QPushButton(self.frame)
        self.btn_min.setGeometry(QtCore.QRect(510, 10, 21, 16))
        self.btn_min.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 255, 127, 150);\n"
"}")
        self.btn_min.setText("")
        self.btn_min.setObjectName("btn_min")
        self.btn_max = QtWidgets.QPushButton(self.frame)
        self.btn_max.setGeometry(QtCore.QRect(540, 10, 21, 16))
        self.btn_max.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(200, 130, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(200, 130, 0, 150);\n"
"}")
        self.btn_max.setText("")
        self.btn_max.setObjectName("btn_max")
        self.btn_exit = QtWidgets.QPushButton(self.frame)
        self.btn_exit.setGeometry(QtCore.QRect(570, 10, 21, 16))
        self.btn_exit.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(235,0,0, 150);\n"
"}")
        self.btn_exit.setText("")
        self.btn_exit.setObjectName("btn_exit")
        self.LOGO = QtWidgets.QFrame(self.frame)
        self.LOGO.setGeometry(QtCore.QRect(10, 40, 581, 60))
        self.LOGO.setStyleSheet("background-color: rgb(250,50, 50, 150);")
        self.LOGO.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LOGO.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LOGO.setObjectName("LOGO")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 530, 221, 91))
        self.pushButton_5.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(88, 255, 107, 150);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 109, 581, 401))
        self.frame_2.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.toolBox = QtWidgets.QToolBox(self.frame_2)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 581, 400))
        self.toolBox.setStyleSheet("")
        self.toolBox.setObjectName("toolBox")
        self.Dir = QtWidgets.QWidget()
        self.Dir.setGeometry(QtCore.QRect(0, 0, 581, 338))
        self.Dir.setStyleSheet("")
        self.Dir.setObjectName("Dir")
        self.btn_min_2 = QtWidgets.QPushButton(self.Dir)
        self.btn_min_2.setGeometry(QtCore.QRect(20, 0, 131, 61))
        self.btn_min_2.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 255, 127, 150);\n"
"}")
        self.btn_min_2.setObjectName("btn_min_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dir)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 271, 51))
        self.textBrowser.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea = QtWidgets.QScrollArea(self.Dir)
        self.scrollArea.setGeometry(QtCore.QRect(20, 130, 271, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 271, 141))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 271, 141))
        self.textBrowser_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(255, 0, 16, 141))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.checkBox = QtWidgets.QCheckBox(self.Dir)
        self.checkBox.setGeometry(QtCore.QRect(190, 15, 91, 32))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.Dir)
        self.checkBox_2.setGeometry(QtCore.QRect(25, 300, 265, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.toolBox.addItem(self.Dir, "")
        self.Params = QtWidgets.QWidget()
        self.Params.setGeometry(QtCore.QRect(0, 0, 581, 338))
        self.Params.setStyleSheet("")
        self.Params.setObjectName("Params")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Params)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 561, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 111, 58))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(340, 20, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 59))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 20, 51, 31))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(400, 20, 141, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 201, 58))
        self.label_5.setObjectName("label_5")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_6)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(400, 20, 141, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_6)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(310, 20, 51, 31))
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 58))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(182, 0, 371, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.toolBox.addItem(self.Params, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "RUN"))
        self.btn_min_2.setText(_translate("MainWindow", "Select\n"
"Directory"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C:/Users/.../test_files</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Files to be processed:\\n</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">abcd.wav</p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Include\n"
"Subfolders"))
        self.checkBox_2.setText(_translate("MainWindow", "Delete intermediate files"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Dir), _translate("MainWindow", "Directory selection"))
        self.label_3.setText(_translate("MainWindow", "Select model (for \n"
"classification):"))
        self.label_2.setText(_translate("MainWindow", "VAD threshold chosen: \n"
"[Can take any value \n"
"between 0.078-0.15]\""))
        self.label_5.setText(_translate("MainWindow", "Probability threshold chosen: \n"
"[Can take any value between 0-1]"))
        self.label.setText(_translate("MainWindow", "Parallelization:"))
        self.radioButton_4.setText(_translate("MainWindow", "No"))
        self.radioButton_3.setText(_translate("MainWindow", "Low"))
        self.radioButton_2.setText(_translate("MainWindow", "Mid"))
        self.radioButton.setText(_translate("MainWindow", "Full"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Params), _translate("MainWindow", "Advanced Parameters"))

