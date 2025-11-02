
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from calculator_ui import Ui_MainWindow  # the generated file

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())
