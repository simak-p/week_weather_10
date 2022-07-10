from datetime import datetime as dt

from PySide6.QtWidgets import QLabel


def w_code(code: float):
    code_str = ''
    if code == 0.0: code_str = 'Ясно'
    elif code == 1.0: code_str = 'В основном ясно'
    elif code == 2.0: code_str = 'Переменная облачность'
    elif code == 3.0: code_str = 'Пасмурно'
    elif code == 45.0: code_str = 'Туман'
    elif code == 48.0: code_str = 'Иней'
    elif code == 51.0: code_str = 'Лёгкая морось'
    elif code == 53.0: code_str = 'Умеренная морось'
    elif code == 55.0: code_str = 'Сильная изморось'
    elif code == 56.0: code_str = 'Лёгкий моросящий дождь'
    elif code == 57.0: code_str = 'Плотный моросящий дождь'
    elif code == 61.0: code_str = 'Небольшой дождь'
    elif code == 63.0: code_str = 'Средний дождь'
    elif code == 65.0: code_str = 'Сильный дождь'
    elif code == 66.0: code_str = 'Небольшой ледяной дождь'
    elif code == 67.0: code_str = 'Сильный ледяной дождь'
    elif code == 71.0: code_str = 'Лёгкий снегопад'
    elif code == 73.0: code_str = 'Средний снегопад'
    elif code == 75.0: code_str = 'Сильный снегопад'
    elif code == 77.0: code_str = 'Снежная крупа'
    elif code == 80.0: code_str = 'Небольшие линевые дожди'
    elif code == 81.0: code_str = 'Умеренные ливневые дожди'
    elif code == 82.0: code_str = 'Сильные ливневые дожди'
    elif code == 85.0: code_str = 'Небольшой снегопад'
    elif code == 86.0: code_str = 'Сильный снегопад'
    elif code == 95.0: code_str = 'Небольшие грозы'
    elif code == 96.0: code_str = 'Гроза с небольшим градом'
    elif code == 99.0: code_str = 'Гроза с сильным градом'
    else: code_str = 'Нет данных'
    return code_str


def wind_srt(degree_f: float):
    degree = int(degree_f)
    wind = ''
    if degree in range(22, 68): wind = 'Северо-восточный'
    elif degree in range(68, 112): wind = 'Западный'
    elif degree in range(112, 158): wind = 'Юго-западный'
    elif degree in range(158, 202): wind = 'Южный'
    elif degree in range(202, 248): wind = 'Юго-восточный'
    elif degree in range(248, 292): wind = 'Восточный'
    elif degree in range(292, 338): wind = 'Северо-восточный'
    else: wind = 'Северный'
    return wind


def create_str_daily(daily: dict, label_list: list[QLabel]):
    for i in range(len(daily['time'])):
        day_str = f"{dt.fromtimestamp(daily['time'][i]): %A  %d %B}.    {w_code(daily['weathercode'][i])}\n" \
                  f"Температура воздуха: днём  {daily['temperature_2m_max'][i]}°C   " \
                  f"по ощущениям {daily['apparent_temperature_max'][i]}°C\n" \
                  f"Температура воздуха:  ночью {daily['temperature_2m_min'][i]}°C   " \
                  f"по ощущениям {daily['apparent_temperature_min'][i]}°C\n" \
                  f"Ветер:  {wind_srt(daily['winddirection_10m_dominant'][i])}  " \
                  f"скорость {daily['windspeed_10m_max'][i]}м/с   порывы до {daily['windgusts_10m_max'][i]}м/с\n" \
                  f"Количество осадков {daily['precipitation_sum'][i]}мм" \
                  f"количество часов за сутки с осадками {daily['precipitation_hours'][i]}\n" \
                  f"Солнце:  Восход {dt.fromtimestamp(daily['sunrise'][i]): %H:%M}    " \
                  f"Закат {dt.fromtimestamp(daily['sunset'][i]): %H:%M}"
        label_list[i].setText(day_str)
