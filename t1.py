from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([''])
    window = QtWidgets.QWidget(windowTitle='你好')
    window.show()
    app.exec()