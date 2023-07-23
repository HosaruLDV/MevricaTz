import requests

# Апи-токен который нужен для работы с Апи.
ExchangeRatesAPIToken = "Li3v3AyQT63x2UGQw2sUiffwjy3XFj6c"


def get_convert_sum(final_currency, start_currency, my_sum):
    # Урл для работы с Апи, в него передаю нужные данные из функции, напрямую.
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={final_currency}&from={start_currency}&amount={my_sum}"
    # Передаю через хэдер наш Апи токен.
    headers = {
        "apikey": ExchangeRatesAPIToken
    }

    request = requests.get(url, headers=headers).json()
    # Проверяю, успешный ли ответ пришёл и формирую ответ для пользователя.
    try:
        response = f"Валюта из которой переводили: {request['query']['from']} " \
                   f"\nВалюта в которую переводили: {request['query']['to']} " \
                   f"\nСумма из которой переводили: {request['query']['amount']} {request['query']['from']}" \
                   f"\nКонечная сумма: {float('{:.2f}'.format(request['result']))} {request['query']['to']}"
    except:
        response = "Я не знаю такой валюты, попробуйте ввести данные еще раз"
        return response
    else:
        return response


if __name__ == "__main__":
    final_currency = input("Введите валюту в которую хотите перевести. \nНапример: USD, EUR, JPU, RUB").replace(" ", "")
    start_currency = input("Введите валюту из которой хотите перевести. \nНапример: USD, EUR, JPU, RUB").replace(" ", "")
    my_sum = input("Введите колличество денег, которые хотите перевести").replace(" ", "")

    print(get_convert_sum(final_currency, start_currency, my_sum))
