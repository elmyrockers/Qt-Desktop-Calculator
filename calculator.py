from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from calculator_ui import Ui_MainWindow  # your generated UI

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_buttons()
        self.setup_menu()

    # --------------------------
    # Button functionality
    # --------------------------
    def setup_buttons(self):
        # Number buttons
        for i in range(10):
            getattr(self.ui, f'pb{i}').clicked.connect(lambda checked, x=i: self.update_display(str(x)))

        # Operators
        self.ui.pbAdd.clicked.connect(lambda: self.update_display('+'))
        self.ui.pbSubtract.clicked.connect(lambda: self.update_display('-'))
        self.ui.pbMultiply.clicked.connect(lambda: self.update_display('*'))
        self.ui.pbDivide.clicked.connect(lambda: self.update_display('/'))
        self.ui.pbDot.clicked.connect(lambda: self.update_display('.'))
        self.ui.pbPercent.clicked.connect(self.percent)

        # Special buttons
        self.ui.pbC.clicked.connect(self.clear)
        self.ui.pbCE.clicked.connect(self.clear_entry)
        self.ui.pbBackspace.clicked.connect(self.backspace)
        self.ui.pbEqual.clicked.connect(self.calculate)

    def update_display(self, value):
        current = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(current + value)

    def clear(self):
        self.ui.lineEdit.setText('')

    def clear_entry(self):
        self.ui.lineEdit.setText('')

    def backspace(self):
        current = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(current[:-1])

    def percent(self):
        try:
            value = float(self.ui.lineEdit.text()) / 100
            self.ui.lineEdit.setText(str(value))
        except ValueError:
            pass

    def calculate(self):
        try:
            result = str(eval(self.ui.lineEdit.text()))
            self.ui.lineEdit.setText(result)
        except Exception:
            self.ui.lineEdit.setText("Error")

    # --------------------------
    # Menu functionality
    # --------------------------
    def setup_menu(self):
        # File -> Exit
        self.ui.menuExit.triggered.connect(self.close)

        # Edit -> Copy, Paste
        self.ui.menuCopy.triggered.connect(self.copy_text)
        self.ui.menuPaste.triggered.connect(self.paste_text)

        # View -> Standard, Scientific Mode
        self.ui.menuStandard.triggered.connect(lambda: self.show_message( "View","Standard Mode"))
        self.ui.menuScientificMode.triggered.connect(lambda: self.show_message( "View","Scientific Mode"))

        # Help -> About
        self.ui.menuAboutApp.triggered.connect(lambda: self.show_message( "About App","Qt Desktop Calculator v1.0"))
        self.ui.menuAboutDeveloper.triggered.connect(self.show_about_developer)
        self.ui.menuVisitWebsite.triggered.connect(self.open_website)

    # Menu actions
    def copy_text(self):
        text = self.ui.lineEdit.text()
        QApplication.clipboard().setText(text)

    def paste_text(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        self.update_display(text)

    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

    def show_about_developer(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("About Developer")
        msg.setIcon(QMessageBox.Information)

        html_content = """
        <h2>Developer Info</h2>
        <p><b style="font-size:10pt;">Name:</b> Helmi Aziz (elmyrockers)</p>
        <p><b style="font-size:10pt;">Title:</b> Fullstack Software Developer / Web Developer</p>
        <p><b style="font-size:10pt;">About:</b><br>I create desktop, web and mobile applications. Passionate about coding and building efficient software solutions.</p>
        <p><b style="font-size:10pt;">Contact:</b> helmi@xeno.com.my</p>
        <p><b style="font-size:10pt;">Website:</b> https://elmyrockers.github.io</p>
        """

        msg.setTextFormat(Qt.RichText)
        msg.setText(html_content)
        msg.exec()

    def open_website(self):
        url = "https://elmyrockers.github.io"
        QDesktopServices.openUrl(QUrl(url))