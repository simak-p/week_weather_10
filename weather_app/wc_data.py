from datetime import datetime as dt

import pytz
from PySide6.QtCore import QPointF, QDateTime
from PySide6.QtWidgets import QLabel

weather_code_dict = {0: 'Ясно', 1: 'Лёгкая облачность', 2: 'Переменная облачность', 3: 'Пасмурно', 45: 'Туман',
                     48: 'Иней', 51: 'Лёгкая морось', 53: 'Умеренная морось', 55: 'Сильная изморось',
                     56: 'Лёгкий моросящий дождь', 57: 'Плотный моросящий дождь', 61: 'Небольшой дождь',
                     63: 'Средний дождь', 65: 'Сильный дождь', 66: 'Небольшой ледяной дождь',
                     67: 'Сильный ледяной дождь', 71: 'Лёгкий снегопад', 73: 'Средний снегопад', 75: 'Сильный снегопад',
                     77: 'Снежная крупа', 80: 'Небольшие линевые дожди', 81: 'Умеренные ливневые дожди',
                     82: 'Сильные ливневые дожди', 85: 'Небольшой снегопад', 86: 'Сильный снегопад',
                     95: 'Небольшие грозы', 96: 'Гроза с небольшим градом', 99: 'Гроза с сильным градом'}


def w_code(weather_code: int):
    for code in weather_code_dict.keys():
        if code == weather_code:
            return weather_code_dict[code]


degree_code_dict = {range(22, 68): 'Северо-восточный', range(68, 112): 'Западный', range(112, 158): 'Юго-западный',
                    range(158, 202): 'Южный', range(202, 248): 'Юго-восточный', range(248, 292): 'Восточный',
                    range(292, 338): 'Северо-восточный'}


def wind_srt(degree_f: float):
    degree = int(degree_f)
    for wind in degree_code_dict.keys():
        if degree in wind:
            return degree_code_dict[wind]
    else:
        return 'Северный'


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
    print(chart_data['soil_moist'])
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
        self.y_soil_moistAxisMin = min(chart_data['soil_moist']) - 0.05
        self.y_soil_moistAxisMax = max(chart_data['soil_moist']) + 0.05


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
    global n
    full_axes = sum(y_axes, [])
    for n in range(1, 5):
        if ((int(max(set(full_axes))) + 2) - (int(min(set(full_axes))) - n)) % 2 != 0:
            n += 1
        else:
            break
    return [int(min(set(full_axes))) - n, int(max(set(full_axes))) + 2]


def chart_points(dates: list, chart_list: list):
    """

    :param dates:
    :param chart_list:
    :return:
    """
    return list(map(QPointF, dates, chart_list))
