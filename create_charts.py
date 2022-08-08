from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QPen, QColor, QFont

from wc_data import HourlyChartsData

chart_font = QFont("Sans Serif", 12, QFont.StyleItalic)


class MyXAxis(QDateTimeAxis):
    def __init__(self, ax_min: QDateTime, ax_max: QDateTime):
        super().__init__()
        self.setFormat('ddd HH:MM')
        self.setLabelsColor('orange')
        self.setTickCount(29)
        self.setLabelsAngle(270)
        self.setTitleText('Часы')
        self.setTitleBrush(QColor('orange'))
        self.setRange(ax_min, ax_max)
        self.setLabelsFont(chart_font)


class MyYAxis(QValueAxis):
    def __init__(self, ax_min: int, ax_max: int, dev: int, name: str):
        super().__init__()
        self.setRange(ax_min, ax_max)
        self.setTickCount((ax_max - ax_min) // dev + 1)
        self.setTitleText(name)
        self.setLabelsFont(chart_font)


class MySplineSeries(QSplineSeries):
    def __init__(self, name: str, list_series: list, color):
        super().__init__()
        self.setName(name)
        self.append(list_series)
        self.setPen(QPen(color, 3))


class TempChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)

        self._y_axis = MyYAxis(hd.y_tempAxisMin, hd.y_tempAxisMax, 2, 'Градусы')
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)

        self.temp_series = MySplineSeries('Температура', hd.tempSeries, Qt.red)
        self.feels_series = MySplineSeries('По ощущениям', hd.feelsSeries, Qt.magenta)

        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addSeries(self.feels_series)
        self.addSeries(self.temp_series)
        self.temp_series.attachAxis(self._y_axis)
        self.feels_series.attachAxis(self._y_axis)


class PressChart(QChart):
    def __init__(self, hourly):
        super().__init__()

        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        #
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        #
        self._yPress_axis = MyYAxis(hd.y_pressAxisMin, hd.y_pressAxisMax, 2, 'гПа')
        #
        self.press_series = MySplineSeries('Давление', hd.pressSeries, Qt.yellow)

        self.addAxis(self._yPress_axis, Qt.AlignLeft)
        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addSeries(self.press_series)
        self.press_series.attachAxis(self._yPress_axis)


class HumidityChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        #
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        #
        self._yHumidity_axis = MyYAxis(hd.y_humidityAxisMin, hd.y_humidityAxisMax, 10, '%')
        #
        self.humidity_series = MySplineSeries('Влажность', hd.humiditySeries, QColor('#7AE0FF'))
        #
        self.addSeries(self.humidity_series)
        self.addAxis(self._yHumidity_axis, Qt.AlignLeft)
        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.humidity_series.attachAxis(self._yHumidity_axis)


class WindChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        self._y_axis = MyYAxis(hd.y_speedAxisMin, hd.y_speedAxisMax, 2, 'м/с.')
        self.speed_series = MySplineSeries('Скорость', hd.speedSeries, QColor('#FF6E1A'))
        self.gust_series = MySplineSeries('Порывы', hd.gustSeries, QColor('#E300EB'))

        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addSeries(self.speed_series)
        self.addSeries(self.gust_series)
        self.speed_series.attachAxis(self._y_axis)
        self.gust_series.attachAxis(self._y_axis)


class PrecipChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        self._y_axis = MyYAxis(hd.y_pressAxisMin, hd.y_precipAxisMax, 2, 'мм.')
        self.precip_series = MySplineSeries('Количество осадков', hd.precipSeries, QColor('#14A8FF'))

        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addSeries(self.precip_series)
        self.precip_series.attachAxis(self._y_axis)


class DewPointChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        self._y_axis = MyYAxis(hd.y_humidityAxisMin, hd.y_humidityAxisMax, 6, '°C')
        self.humidity_series = MySplineSeries('Точка росы', hd.humiditySeries, QColor('#FF14A8'))

        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addSeries(self.humidity_series)
        self.humidity_series.attachAxis(self._y_axis)


class SunRadChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        self._y_axis = MyYAxis(hd.y_radiationAxisMin, hd.y_radiationAxisMax, 100, 'Радиация Вт/м')
        self.radiation_series = MySplineSeries('Солнечная радиация', hd.radiationSeries, QColor('#FF1432'))

        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addSeries(self.radiation_series)
        self.radiation_series.attachAxis(self._y_axis)


class SnowDepthChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        self._y_axis = MyYAxis(hd.y_snowAxisMin, hd.y_snowAxisMax, 100, 'Высота снежного\nпокрова см.')
        self.snow_depth_series = MySplineSeries('Количество снега', hd.snowSeries, QColor('#1432FF'))

        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addSeries(self.snow_depth_series)
        self.snow_depth_series.attachAxis(self._y_axis)


class SoilChart(QChart):
    def __init__(self, hourly):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = HourlyChartsData(hourly)
        self._x_axis = MyXAxis(hd.x_axisMin, hd.x_axsMax)
        self._y_temp_axis = MyYAxis(hd.y_soil_temp_AxisMin, hd.y_soil_temp_AxisMax, 2, 'Температура почвы °C')
        self._y_moist_axis = MyYAxis(0, hd.y_soil_moistAxisMax - 1.5, 2, 'Влажность почвы м.м')
        self.soil_temp6_series = MySplineSeries('Температура почвы на 6см', hd.soil_temp_6Series, QColor('#FF1432'))
        self.soil_temp18_series = MySplineSeries('Температура почвы на 6=18см', hd.soil_temp_18Series,
                                                 QColor('#FF14A8'))
        self.soil_moist_series = MySplineSeries('Влажность почвы', hd.soil_moistSeries, QColor('#14A8FF'))

        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addAxis(self._y_temp_axis, Qt.AlignLeft)
        self.addAxis(self._y_moist_axis, Qt.AlignRight)
        self.addSeries(self.soil_temp6_series)
        self.addSeries(self.soil_temp18_series)
        self.addSeries(self.soil_moist_series)
        self.soil_temp6_series.attachAxis(self._y_temp_axis)
        self.soil_temp18_series.attachAxis(self._y_temp_axis)
        self.soil_moist_series.attachAxis(self._y_moist_axis)
