import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase
from qt_material import apply_stylesheet
from calculator import Calculator  # import Calculator class

def main():
    app = QApplication(sys.argv)

    # Apply a dark theme
    apply_stylesheet(app, theme='dark_teal.xml')

    window = Calculator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

