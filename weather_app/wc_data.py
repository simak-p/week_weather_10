
from datetime import datetime as dt
import pytz
from pprint import pprint

from PySide6.QtCore import QPointF, QDateTime
from PySide6.QtWidgets import QLabel


def w_code(code: float):
    if code == 0.0:
        code_str = 'Ясно'
    elif code == 1.0:
        code_str = 'В основном ясно'
    elif code == 2.0:
        code_str = 'Переменная облачность'
    elif code == 3.0:
        code_str = 'Пасмурно'
    elif code == 45.0:
        code_str = 'Туман'
    elif code == 48.0:
        code_str = 'Иней'
    elif code == 51.0:
        code_str = 'Лёгкая морось'
    elif code == 53.0:
        code_str = 'Умеренная морось'
    elif code == 55.0:
        code_str = 'Сильная изморось'
    elif code == 56.0:
        code_str = 'Лёгкий моросящий дождь'
    elif code == 57.0:
        code_str = 'Плотный моросящий дождь'
    elif code == 61.0:
        code_str = 'Небольшой дождь'
    elif code == 63.0:
        code_str = 'Средний дождь'
    elif code == 65.0:
        code_str = 'Сильный дождь'
    elif code == 66.0:
        code_str = 'Небольшой ледяной дождь'
    elif code == 67.0:
        code_str = 'Сильный ледяной дождь'
    elif code == 71.0:
        code_str = 'Лёгкий снегопад'
    elif code == 73.0:
        code_str = 'Средний снегопад'
    elif code == 75.0:
        code_str = 'Сильный снегопад'
    elif code == 77.0:
        code_str = 'Снежная крупа'
    elif code == 80.0:
        code_str = 'Небольшие линевые дожди'
    elif code == 81.0:
        code_str = 'Умеренные ливневые дожди'
    elif code == 82.0:
        code_str = 'Сильные ливневые дожди'
    elif code == 85.0:
        code_str = 'Небольшой снегопад'
    elif code == 86.0:
        code_str = 'Сильный снегопад'
    elif code == 95.0:
        code_str = 'Небольшие грозы'
    elif code == 96.0:
        code_str = 'Гроза с небольшим градом'
    elif code == 99.0:
        code_str = 'Гроза с сильным градом'
    else:
        code_str = 'Нет данных'
    return code_str


def wind_srt(degree_f: float):
    degree = int(degree_f)
    if degree in range(22, 68):
        wind = 'Северо-восточный'
    elif degree in range(68, 112):
        wind = 'Западный'
    elif degree in range(112, 158):
        wind = 'Юго-западный'
    elif degree in range(158, 202):
        wind = 'Южный'
    elif degree in range(202, 248):
        wind = 'Юго-восточный'
    elif degree in range(248, 292):
        wind = 'Восточный'
    elif degree in range(292, 338):
        wind = 'Северо-восточный'
    else:
        wind = 'Северный'
    return wind


def create_str_daily(mw_dict: dict, label_list: list[QLabel], t_zone: str):
    """
    Создаёт строки с погодой на семь дней по числу labels в
    label_list и вставляет их туда.
    :param t_zone:
    :param mw_dict:
    :param label_list:
    :return:
    """
    city_timezone = pytz.timezone(t_zone)
    daily = mw_dict['daily']
    for i in range(len(daily['time'])):
        day_str = f"{dt.fromtimestamp(daily['time'][i]): %A  %d %B}.    {w_code(daily['weathercode'][i])}\n" \
                  f"Температура воздуха: днём  {daily['temperature_2m_max'][i]}°C   " \
                  f"по ощущениям {daily['apparent_temperature_max'][i]}°C\n" \
                  f"Температура воздуха:  ночью {daily['temperature_2m_min'][i]}°C   " \
                  f"по ощущениям {daily['apparent_temperature_min'][i]}°C\n" \
                  f"Ветер:  {wind_srt(daily['winddirection_10m_dominant'][i])}  " \
                  f"скорость {daily['windspeed_10m_max'][i]}м/с   порывы до {daily['windgusts_10m_max'][i]}м/с\n " \
                  f"Количество осадков {daily['precipitation_sum'][i]}мм    " \
                  f"количество часов за сутки с осадками {daily['precipitation_hours'][i]}\n" \
                  f"Солнце:  Восход {dt.fromtimestamp(daily['sunrise'][i], tz=city_timezone): %H:%M}    " \
                  f"Закат {dt.fromtimestamp(daily['sunset'][i], tz=city_timezone): %H:%M}   Долгота дня: " \
                  f" {dt.utcfromtimestamp(daily['sunset'][i] - daily['sunrise'][i]): %H:%M}"
        label_list[i].setText(day_str)


def create_str_current(cw_dict: dict, city_dict: list, label: QLabel):
    """

    :param cw_dict:
    :param city_dict:
    :param label:
    :return:
    """
    if city_dict[0] == city_dict[2]:
        current_str = f"Погода на {dt.fromtimestamp(cw_dict['time']): %H:%M}\n" \
                      f"гор.{city_dict[0]} {city_dict[1]} \n" \
                      f"{w_code(cw_dict['weathercode'])}  температура:{cw_dict['temperature']}°C\n " \
                      f" ветер  {wind_srt(cw_dict['winddirection'])}  скорость:{cw_dict['windspeed']}м/с"
    else:
        current_str = f"Погода на {dt.fromtimestamp(cw_dict['time']): %H:%M}\n" \
                      f"гор.{city_dict[0]} {city_dict[1]} регион: {city_dict[2]}\n" \
                      f"{w_code(cw_dict['weathercode'])}  температура:{cw_dict['temperature']}°C\n " \
                      f" ветер  {wind_srt(cw_dict['winddirection'])}  скорость:{cw_dict['windspeed']}м/с"
    label.setText(current_str)


def create_data(hourly: dict):
    """

    :param hourly:
    :return:
    """
    chart_data = {'temp': hourly['temperature_2m'], 'press': hourly['surface_pressure'],
                  'humidity': hourly['relativehumidity_2m'], 'feels': hourly['apparent_temperature'],
                  'time': list(map(QDateTime.fromSecsSinceEpoch, hourly['time'])), 'dt': hourly['time'],
                  'windspeed': hourly['windspeed_10m'], 'wind_gust': hourly['windgusts_10m'],
                  'dew_point': hourly['dewpoint_2m'], 'snow_depth': hourly['snow_depth'],
                  'precipitation': hourly['precipitation'], 'shortwave_radiation': hourly['shortwave_radiation'],
                  'soil_temp_6': hourly['soil_temperature_6cm'], 'soil_temp_18': hourly['soil_temperature_18cm'],
                  'soil_moist': hourly['soil_moisture_3_9cm']}
    # print(chart_data['soil_moist'])
    return chart_data


class HourlyChartsData:
    """

    """

    def __init__(self, hourly: dict):
        """

        :param hourly:
        """
        chart_data = create_data(hourly)
        self.tempSeries = chart_points(chart_data['dt'], chart_data['temp'])
        self.feelsSeries = chart_points(chart_data['dt'], chart_data['feels'])
        self.pressSeries = chart_points(chart_data['dt'], chart_data['press'])
        self.humiditySeries = chart_points(chart_data['dt'], chart_data['humidity'])
        self.speedSeries = chart_points(chart_data['dt'], chart_data['windspeed'])
        self.gustSeries = chart_points(chart_data['dt'], chart_data['wind_gust'])
        self.dew_pointSeries = chart_points(chart_data['dt'], chart_data['dew_point'])
        snow_list = snow_dept_no_sm(chart_data['snow_depth'])
        self.snowSeries = chart_points(chart_data['dt'], snow_list)
        self.precipSeries = chart_points(chart_data['dt'], chart_data['precipitation'])
        self.radiationSeries = chart_points(chart_data['dt'], chart_data['shortwave_radiation'])
        self.soil_temp_6Series = chart_points(chart_data['dt'], chart_data['soil_temp_6'])
        self.soil_temp_18Series = chart_points(chart_data['dt'], chart_data['soil_temp_18'])
        self.soil_moistSeries = chart_points(chart_data['dt'], chart_data['soil_moist'])
        self.x_axisMin = x_axis_range(chart_data['time'])[0]
        self.x_axsMax = x_axis_range(chart_data['time'])[1]
        self.y_tempAxisMin = y_axis_range([chart_data['temp'], chart_data['feels']])[0]
        self.y_tempAxisMax = y_axis_range([chart_data['temp'], chart_data['feels']])[1]
        self.y_pressAxisMin = y_axis_range([chart_data['press']])[0]
        self.y_pressAxisMax = y_axis_range([chart_data['press']])[1]
        self.y_humidityAxisMin = y_axis_range([chart_data['humidity']])[0]
        self.y_humidityAxisMax = y_axis_range([chart_data['humidity']])[1]
        self.y_speedAxisMin = y_axis_range([chart_data['windspeed'], chart_data['wind_gust']])[0]
        self.y_speedAxisMax = y_axis_range([chart_data['windspeed'], chart_data['wind_gust']])[1]
        self.y_devPointAxisMin = y_axis_range([chart_data['dew_point']])[0]
        self.y_devPointAxisMax = y_axis_range([chart_data['dew_point']])[1]
        self.y_snowAxisMin = y_axis_range([snow_dept_no_sm(chart_data['snow_depth'])])[0]
        self.y_snowAxisMax = y_axis_range([snow_dept_no_sm(chart_data['snow_depth'])])[1]
        self.y_precipAxisMin = y_axis_range([chart_data['precipitation']])[0]
        self.y_precipAxisMax = y_axis_range([chart_data['precipitation']])[1]
        self.y_radiationAxisMin = y_axis_range([chart_data['shortwave_radiation']])[0]
        self.y_radiationAxisMax = y_axis_range([chart_data['shortwave_radiation']])[1]
        self.y_soil_temp_AxisMin = y_axis_range([chart_data['soil_temp_6'], chart_data['soil_temp_18']])[0]
        self.y_soil_temp_AxisMax = y_axis_range([chart_data['soil_temp_6'], chart_data['soil_temp_18']])[1]
        self.y_soil_moistAxisMin = y_axis_range([chart_data['soil_moist']])[0]
        self.y_soil_moistAxisMax = y_axis_range([chart_data['soil_moist']])[1]


def snow_dept_no_sm(qdata: list) -> list:
    """
    Умножает каждый элемент списка на 100
    :param qdata:
    :return:
    """
    return [i * 100 for i in qdata]


def x_axis_range(qdates: list):
    """

    :param qdates:
    :return:
    """
    return [min(qdates), max(qdates)]


def y_axis_range(y_axes: list):
    """

    :param y_axes:
    :return:
    """
    n = int
    full_axes = sum(y_axes, [])
    for n in range(1, 5):
        if ((int(max(set(full_axes))) + 2) - (int(min(set(full_axes))) - n)) % 2 == 0:
            break
        else:
            n += 1
    return [int(min(set(full_axes))) - n, int(max(set(full_axes))) + 2]


def chart_points(dates: list, chart_list: list):
    """

    :param dates:
    :param chart_list:
    :return:
    """
    return list(map(QPointF, dates, chart_list))
