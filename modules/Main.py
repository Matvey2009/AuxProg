import sys
from PySide2 import QtWidgets
from modules.Form import Ui_AuxProg
import pyautogui as a

class Main(object):
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    ui_AuxProg = Ui_AuxProg()
    ui_AuxProg.setupUi(form)
    form.show()

    def test1(self):
        print("privet")
        print(a.position())

    def test2(self):
        self.ui_AuxProg.label_10.setText("Макросы")


    ui_AuxProg.ButtonClick.clicked.connect(test1)
    ui_AuxProg.ButtonClick.pressed.connect(test2)

    sys.exit(app.exec_())