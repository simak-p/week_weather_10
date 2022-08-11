import json
import sys
from pprint import pprint
from wc_data import create_str_daily
from PySide6.QtGui import QScreen, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from form import Ui_MainWindow
from dw_weather import get_weather_dict, loc_to_coord
from my_dialog_charts import DialogCarts
from choose_city.choose_sity_dialog import ChooseCity
from history_dialog.histoey_dialog import HistoryDialog


def choose_dialog_show(city_list: list):
    choose_dialog = ChooseCity(city_list)
    if choose_dialog.exec() == QDialog.Accepted:
        return choose_dialog.return_index_data()
    else:
        pass
    choose_dialog.deleteLater()


def saved_data(data: list, name_file: str):
    with open(name_file, "w") as write_file:
        json.dump(data, write_file)


def load_data(name_File: str):
    with open(name_File, "r") as read_file:
        return json.load(read_file)


class MainWeather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mw_dict = {}
        # self.searce_list = []
        self.favorites_list = []
        self.history_list = []
        self.history_file = 'data_stor/history.json'
        self.label_list = [self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                           self.ui.label_5, self.ui.label_6, self.ui.label_7]
        self.ui.pushButtonsearce.clicked.connect(self.weather_from_name)
        self.ui.action_chart_week.triggered.connect(self.charts_show)
        self.ui.pushButton_history.clicked.connect(self.history_dialog_show)

        try:
            self.history_list = load_data(self.history_file)
        except FileNotFoundError:
            pass
        print(self.history_list)

    def weather_from_name(self):
        try:
            resp = loc_to_coord(self.ui.lineEdit_Cyty.text())
            searce_list = []
            for i in resp.json()['results']:
                searce_list.append(
                    f"{i['name']}  {i.get('country', 'нет данных')}  {i.get('admin1', 'нет данных')}  "
                    f"{i.get('latitude', 'нет данных')}  {i.get('longitude', 'нет данных')}")
            ret_list = choose_dialog_show(searce_list).split('  ')
            print('ret', ret_list)

            self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
            create_str_daily(self.mw_dict, self.label_list)
            # pprint(self.mw_dict)
            # pprint(self.mw_dict['hourly']['time'])
            self.history_list.insert(0, '  '.join(ret_list))
            print('history', self.history_list)
            saved_data(self.history_list, self.history_file)
        except KeyError:
            print('такого города не найдено')

    def weather_from_dialog(self, ret_list: list):
        self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
        create_str_daily(self.mw_dict, self.label_list)

    def charts_show(self):
        dialog_charts = DialogCarts(self.mw_dict['hourly'])
        dialog_charts.show()

    def history_dialog_show(self):
        history_dialog = HistoryDialog(self.history_list, self.favorites_list)
        # history_dialog.weather_action.triggered.connect(self.weather_from_dialog(history_dialog.))
        history_dialog.del_action.triggered.connect(self.save_history_list(history_dialog.delete_row()))
        history_dialog.exec()

    def save_history_list(self, history: list):
        print('his', history)
        self.history_list = history
        print('his. list', self.history_list)
        saved_data(self.history_list, self.history_file)


if __name__ == '__main__':
    app = QApplication()
    window = MainWeather()
    window.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width() / 1.5,
                  QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
    window.setWindowIcon(QIcon('program_icon.png'))
    window.setWindowTitle('Подробный прогноз погоды на неделю.')
    f = open('my_qssStyle.qss', 'r')
    with f:
        qss = f.read()
        window.setStyleSheet(qss)
    window.show()
    sys.exit(app.exec())
