import json
import sys
from copy import copy

from PySide6 import QtGui
from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QScreen, QIcon, QAction, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QMessageBox

from my_dialog_charts import DialogCarts
from searce_dialog.dialog_searce import Dialog_searce
from wc_data import create_str_daily, create_str_current
from weather_app.dictionary_sort import count_sorted_list, abc_sorted_list
from weather_app.dw_weather import get_weather_dict
from weather_app.favorites_dialog.dialog_favorite import DialogFavorite
from weather_app.history_dialog.dialog_history import DialogHistory
from weather_app.main_form import Ui_MainWindow


def saved_data(data: [list, dict], name_file: str):  # аргументы: данные и имя файла
    """

    :param data:
    :param name_file:
    :return:
    """
    with open(name_file, "w") as write_file:  # открываем файл для записи
        json.dump(data, write_file)  # записываем данные


# читает данные из файла
def load_data(name_file: str):  # аргумент: имя файла
    """

    :param name_file:
    :return:
    """
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
        self.dialog_history = DialogHistory()
        self.dialog_searce = Dialog_searce()
        self.dialog_favorite = DialogFavorite()

        try:
            self.history_list = load_data(self.history_file)
            self.by_popularity_dict = load_data(self.popularity_file)
        except FileNotFoundError:
            pass

        self.history_model = QStringListModel()
        self.history_model.setStringList(self.history_list)

        self.favorites_model = QStringListModel()
        self.favorites_model.setStringList(list(self.by_popularity_dict.keys()))

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

        self.searce_action.triggered.connect(self.searce_show)
        self.history_action.triggered.connect(self.history_show)
        self.favorites_action.triggered.connect(self.favorite_show)
        self.charts_action.triggered.connect(self.charts_show)

        self.label_list = [self.ui.label_0, self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                           self.ui.label_5, self.ui.label_6]

    def add_to_favorites(self):
        """

        :return:
        """
        if self.dialog_history.ui.listView.currentIndex().data() not in list(self.by_popularity_dict):
            self.by_popularity_dict[self.dialog_history.ui.listView.currentIndex().data()] = 0
            self.favorites_model.setStringList(list(self.by_popularity_dict))
            self.dialog_favorite.ui.listView.setModel(self.favorites_model)
            saved_data(self.by_popularity_dict, self.popularity_file)
            QMessageBox.information(self, 'Информация!',
                                    'Город успешно добавлен в "Избранное"', QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.information(self, 'Информация!',
                                    'Этот город уже есть в списке "Избранного"', QMessageBox.StandardButton.Ok)

    def delete_row_favorites(self):
        """

        :return:
        """
        self.dialog_favorite.ui.listView.setModel(self.favorites_model)
        self.dialog_favorite.ui.listView.model().removeRow(self.dialog_favorite.ui.listView.currentIndex().row())
        for i in list(self.by_popularity_dict):
            if i not in self.favorites_model.stringList():
                del (self.by_popularity_dict[i])
        self.dialog_favorite.ui.listView.setModel(self.favorites_model)
        saved_data(self.by_popularity_dict, self.popularity_file)
        QMessageBox.information(self, 'Информация!.',
                                'Город успешно удалён из "Избранного".', QMessageBox.StandardButton.Ok)

    def charts_show(self):
        """

        :return:
        """
        dialog_charts = DialogCarts(self.mw_dict['hourly'])
        file = open('qss_styles/my_qssStyle.qss', 'r')
        with file:
            my_qss = file.read()
            dialog_charts.setStyleSheet(my_qss)
        dialog_charts.exec()

    def searce_show(self):
        """

        :return:
        """
        file = open('qss_styles/my_qssStyle.qss', 'r')
        with file:
            my_qss = file.read()
            self.dialog_searce.setStyleSheet(my_qss)
        if self.dialog_searce.exec():
            self.weather_from_searce_list(self.dialog_searce.ui.listView_searce.currentIndex().data().
                                          split('  '))
        else:
            pass

    def remove_row_history_list(self):
        """

        :return:
        """
        self.dialog_history.ui.listView.setModel(self.history_model)
        self.dialog_history.ui.listView.model().removeRow(self.dialog_history.ui.
                                                          listView.currentIndex().row())
        self.history_list = self.history_model.stringList()
        self.history_model.setStringList(self.history_list)
        self.dialog_history.ui.listView.setModel(self.history_model)
        saved_data(self.history_list, self.history_file)
        QMessageBox.information(self, 'Информация!',
                                'Этот город успешно удалён из списке "История поиска"', QMessageBox.StandardButton.Ok)

    def favorite_show(self):
        """

        :return:
        """
        file = open('qss_styles/my_qssStyle.qss', 'r')
        with file:
            my_qss = file.read()
            self.dialog_favorite.setStyleSheet(my_qss)

        self.dialog_favorite.ui.listView.setModel(self.favorites_model)

        self.dialog_favorite.ui.pushButton_delete.clicked.connect(self.delete_row_favorites)
        self.dialog_favorite.ui.pushButton_abc.clicked.connect(self.sorted_abc)
        self.dialog_favorite.ui.pushButton_popularity.clicked.connect(self.sorted_popularity)

        if self.dialog_favorite.exec():
            self.weather_from_favorite()
        else:
            pass

    def history_show(self):
        """

        :return:
        """
        file = open('qss_styles/my_qssStyle.qss', 'r')
        with file:
            my_qss = file.read()
            self.dialog_history.setStyleSheet(my_qss)

        self.dialog_history.ui.listView.setModel(self.history_model)

        self.dialog_history.ui.pushButton_addFavorit.clicked.connect(self.add_to_favorites)
        self.dialog_history.ui.pushButton_delete.clicked.connect(self.remove_row_history_list)

        if self.dialog_history.isVisible():
            QMessageBox.information(self, 'Теперь нужно выбрать город.',
                                    'Выделите город из списка.', QMessageBox.StandardButton.Ok)

        if self.dialog_history.exec():
            self.weather_from_history(self.dialog_history.ui.listView.currentIndex().data().split('  '))
        else:
            pass

    def weather_from_searce_list(self, city_data: list):
        """

        :return:
        """
        try:
            ret_list = city_data
            self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
            create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label)
            create_str_daily(self.mw_dict, self.label_list, ret_list[5])
            if '  '.join(ret_list) not in self.history_list:
                self.history_list.insert(0, '  '.join(ret_list))
                self.history_model.setStringList(self.history_list)
                self.dialog_history.ui.listView.setModel(self.history_model)
                saved_data(self.history_list, self.history_file)
            else:
                pass
        except KeyError:
            pass

    def weather_from_history(self, city_data: list):
        """

        :return:
        """
        ret_list = city_data
        self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
        create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label)
        create_str_daily(self.mw_dict, self.label_list, ret_list[5])
        self.history_list.insert(0, '  '.join(ret_list))

    def weather_from_favorite(self):
        """

        :return:
        """
        ret_list = self.dialog_favorite.ui.listView.currentIndex().data().split('  ')

        self.mw_dict = get_weather_dict(float(ret_list[3]), float(ret_list[4]))
        create_str_current(self.mw_dict['current_weather'], ret_list, self.ui.label)
        create_str_daily(self.mw_dict, self.label_list, ret_list[5])

        city = self.dialog_favorite.ui.listView.currentIndex().data()
        for key in self.by_popularity_dict.keys():
            if key == city:
                self.by_popularity_dict[key] += 1
                sorted_dict = dict(sorted(self.by_popularity_dict.items(), key=lambda item: item[1], reverse=True))
                self.by_popularity_dict = copy(sorted_dict)
                print(self.by_popularity_dict)
                saved_data(sorted_dict, self.popularity_file)

    def sorted_popularity(self):
        sorted_list = count_sorted_list(self.by_popularity_dict)
        self.favorites_model.setStringList(sorted_list)
        saved_data(self.by_popularity_dict, self.popularity_file)
        """

        :return:city
        """
        city_list = list(self.by_popularity_dict)
        self.favorites_model.setStringList(city_list)
        saved_data(self.by_popularity_dict, self.popularity_file)

    def sorted_abc(self):
        sorted_list = abc_sorted_list(self.by_popularity_dict)
        self.favorites_model.setStringList(sorted_list)
        saved_data(self.by_popularity_dict, self.popularity_file)
        """

        :return:
        """
        sorted_list = list(self.by_popularity_dict)
        sorted_list.sort()


if __name__ == '__main__':
    app = QApplication()
    QtGui.QFontDatabase.addApplicationFont('roboto/Roboto-BoldItalic.ttf')
    window = MainWeather()
    window.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width() / 1.5,
                  QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
    window.setWindowIcon(QIcon('icon_files/program_icon.png'))
    window.setWindowTitle('Подробный прогноз погоды на неделю.')
    f = open('qss_styles/my_qssStyle.qss', 'r')
    with f:
        qss = f.read()
        window.setStyleSheet(qss)
    window.show()
    sys.exit(app.exec())
