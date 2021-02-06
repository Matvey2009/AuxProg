# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0opUYJG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(220, 156)
        icon = QIcon()
        icon.addFile(u"D:/Documents/Pictures/\u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 50, 111, 61))
        self.pushButton.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 4px solid rgb(255, 0, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Pos_x = QLabel(Form)
        self.Pos_x.setObjectName(u"Pos_x")
        self.Pos_x.setGeometry(QRect(30, 130, 51, 21))
        self.Pos_x.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(255, 0, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Pos_y = QLabel(Form)
        self.Pos_y.setObjectName(u"Pos_y")
        self.Pos_y.setGeometry(QRect(130, 130, 51, 21))
        self.Pos_y.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(255, 0, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Xp = QLabel(Form)
        self.Xp.setObjectName(u"Xp")
        self.Xp.setGeometry(QRect(40, 110, 48, 13))
        self.Xp.setStyleSheet(u"QWidget\n"
"{\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Yp = QLabel(Form)
        self.Yp.setObjectName(u"Yp")
        self.Yp.setGeometry(QRect(130, 110, 48, 13))
        self.Yp.setStyleSheet(u"QWidget\n"
"{\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Freething = QCheckBox(Form)
        self.Freething.setObjectName(u"Freething")
        self.Freething.setGeometry(QRect(130, 20, 91, 17))
        self.Freething.setStyleSheet(u"QWidget\n"
"{\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.KOL_CLICK_SEK = QLineEdit(Form)
        self.KOL_CLICK_SEK.setObjectName(u"KOL_CLICK_SEK")
        self.KOL_CLICK_SEK.setGeometry(QRect(10, 20, 91, 20))
        self.KOL_CLICK_SEK.setStyleSheet(u"QWidget\n"
"{\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Kol_click_sek = QLabel(Form)
        self.Kol_click_sek.setObjectName(u"Kol_click_sek")
        self.Kol_click_sek.setGeometry(QRect(0, 0, 111, 16))
        self.Kol_click_sek.setStyleSheet(u"QWidget\n"
"{\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.Fon = QGraphicsView(Form)
        self.Fon.setObjectName(u"Fon")
        self.Fon.setGeometry(QRect(-20, -20, 256, 192))
        self.Fon.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.318182 rgba(5, 5, 5, 255), stop:0.965909 rgba(255, 255, , 255));\n"
"}")
        self.Fon.raise_()
        self.pushButton.raise_()
        self.Pos_x.raise_()
        self.Pos_y.raise_()
        self.Xp.raise_()
        self.Yp.raise_()
        self.Freething.raise_()
        self.KOL_CLICK_SEK.raise_()
        self.Kol_click_sek.raise_()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AuxProg", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0436\u0438\u043c\u0430\u0439 \u0441\u044e\u0434\u0430", None))
        self.Pos_x.setText("")
        self.Pos_y.setText("")
        self.Xp.setText(QCoreApplication.translate("Form", u"      X", None))
        self.Yp.setText(QCoreApplication.translate("Form", u"      Y", None))
        self.Freething.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043c\u0430\u043e\u0440\u043e\u0437\u043a\u0430", None))
        self.Kol_click_sek.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u043a\u043e\u0432", None))
    # retranslateUi

