import requests

def get_weather_info():
    dict_of_place = {
        'Шерементево': 'https://wttr.in/SVO',
        'Череповец': 'https://wttr.in/Череповец',
        'Лондон': 'https://wttr.in/Лондон'
    }

    params = {
        'lang': 'ru',
        'm': '',
        'M': '',
        'q': '',
        '0': ''
    }

    weather_data = []

    for name,url in dict_of_place.items():
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data.append(response.text)
    return weather_data


def print_weather_data():
    weather_data = get_weather_info()
    print(f'Погода в аэропорту Шерементево: {weather_data[0]}')
    print(f'Погода в Череповце: {weather_data[1]}')
    print(f'Погода в Лондоне: {weather_data[2]}')


def main():
    print_weather_data()


if __name__ == '__main__':
    main()

