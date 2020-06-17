import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)
        char_count_label = qtw.QLabel("chars: 0")
        self.text_edit.textChanged.connect(lambda: char_count_label.setText("chars: {0}".format(len(self.text_edit.toPlainText()))))
        self.statusBar().addPermanentWidget(char_count_label)
        file_menu = self.menuBar().addMenu('文件')
        file_menu.addAction('打开', self.open_file)
        file_menu.addAction('设置字体', self.set_font)
        file_menu.addAction('退出', self.close)

        toolbar1 = self.addToolBar('文件')
        toolbar1.addAction('保存')

        dock = qtw.QDockWidget("Replace")
        self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)
        self.show()

    def open_file(self):
        file_name = qtw.QFileDialog.getOpenFileName(self, initialFilter='*.py')
        print(file_name)

    def show_question(self):
        result = qtw.QMessageBox.question(self, "测试", "是否打开")
        print(result)

    def set_font(self):
        current = self.text_edit.currentFont()
        font, accepted = qtw.QFontDialog.getFont(current, self)
        if accepted:
            self.text_edit.setCurrentFont(font)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
