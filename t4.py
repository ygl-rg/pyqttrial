import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.event_table = {}
        self.setWindowTitle('日历应用')
        self.resize(800, 600)
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        self.calendar = qtw.QCalendarWidget()
        self.calendar.selectionChanged.connect(self.populate_list)
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
        self.events.itemSelectionChanged.connect(self.populate_form)

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
        self.event_category.currentIndexChanged[str].connect(self.on_category_change)

        self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
        event_form_layout.addWidget(self.event_time, 2, 2)

        self.all_day_check = qtw.QCheckBox('全日')
        self.all_day_check.toggled.connect(self.event_time.setDisabled)
        event_form_layout.addWidget(self.all_day_check, 2, 3)

        self.event_detail = qtw.QTextEdit()
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)

        self.add_btn = qtw.QPushButton('增加/更新')
        self.add_btn.clicked.connect(self.save_event)
        event_form_layout.addWidget(self.add_btn, 4, 2)

        self.del_btn = qtw.QPushButton('删除')
        self.del_btn.clicked.connect(self.delete_event)
        event_form_layout.addWidget(self.del_btn, 4, 3)
        self.events.itemSelectionChanged.connect(self.check_delete_btn)

        self.quit_btn = qtw.QPushButton('退出')
        event_form_layout.addWidget(self.quit_btn, 4, 4)
        self.quit_btn.clicked.connect(self.close)
        self.show()

    def clear_form(self):
        self.event_title.clear()
        self.event_category.setCurrentIndex(0)
        self.event_time.setTime(qtc.QTime(8, 0))
        self.all_day_check.setChecked(False)
        self.event_detail.setPlainText('')

    def populate_list(self):
        self.events.clear()
        self.clear_form()
        date = self.calendar.selectedDate()
        for event in self.event_table.get(date, []):
            time_obj = event['time'].toString('hh:mm') if event['time'] else '全日'
            self.events.addItem(f"{time_obj}: {event['title']}")

    def populate_form(self):
        self.clear_form()
        date = self.calendar.selectedDate()
        event_nu = self.events.currentRow()
        if event_nu == -1:
            return
        event_data = self.event_table.get(date)[event_nu]
        self.event_category.setCurrentText(event_data['category'])
        if event_data['time'] is None:
            self.all_day_check.setChecked(True)
        else:
            self.event_time.setTime(event_data['time'])
        self.event_title.setText(event_data['title'])
        self.event_detail.setPlainText(event_data['detail'])

    def save_event(self):
        event = {
            'category': self.event_category.currentText(),
            'time': (None if self.all_day_check.isChecked() else self.event_time.time()),
            'title': self.event_title.text(),
            'detail': self.event_detail.toPlainText()
        }
        date = self.calendar.selectedDate()
        event_list = self.event_table.get(date, [])
        event_nu = self.events.currentRow()
        if event_nu == -1:
            event_list.append(event)
        else:
            event_list[event_nu] = event
        event_list.sort(key=lambda x: x['time'] or qtc.QTime(0, 0))
        self.event_table[date] = event_list
        self.populate_list()

    def delete_event(self):
        date = self.calendar.selectedDate()
        row = self.events.currentRow()
        del (self.event_table[date][row])
        self.events.setCurrentRow(-1)
        self.clear_form()
        self.populate_list()

    def check_delete_btn(self):
        self.del_btn.setDisabled(self.events.currentRow() == -1)

    def add_category(self, category):
        self.event_category.addItem(category)
        self.event_category.setCurrentText(category)

    def on_category_change(self, text):
        if text == 'New...':
            self.form = CategoryWindow()
            self.form.submitted.connect(self.add_category)
            self.event_category.setCurrentIndex(0)


class CategoryWindow(qtw.QWidget):
    submitted = qtc.pyqtSignal(str)

    def __init__(self):
        super().__init__(None)
        self.setWindowModality(qtc.Qt.WindowModal)
        self.resize(640, 480)
        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(qtw.QLabel('Please enter a new catgory name:'))
        self.category_entry = qtw.QLineEdit()
        self.layout().addWidget(self.category_entry)
        self.submit_btn = qtw.QPushButton('Submit', clicked=self.onSubmit)
        self.layout().addWidget(self.submit_btn)
        self.cancel_btn = qtw.QPushButton('Cancel', clicked=self.close)
        self.layout().addWidget(self.cancel_btn)
        self.show()


    @qtc.pyqtSlot()
    def onSubmit(self):
        if self.category_entry.text():
            self.submitted.emit(self.category_entry.text())
        self.close()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
