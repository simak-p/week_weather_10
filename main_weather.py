import json
import sys
from pprint import pprint

from PySide6.QtCore import QStringListModel

from wc_data import create_str_daily, create_str_current
from PySide6.QtGui import QScreen, QIcon, QAction, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog
from form import Ui_MainWindow
from dw_weather import get_weather_dict, loc_to_coord
from my_dialog_charts import DialogCarts
from choose_city.choose_sity_dialog import ChooseCity


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

        self.favorites_list = []
        self.history_list = []
        self.favorites_file = 'data_stor/favorites.json'
        self.history_file = 'data_stor/history.json'
        self.history_model = QStringListModel()
        self.favorites_model = QStringListModel()

        self.label_list = [self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                           self.ui.label_5, self.ui.label_6, self.ui.label_7]
        self.ui.pushButton_searce.clicked.connect(self.weather_from_name)
        self.ui.action_chart_week.triggered.connect(self.charts_show)
        self.ui.action_weather_2.triggered.connect(self.show_weather)
        self.ui.action_favorites_2.triggered.connect(self.show_favorites)

        try:
            self.history_list = load_data(self.history_file)
            self.favorites_list = load_data(self.favorites_file)
        except FileNotFoundError:
            pass
        print(self.history_list)
        self.history_model.setStringList(self.history_list)
        self.ui.listView_history.setModel(self.history_model)

        self.favorites_model.setStringList(self.favorites_list)
        self.ui.listView_favorites.setModel(self.favorites_model)

        self.ui.listView_history.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.listView_favorites.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.delete_action = QAction('Удалить из истории')
        self.ui.listView_history.addAction(self.delete_action)
        self.delete_action.triggered.connect(self.remove_row_history_list)

        self.show_weather_action = QAction('Показать погоду')
        self.ui.listView_history.addAction(self.show_weather_action)
        self.show_weather_action.triggered.connect(self.weather_from_history)

        self.add_favorite_action = QAction('Добавить в избранное')
        self.ui.listView_history.addAction(self.add_favorite_action)
        self.add_favorite_action.triggered.connect(self.add_to_favorites)

        self.delete_favorites_action = QAction('Удалить мз избранного')
        self.ui.listView_favorites.addAction(self.delete_favorites_action)
        self.delete_favorites_action.triggered.connect(self.delete_row_favorites)

        self.show_weather_favorites_action = QAction('Показать погоду')
        self.ui.listView_favorites.addAction(self.show_weather_favorites_action)
        self.show_weather_favorites_action.triggered.connect(self.weather_from_favorite)

    def weather_from_name(self):
        try:
            resp = loc_to_coord(self.ui.lineEdit_city.text())
            searce_list = []
            for i in resp.json()['results']:
                searce_list.append(
                    f"{i['name']}  {i.get('country', 'нет данных')}  {i.get('admin1', 'нет данных')}  "
                    f"{i.get('latitude', 'нет данных')}  {i.get('longitude', 'нет данных')}")
            ret_list = choose_dialog_show(searce_list).split('  ')
            print('ret', ret_list)

            self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
            create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label_0)
            create_str_daily(self.mw_dict, self.label_list)
            pprint(self.mw_dict)
            self.history_list.insert(0, '  '.join(ret_list))
            print('history', self.history_list)
            saved_data(self.history_list, self.history_file)
        except KeyError:
            print('такого города не найдено')

    def weather_from_history(self):
        ret_list = self.ui.listView_history.currentIndex().data().split('  ')
        self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
        create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label_0)
        create_str_daily(self.mw_dict, self.label_list)
        self.ui.stackedWidget.setCurrentIndex(0)

    def weather_from_favorite(self):
        ret_list = self.ui.listView_favorites.currentIndex().data().split('  ')
        print('ret_list', ret_list)
        self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
        create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label_0)
        create_str_daily(self.mw_dict, self.label_list)
        self.ui.stackedWidget.setCurrentIndex(0)

    def charts_show(self):
        dialog_charts = DialogCarts(self.mw_dict['hourly'])
        dialog_charts.exec()

    def remove_row_history_list(self):
        self.ui.listView_history.model().removeRow(self.ui.listView_history.currentIndex().row())
        self.history_list = self.history_model.stringList()
        print('his. list', self.history_list)
        saved_data(self.history_list, self.history_file)

    def show_weather(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_favorites(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def add_to_favorites(self):
        self.favorites_list.insert(0, self.ui.listView_history.currentIndex().data())
        self.favorites_model.setStringList(self.favorites_list)
        saved_data(self.favorites_list, self.favorites_file)

    def delete_row_favorites(self):
        self.ui.listView_favorites.model().removeRow(self.ui.listView_favorites.currentIndex().row())
        self.favorites_list = self.favorites_model.stringList()
        saved_data(self.favorites_list, self.favorites_file)


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
