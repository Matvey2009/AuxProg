# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formcfNsRU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AuxProg(object):
    def setupUi(self, AuxProg):
        if not AuxProg.objectName():
            AuxProg.setObjectName(u"AuxProg")
        AuxProg.resize(600, 401)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        AuxProg.setFont(font)
        AuxProg.setCursor(QCursor(Qt.WhatsThisCursor))
        icon = QIcon()
        icon.addFile(u"../../../Pictures/botton.png", QSize(), QIcon.Normal, QIcon.Off)
        AuxProg.setWindowIcon(icon)
        AuxProg.setStyleSheet(u"QMainWindow {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(123, 123, 123, 255), stop:1 rgba(50, 50, 50, 255));\n"
"}\n"
"\n"
".QPushButton {\n"
"	\n"
"	background-color: rgba(135, 135, 135, 200);\n"
"}\n"
"\n"
"#pushButton\n"
"{\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(AuxProg)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-30, 90, 641, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-10, 220, 641, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 30, 91, 51))
        self.textEdit.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(260, 30, 91, 51))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(440, 30, 91, 51))
        self.textEdit_3.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(40, 130, 191, 81))
        self.textEdit_4.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(380, 130, 191, 81))
        self.textEdit_5.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(50, 260, 171, 71))
        self.textEdit_6.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.textEdit_7 = QTextEdit(self.centralwidget)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(390, 260, 171, 71))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.textEdit_7.setFont(font1)
        self.textEdit_7.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 3, 61, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 10, 48, 13))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 10, 81, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 110, 131, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 110, 131, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 240, 48, 13))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(450, 240, 61, 20))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 330, 161, 51))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 240, 111, 20))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(280, 100, 48, 13))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(250, 80, 101, 16))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 320, 111, 41))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ButtonClick = QPushButton(self.centralwidget)
        self.ButtonClick.setObjectName(u"ButtonClick")
        self.ButtonClick.setGeometry(QRect(260, 160, 75, 23))
        AuxProg.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AuxProg)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        AuxProg.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AuxProg)
        self.statusbar.setObjectName(u"statusbar")
        AuxProg.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(AuxProg)
        self.ButtonClick.clicked.connect(self.textEdit_5.hide)
        self.ButtonClick.clicked.connect(self.label.setFocus)

        QMetaObject.connectSlotsByName(AuxProg)
    # setupUi

    def retranslateUi(self, AuxProg):
        AuxProg.setWindowTitle(QCoreApplication.translate("AuxProg", u"AuxProg", None))
        self.label.setText(QCoreApplication.translate("AuxProg", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("AuxProg", u"\u0421\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.label_3.setText(QCoreApplication.translate("AuxProg", u"\u041c\u0438\u043b\u0438\u0441\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.label_4.setText(QCoreApplication.translate("AuxProg", u"\u041a\u043d\u043e\u043f\u043a\u0430 \u043d\u0430 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0440\u0443\u0440\u0435", None))
        self.label_5.setText(QCoreApplication.translate("AuxProg", u"\u041a\u043d\u043e\u043f\u043a\u0430 \u043d\u0430 \u043c\u044b\u0448\u043a\u0435", None))
        self.label_6.setText(QCoreApplication.translate("AuxProg", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("AuxProg", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("AuxProg", u"\u0413\u043e\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438", None))
        self.label_10.setText(QCoreApplication.translate("AuxProg", u"\u041a\u043d\u043e\u043f\u043a\u0438", None))
        self.label_11.setText(QCoreApplication.translate("AuxProg", u"\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0432\u0442\u0430\u0440\u0435\u043d\u0438\u044f", None))
        self.label_12.setText(QCoreApplication.translate("AuxProg", u"AuxProg", None))
        self.ButtonClick.setText(QCoreApplication.translate("AuxProg", u"PushButton", None))
        self.menu.setTitle(QCoreApplication.translate("AuxProg", u"\u0410\u0432\u0442\u043e\u041a\u043b\u0438\u043a\u0435\u0440", None))
    # retranslateUi

