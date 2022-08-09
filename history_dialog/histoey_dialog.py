from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QDialog

from history_dialog.history_form import Ui_Dialog


class HistoryDialog(QDialog):
    def __init__(self, history_list: list, favorites_list: list):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        f = open('my_qssStyle.qss', 'r')
        with f:
            qss = f.read()
            self.setStyleSheet(qss)
        self.history_model = QStringListModel()
        self.history_model.setStringList(history_list)
        self.ui.listView.setModel(self.history_model)

    def remove_row(self):
        self.ui.listView.model().removeRow(self.ui.listView.currentIndex().row())

    def show_weather(self):
        return self.ui.listView.currentIndex().data()

    def add_row_favorites(self, favorites_list: list):
        favorites_list.insert(0, self.ui.listView.currentIndex().data())
