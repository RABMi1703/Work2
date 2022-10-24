# Импортируем библиотеки
import requests


def get_weather(city, appid) -> None:
    # Получаем информацию
    res = requests.get('http://api.openweathermap.org/data/2.5/weather', params = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

    # Получаем значения ветра и видимости
    wind_speed, wind_deg, wind_gust = data['wind']['speed'], data['wind']['deg'], data['wind']['gust']
    visibility = data['visibility']

    # Выводим информацию
    print(f'Скорость ветра: {wind_speed} (м/с)\nНаправление ветра: {wind_deg} (градусы)\nПорыв ветра: {wind_gust} (м/с)\nВидимость: {visibility} (м)')

def get_forecast(city, appid) -> None:
    # Получаем информацию
    res = requests.get('http://api.openweathermap.org/data/2.5/forecast', params = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

    # Пробегаем периоды, из которых будем доставать инфомацию
    for i in data['list']:
        # Получаем дату, значения ветра и видимости
        data_now = i['dt_txt']
        wind_speed, wind_deg, wind_gust = i['wind']['speed'], i['wind']['deg'], i['wind']['gust']
        visibility = i['visibility']

        # Выводим информацию
        print(f'Дата: {data_now}\nСкорость ветра: {wind_speed} (м/с)\nНаправление ветра: {wind_deg} (градусы)\nПорыв ветра: {wind_gust} (м/с)\nВидимость: {visibility} (м)')
        print('_' * 20)

def main() -> None:
    # Входные данные
    city = 'Moscow,RU'
    appid = 'f655b0020672a9ee932f06fa3ab2ff1d'

    # Вывод
    print('Текущий прогноз:')
    get_weather(city, appid)
    print('Недельный прогноз:')
    get_forecast(city, appid)

main()
