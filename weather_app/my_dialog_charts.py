from PySide6.QtCharts import QChartView
from PySide6.QtGui import QScreen, QPainter
from PySide6.QtWidgets import QDialog, QApplication, QScrollArea

from weather_app.create_charts import TempChart, PressChart, HumidityChart, WindChart, PrecipChart, DewPointChart, \
    SunRadChart, SnowDepthChart, SoilChart
from weather_app.dialog_charts import Ui_Dialog_charts


class DialogCarts(QDialog):
    """

    """

    def __init__(self, hourly):
        """

        :param hourly:
        """
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
        self.scroll_area = QScrollArea()
        self.chart_view = QChartView(self.scroll_area)
        self.scroll_area.setWidget(self.chart_view)
        self.scroll_area.setWidgetResizable(False)
        self.ui.verticalLayout.addWidget(self.scroll_area)
        self.chart_view.setChart(self.temp_chart)
        self.ui.horizontalSlider.setRange(self.width(), 4000)
        self.ui.comboBox_week.currentTextChanged.connect(self.set_chart)
        self.ui.horizontalSlider.valueChanged.connect(self.resizeEvent)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_scaling()

    def set_chart(self, text):
        """

        :param text:
        :return:
        """
        if text == 'Температура':
            self.chart_view.setChart(self.temp_chart)
        elif text == 'Давление':
            self.chart_view.setChart(self.press_chart)
        elif text == 'Влажность':
            self.chart_view.setChart(self.humidity_chart)
        elif text == 'Ветер':
            self.chart_view.setChart(self.wind_chart)
        elif text == 'Осадки':
            self.chart_view.setChart(self.precip_chart)
        elif text == 'Точка росы':
            self.chart_view.setChart(self.dewpoint_chart)
        elif text == 'Солнечная радиация':
            self.chart_view.setChart(self.radiation_chart)
        elif text == 'Высота снега':
            self.chart_view.setChart(self.snow_depth_chart)
        elif text == 'Почва':
            self.chart_view.setChart(self.soil_chart)

    def chart_scaling(self):
        self.chart_view.resize(self.ui.horizontalSlider.value(), self.scroll_area.height())
        print(self.ui.horizontalSlider.value())
        print(self.chart_view.width())

    def resizeEvent(self, event) -> None:
        self.chart_view.resize(self.ui.horizontalSlider.value(), self.scroll_area.height())
