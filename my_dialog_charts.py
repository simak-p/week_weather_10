from PySide6.QtCharts import QChartView
from PySide6.QtGui import QScreen, QPainter, QAction
from PySide6.QtWidgets import QDialog, QApplication, QButtonGroup

from create_charts import TempChart, PressChart, HumidityChart, WindChart, PrecipChart, DewPointChart, SunRadChart, \
                            SnowDepthChart, SoilChart
from dialog_charts import Ui_Dialog_charts


class DialogCarts(QDialog):
    def __init__(self, hourly):
        super(DialogCarts, self).__init__()
        self.ui = Ui_Dialog_charts()
        self.ui.setupUi(self)
        self.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width(),
                    QScreen.availableGeometry(QApplication.primaryScreen()).height() / 1.5)
        self.temp_chart = TempChart(hourly)
        self.press_chart = PressChart(hourly)
        self.humidity_chart = HumidityChart(hourly)
        self.wind_chart = WindChart(hourly)
        self.precip_chart = PrecipChart(hourly)
        self.dewpoint_chart = DewPointChart(hourly)
        self.radiation_chart = SunRadChart(hourly)
        self.snow_depth_chart = SnowDepthChart(hourly)
        self.soil_chart = SoilChart(hourly)
        self.chart_list = ['Температура', 'Давление', 'Влажность', 'Ветер', 'Точка росы', 'Осадки', 'Высота снега',
                           'Солнечная радиация', 'Почва']
        self.ui.comboBox_week.addItems(self.chart_list)
        self.ui.comboBox_2daly.addItems(self.chart_list)
        self.chart = QChartView()
        self.chart.setChart(self.temp_chart)
        self.ui.verticalLayout.addWidget(self.chart)
        self.ui.comboBox_week.currentTextChanged.connect(self.set_chart)

        self.chart.setRenderHint(QPainter.Antialiasing)

    def set_chart(self, text):
        if text == 'Температура':
            self.chart.setChart(self.temp_chart)
        elif text == 'Давление':
            self.chart.setChart(self.press_chart)
        elif text == 'Влажность':
            self.chart.setChart(self.humidity_chart)
        elif text == 'Ветер':
            self.chart.setChart(self.wind_chart)
        elif text == 'Осадки':
            self.chart.setChart(self.precip_chart)
        elif text == 'Точка росы':
            self.chart.setChart(self.dewpoint_chart)
        elif text == 'Солнечная радиация':
            self.chart.setChart(self.radiation_chart)
        elif text == 'Высота снега':
            self.chart.setChart(self.snow_depth_chart)
        elif text == 'Почва':
            self.chart.setChart(self.soil_chart)
