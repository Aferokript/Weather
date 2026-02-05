import requests

def fetch_weather(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def get_weather_data():
    locations = {
        'Шереметьево': 'https://wttr.in/SVO',
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

    weather_data = {}

    for name, url in locations.items():
        weather_text = fetch_weather(url, params)
        weather_data[name] = weather_text
    return weather_data

def print_weather(weather_data):
    for name, weather_text in weather_data.items():
        print(f'Погода в {name}: {weather_text}')


def main():
    weather_data = get_weather_data()
    print_weather(weather_data)

if __name__ == '__main__':
    main()


