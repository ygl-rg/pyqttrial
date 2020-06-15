import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('日历应用')
        self.resize(800, 600)
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        self.calendar = qtw.QCalendarWidget()
        main_layout.addWidget(self.calendar)
        self.calendar.setSizePolicy(qtw.QSizePolicy.Expanding,
                                    qtw.QSizePolicy.Expanding)
        right_layout = qtw.QVBoxLayout()
        main_layout.addLayout(right_layout)
        right_layout.addWidget(qtw.QLabel('日期事件'))

        self.events = qtw.QListWidget()
        right_layout.addWidget(self.events)
        self.events.setSizePolicy(qtw.QSizePolicy.Expanding,
                                  qtw.QSizePolicy.Expanding)

        event_form = qtw.QGroupBox('事件')
        right_layout.addWidget(event_form)
        event_form_layout = qtw.QGridLayout()
        event_form.setLayout(event_form_layout)


        self.event_title = qtw.QLineEdit()
        event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)

        self.event_category = qtw.QComboBox()
        event_form_layout.addWidget(self.event_category, 2, 1)
        self.event_category.addItems(['Select category', 'New...', 'NY...', 'Meeting'])
        self.event_category.model().item(0).setEnabled(False)

        self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
        event_form_layout.addWidget(self.event_time, 2, 2)

        self.all_day_check = qtw.QCheckBox('全日')
        event_form_layout.addWidget(self.all_day_check, 2, 3)

        self.event_detail = qtw.QTextEdit()
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)

        self.add_btn = qtw.QPushButton('增加/更新')
        event_form_layout.addWidget(self.add_btn, 4, 2)
        self.del_btn = qtw.QPushButton('删除')
        event_form_layout.addWidget(self.del_btn, 4, 3)
        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
