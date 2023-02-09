from PySide6.QtWidgets import QDialog, QDialogButtonBox

from weather_app.favorites_dialog.favorites_dialog import Ui_Dialog_favorites


class DialogFavorite(QDialog):
    def __init__(self):
        super(DialogFavorite, self).__init__()
        self.ui = Ui_Dialog_favorites()
        self.ui.setupUi(self)

        self.weather_button = self.ui.buttonBox.addButton('Показать погоду', QDialogButtonBox.ButtonRole.AcceptRole)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.accepted.connect(self.accept)
