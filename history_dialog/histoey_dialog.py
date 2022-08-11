from PySide6.QtCore import QStringListModel
from PySide6.QtGui import Qt, QAction
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
        self.ui.listView.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.add_favorite_action = QAction()
        self.add_favorite_action.setText('Добавить в избранное')
        self.ui.listView.addAction(self.add_favorite_action)

        self.del_action = QAction()
        self.del_action.setText('Delete')
        self.del_action.triggered.connect(self.delete_row)
        self.ui.listView.addAction(self.del_action)

        self.weather_action = QAction()
        self.weather_action.setText('Показать погоду')
        self.ui.listView.addAction(self.weather_action)

    def delete_row(self):
        self.ui.listView.model().removeRow(self.ui.listView.currentIndex().row())
        return self.history_model.stringList()
