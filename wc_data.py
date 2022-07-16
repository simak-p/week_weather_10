from datetime import datetime as dt

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
    wind = ''
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


def create_str_daily(mw_dict: dict, label_list: list[QLabel]):
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
                  f"Солнце:  Восход {dt.fromtimestamp(daily['sunrise'][i]): %H:%M}    " \
                  f"Закат {dt.fromtimestamp(daily['sunset'][i]): %H:%M}"
        label_list[i].setText(day_str)


def create_data(hourly: dict):
    chart_data = {'temp': hourly['temperature_2m'], 'press': hourly['surface_pressure'],
                  'humidity': hourly['relativehumidity_2m'], 'feels': hourly['apparent_temperature'],
                  'time': list(map(QDateTime.fromSecsSinceEpoch, hourly['time'])), 'dt': hourly['time'],
                  'windspeed': hourly['windspeed_10m']}
    return chart_data


class HourlyChartsData:
    def __init__(self, hourly: dict):
        chart_data = create_data(hourly)
        self.temp_series = chart_points(chart_data['dt'], chart_data['temp'])
        self.feels_series = chart_points(chart_data['dt'], chart_data['feels'])
        self.pressSeries = chart_points(chart_data['dt'], chart_data['press'])
        self.humiditySeries = chart_points(chart_data['dt'], chart_data['humidity'])
        self.uviSeries = chart_points(chart_data['dt'], chart_data['windspeed'])
        self.x_axisMin = x_axis_range(chart_data['time'])[0]
        self.x_axsMax = x_axis_range(chart_data['time'])[1]
        self.y_tempAxisMin = y_axis_range([chart_data['temp'],chart_data['feels']])[0]
        self.y_tempAxisMax = y_axis_range([chart_data['temp'], chart_data['feels']])[1]
        self.y_pressAxisMin = y_axis_range([chart_data['press']])[0]
        self.y_pressAxisMax = y_axis_range([chart_data['press']])[1]
        self.y_humidityAxisMin = y_axis_range([chart_data['humidity']])[0]
        self.y_humidityAxisMax = y_axis_range([chart_data['humidity']])[1]
        self.y_uviAxisMin = y_axis_range([chart_data['windspeed']])[0]
        self.y_uviAxisMax = y_axis_range([chart_data['windspeed']])[1]


def x_axis_range(qdates: list):
    return [min(qdates), max(qdates)]


def y_axis_range(y_axes: list):
    n = int
    full_axes = sum(y_axes, [])
    for n in range(1, 5):
        if ((int(max(set(full_axes))) + 2) - (int(min(set(full_axes))) - n)) % 2 == 0:
            break
        else:
            n += 1
    return [int(min(set(full_axes))) - n, int(max(set(full_axes))) + 2]


def chart_points(dates: list, chart_list: list):
    return list(map(QPointF, dates, chart_list))
