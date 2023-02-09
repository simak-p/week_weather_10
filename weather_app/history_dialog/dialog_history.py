import json

from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QDialogButtonBox, QDialog

from weather_app.history_dialog.history_dialog import Ui_Dialog


class DialogHistory(QDialog):
    def __init__(self):
        super(DialogHistory, self).__init__()
        self.history_list = []
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.weather_button = self.ui.buttonBox.addButton('Показать погоду', QDialogButtonBox.ButtonRole.AcceptRole)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.accepted.connect(self.accept)
