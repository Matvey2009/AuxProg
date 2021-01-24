
from PySide2 import QtCore
from modules.Form import Ui_AuxProg
import pyautogui as a

class Main(Ui_AuxProg):
    """ Код автокликера """
    def __init__(self):
        super().__init__()
        self.click_x = 0
        self.click_y = 0
        self.setupUi(self)
        self.show()
        # Сигналы - Слоты
        self.click_status = False
        self.ButtonClick.clicked.connect(self.Button_Click)

    def Button_Click(self):
        self.click_status = not self.click_status
        if self.click_status:
            self.autoclick()

    def autoclick(self):
        while True:
            a.tripleClick()
            print("x")
