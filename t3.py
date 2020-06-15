import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import validator


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit = qtw.QLineEdit('', self)
        self.line_edit.setValidator(validator.IPV4Validator())
        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
