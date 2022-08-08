from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QDialog
from dialog_searce import Ui_Dialog


class DialogSearce(QDialog):
    def __init__(self, searce_list: list = None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        f = open('my_qssStyle.qss', 'r')
        with f:
            qss = f.read()
            self.setStyleSheet(qss)
        self.searce_name = []
        for i in searce_list:
            self.searce_name.append(f"{i[0]}   {i[1]}")

        self.model = QStringListModel()
        self.model.setStringList(self.searce_name)
        self.ui.listView.setModel(self.model)
