import requests

# Токен для работы с Апи
OpenWeatherApiKey = "d8f6405154f58627df4e6ea56cb457bf"


def get_weather_coordinates(city_name):
    limit = 1
    # Передаю в URL переменные с названием города, выбираю лимит в 1 город, и передаю токен
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={OpenWeatherApiKey}"
    # Получаю ответ в json формате, что бы потом вытащить координаты города
    request = requests.get(url).json()
    # Получаю координаты из ответа
    for i in request:
        coordinates_tuple = (i['lat'], i['lon'])
    return coordinates_tuple


def get_weather(coordinates_tuple):
    coordinates = coordinates_tuple
    lang = 'ru'
    # Отправляю запрос, что бы получить ответ по погоде в нужном городе.
    # Так-же использую координаты, из прошлой функции. Т.к. данное Апи работает не с названием города, а координатами.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid={OpenWeatherApiKey}&lang={lang}"
    # Получаю ответ и возвращаю его.
    response = requests.get(url).json()
    return response


if __name__ == "__main__":
    # Получаю город и кладу его в переменную
    city_name = input("Введите город в котором хотите узнать погоду")

    # Получаю координаты нужного города
    coordinates_tuple = get_weather_coordinates(city_name)

    # Вызываю функцию, и кладу ответ в переменную.
    try:
        data = get_weather(coordinates_tuple)
    # Если функция выдала ошибку, т.к. город который мы ввели несуществует, она выдаёт предупреждение.
    except:
        response = f"Данный город не обнаружен, пожалуйста, проверьте правильность написания"
    # В случае успеха достаю данные из переменной data и формурю ответ пользователю.
    else:
        temp_celsia = float('{:.1f}'.format((data['main']['temp'] - 273.15)))
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        response = f"Город: {city_name}\nТемпература: {temp_celsia} °C\nНа улице: {description}\nВетер: {wind_speed} м/с"
    print(response)
