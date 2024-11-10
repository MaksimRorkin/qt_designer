from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

import random

from ui import Ui_MainWindow

app = QApplication([])

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Button_generate.clicked.connect(self.example)

    def example(self):
        symbols = ""

        if self.ui.Ceck_numbers.isChecked():
            symbols = "1234567890"
        if self.ui.checkBox_letters.isChecked():
            symbols += "qwertyuiopasdfghjklzxcvbnm"

        password = ""

        for i in range(random.randint(5, 10)):
            password += random.choise(symbols)

        self.ui.label_result.setText(password)




window = Widget()
window.show()
app.exec_()