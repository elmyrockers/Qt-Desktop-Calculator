import sys
from PySide6.QtWidgets import QApplication
from calculator import Calculator  # import Calculator class

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

