
from PySide2 import QtCore, QtWidgets
from modules.Form import Ui_AuxProg
import pyautogui as a

class Main(Ui_AuxProg, QtWidgets.QMainWindow):
    """ Код автокликера """
    def __init__(self):
        super().__init__()
        self.click_x = 0
        self.click_y = 0
        self.setupUi(self)
        self.installEventFilter(self)
        self.show()
        # Сигналы - Слоты
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.autoclick)
        self.click_status = False
        self.ButtonClick.clicked.connect(self.Button_Click)

    def Button_Click(self):
        """ Переключатель Автоклика """
        self.click_status = not self.click_status
        if self.click_status:
            self.timer.start()
            self.autoclick()
            self.ButtonClick.setText("Stop")
        else:
            self.timer.stop()
            self.ButtonClick.setText("Start")

    def autoclick(self):
        """ Автоклик """
        a.tripleClick()
    def mouseMoveEvent(self, e):
        """ Позицыя курсора """
        self.label_6.setText(str(e.x()))
        self.label_7.setText(str(e.y()))

    def keyPressEvent(self, e):
        """ Горячие клавиши """
        if e.key():
            self.label_5.setText(str(chr(e.key())))
        e.assept()
