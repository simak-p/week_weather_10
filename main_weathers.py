import json
import sys
from copy import copy
from pprint import pprint

from PySide6 import QtGui
from PySide6.QtCore import QStringListModel

from wc_data import create_str_daily, create_str_current
from PySide6.QtGui import QScreen, QIcon, QAction, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar
from main_form import Ui_MainWindow
from dw_weather import get_weather_dict, loc_to_coord
from my_dialog_charts import DialogCarts
import pysnooper


def saved_data(data: [list, dict], name_file: str):  # аргументы: данные и имя файла
    with open(name_file, "w") as write_file:  # открываем файл для записи
        json.dump(data, write_file)  # записываем данные


# читает данные из файла
def load_data(name_file: str):  # аргумент: имя файла
    with open(name_file, "r") as read_file:  # открываем файл для чтения
        return json.load(read_file)  # возвращает данные


class MainWeather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mw_dict = {}

        self.history_list = []
        self.by_popularity_dict = {}
        self.history_file = 'data_stor/history.json'
        self.popularity_file = 'data_stor/popularity.json'
        self.history_model = QStringListModel()
        self.favorites_model = QStringListModel()
        self.searce_model = QStringListModel()

        try:
            self.history_list = load_data(self.history_file)
            self.by_popularity_dict = load_data(self.popularity_file)
        except FileNotFoundError:
            pass

        self.history_model.setStringList(self.history_list)
        self.ui.listView_history.setModel(self.history_model)

        self.favorites_model.setStringList(list(self.by_popularity_dict))
        self.ui.listView_favorites.setModel(self.favorites_model)

        self.ui.listView_history.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ui.listView_favorites.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.tool_bar = QToolBar('Окна')
        self.tool_bar.setOrientation(Qt.Orientation.Vertical)
        self.searce_action = QAction('Поиск')
        self.favorites_action = QAction('Избранное')
        self.history_action = QAction('История')
        self.charts_action = QAction('Графики')
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.searce_action)
        self.tool_bar.addAction(self.favorites_action)
        self.tool_bar.addAction(self.history_action)
        self.tool_bar.addAction(self.charts_action)
        self.addToolBar(self.tool_bar)

        self.searce_action.triggered.connect(self.searce_state)
        self.history_action.triggered.connect(self.history_state)
        self.favorites_action.triggered.connect(self.favorites_state)
        self.charts_action.triggered.connect(self.charts_show)

        self.ui.dockWidget_searce.setVisible(False)
        self.ui.dockWidget_favorites.setVisible(False)
        self.ui.dockWidget_history.setVisible(False)

        self.label_list = [self.ui.label_0, self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                           self.ui.label_5, self.ui.label_6]

        self.ui.pushButton_searce.clicked.connect(self.chose_list_from_name)

        self.chose_action = QAction('Выбрать')
        self.chose_action.triggered.connect(self.weather_from_searce_list)
        self.ui.listView_searce.addAction(self.chose_action)

        self.delete_action = QAction('Удалить из истории')
        self.ui.listView_history.addAction(self.delete_action)
        self.delete_action.triggered.connect(self.remove_row_history_list)

        self.add_favorite_action = QAction('Добавить в избранное')
        self.ui.listView_history.addAction(self.add_favorite_action)
        self.add_favorite_action.triggered.connect(self.add_to_favorites)

        self.delete_favorites_action = QAction('Удалить мз избранного')
        self.ui.listView_favorites.addAction(self.delete_favorites_action)
        self.delete_favorites_action.triggered.connect(self.delete_row_favorites)

        self.show_weather_favorites_action = QAction('Показать погоду')
        self.ui.listView_favorites.addAction(self.show_weather_favorites_action)
        self.show_weather_favorites_action.triggered.connect(self.weather_from_favorite)

        self.show_weather_history_action = QAction('Показать погоду')
        self.ui.listView_history.addAction(self.show_weather_history_action)
        self.show_weather_history_action.triggered.connect(self.weather_from_history)

        self.popularity_action = QAction('Сортировать по популярности')
        self.ui.listView_favorites.addAction(self.popularity_action)
        self.popularity_action.triggered.connect(self.sorted_popularity)

        self.abc_action = QAction('Сортировать по алфавиту')
        self.ui.listView_favorites.addAction(self.abc_action)
        self.popularity_action.triggered.connect(self.sorted_abc)

    def remove_row_history_list(self):
        self.ui.listView_history.model().removeRow(self.ui.listView_history.currentIndex().row())
        self.history_list = self.history_model.stringList()
        print('his. list', self.history_list)
        saved_data(self.history_list, self.history_file)

    def add_to_favorites(self):
        if self.ui.listView_history.currentIndex().data() not in list(self.by_popularity_dict.keys()):
            self.by_popularity_dict[self.ui.listView_history.currentIndex().data()] = 0
            self.favorites_model.setStringList(list(self.by_popularity_dict))
            saved_data(self.by_popularity_dict, self.popularity_file)
        else:
            print('Этот город был добавлен ранее.')

    def delete_row_favorites(self):
        self.ui.listView_favorites.model().removeRow(self.ui.listView_favorites.currentIndex().row())
        for i in list(self.by_popularity_dict):
            if i not in self.favorites_model.stringList():
                del (self.by_popularity_dict[i])
        saved_data(self.by_popularity_dict, self.popularity_file)

    def charts_show(self):
        dialog_charts = DialogCarts(self.mw_dict['hourly'])
        file = open('my_qssStyle.qss', 'r')
        with file:
            my_qss = file.read()
            dialog_charts.setStyleSheet(my_qss)
        dialog_charts.exec()

    def favorites_state(self):
        if self.ui.dockWidget_favorites.isVisible():
            self.ui.dockWidget_favorites.setVisible(False)
        elif not self.ui.dockWidget_favorites.isVisible():
            self.ui.dockWidget_favorites.setVisible(True)

    def history_state(self):
        if self.ui.dockWidget_history.isVisible():
            self.ui.dockWidget_history.setVisible(False)
        elif not self.ui.dockWidget_history.isVisible():
            self.ui.dockWidget_history.setVisible(True)

    def searce_state(self):
        if self.ui.dockWidget_searce.isVisible():
            self.ui.dockWidget_searce.setVisible(False)
        elif not self.ui.dockWidget_searce.isVisible():
            self.ui.dockWidget_searce.setVisible(True)

    @pysnooper.snoop()
    def chose_list_from_name(self):
        try:
            resp = loc_to_coord(self.ui.lineEdit_searce.text())
            searce_list = []
            for i in resp.json()['results']:
                searce_list.append(
                    f"{i['name']}  {i.get('country', 'нет данных')}  {i.get('admin1', 'нет данных')}  "
                    f"{i.get('latitude', 'нет данных')}  {i.get('longitude', 'нет данных')}")
            self.searce_model.setStringList(searce_list)
            self.ui.listView_searce.setModel(self.searce_model)
        except KeyError:
            print('Такой город не найден')

    def weather_from_searce_list(self):
        try:
            ret_list = self.ui.listView_searce.currentIndex().data().split('  ')
            self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
            create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label)
            create_str_daily(self.mw_dict, self.label_list)
            pprint(self.mw_dict)
            self.history_list.insert(0, '  '.join(ret_list))
            if len(self.history_list) > 50:
                del self.history_list[50:]
            self.history_model.setStringList(self.history_list)
            self.ui.listView_history.setModel(self.history_model)
            print('history', self.history_list)
            saved_data(self.history_list, self.history_file)
        except KeyError:
            pass

    def weather_from_history(self):
        ret_list = self.ui.listView_history.currentIndex().data().split('  ')
        self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
        create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label)
        create_str_daily(self.mw_dict, self.label_list)
        self.history_list.insert(0, '  '.join(ret_list))
        self.history_model.setStringList(self.history_list)
        self.ui.listView_history.setModel(self.history_model)
        print('history', self.history_list)
        saved_data(self.history_list, self.history_file)

    @pysnooper.snoop()
    def weather_from_favorite(self):
        ret_list = self.ui.listView_favorites.currentIndex().data().split('  ')
        print('ret_list', ret_list)
        self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
        create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label)
        create_str_daily(self.mw_dict, self.label_list)
        self.history_list.insert(0, '  '.join(ret_list))
        self.history_model.setStringList(self.history_list)
        self.ui.listView_history.setModel(self.history_model)
        # print('history', self.history_list)
        saved_data(self.history_list, self.history_file)

        city = self.ui.listView_favorites.currentIndex().data()
        for key in self.by_popularity_dict.keys():
            if key == city:
                self.by_popularity_dict[key] += 1
                sorted_dict = dict(sorted(self.by_popularity_dict.items(), key=lambda item: item[1], reverse=True))
                self.by_popularity_dict = copy(sorted_dict)
                print(self.by_popularity_dict)
                saved_data(sorted_dict, self.popularity_file)

    def sorted_popularity(self):
        city_list = list(self.by_popularity_dict)
        self.favorites_model.setStringList(city_list)
        saved_data(self.by_popularity_dict, self.popularity_file)

    def sorted_abc(self):
        city_list = list(self.by_popularity_dict)
        city_list.sort()
        self.favorites_model.setStringList(city_list)
        # saved_data(self.by_popularity_dict, self.popularity_file)


if __name__ == '__main__':
    app = QApplication()
    QtGui.QFontDatabase.addApplicationFont('roboto/Roboto-BoldItalic.ttf')
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
