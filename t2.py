import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.wg = qtw.QLineEdit('def', self, placeholderText='输入', clearButtonEnabled=True,
                                maxLength=20)
        #self.setAttribute(qtc.Qt.WA_InputMethodEnabled)
        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
