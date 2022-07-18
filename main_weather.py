import pickle
import sys
from pprint import pprint
from save_dowwnload_data import load_data, saved_data
from wc_data import create_str_daily, create_data

from PySide6.QtGui import QScreen, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication
from form import Ui_MainWindow
from dw_weather import get_weather_dict, loc_to_coord
from my_dialog_charts import DialogCarts


class MainWeather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mw_dict = {}
        self.dialog_charts = None
        self.label_list = [self.ui.label_0, self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                           self.ui.label_5, self.ui.label_6, self.ui.label_7]
        self.ui.pushButtonsearce.clicked.connect(self.weather_from_name)
        self.ui.action_chart_week.triggered.connect(self.charts_show)

    # def create_weather_dict(self):
    #     mw_dict = get_weather_dict()
    #     if mw_dict is not None:
    #         pass
    #     else:
    #         print('No connection')
    #     # print(self.mw_dict['hourly'].keys())
    #     # pprint(self.mw_dict['hourly'])

    def weather_from_name(self):
        geo_coord = loc_to_coord(self.ui.lineEdit_Cyty.text())
        # self.mw_dict = get_weather_dict(geo_coord[1], geo_coord[0])
        # create_str_daily(self.mw_dict, self.label_list)
        # print(self.mw_dict['hourly'].keys())
        # # pprint(self.mw_dict['hourly']['time'])

    def charts_show(self):
        self.dialog_charts = DialogCarts(self.mw_dict['hourly'])
        self.dialog_charts.show()


if __name__ == '__main__':
    app = QApplication()
    window = MainWeather()
    window.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width() / 1.5,
                  QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
    # window.setWindowIcon(QIcon('program_icon.png'))
    window.setWindowTitle('Подробный прогноз погоды на три дня.')
    f = open('my_qssStyle.qss', 'r')
    with f:
        qss = f.read()
        window.setStyleSheet(qss)
    window.show()
    sys.exit(app.exec())
