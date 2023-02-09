from pprint import pprint

from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QDialog, QMessageBox

from weather_app.dw_weather import loc_to_coord
from weather_app.searce_dialog.searce_dialog import Ui_Dialog_searce


class Dialog_searce(QDialog):
    def __init__(self):
        super(Dialog_searce, self).__init__()
        self.ui = Ui_Dialog_searce()
        self.ui.setupUi(self)

        self.searce_list = []

        self.ui.pushButton_searce.clicked.connect(self.chose_list_from_name)

        self.ui.lineEdit_searce.setPlaceholderText('Впишите название города')

    def chose_list_from_name(self):
        """

        :return:
        """
        searce_model = QStringListModel()
        try:
            resp = loc_to_coord(self.ui.lineEdit_searce.text())
            pprint(resp.json())
            for i in resp.json()['results']:
                self.searce_list.append(
                    f"{i['name']}  {i.get('country', 'нет данных')}  {i.get('admin1', 'нет данных')}  "
                    f"{i.get('latitude', 'нет данных')}  {i.get('longitude', 'нет данных')}"
                    f"  {i.get('timezone', 'нет данных')}")
            searce_model.setStringList(self.searce_list)
            self.ui.listView_searce.setModel(searce_model)
        except KeyError:
            print('Такой город не найден')
        QMessageBox.information(self, 'Теперь нужно выбрать город.',
                                'Выделите город из списка.',
                                QMessageBox.Ok)
