import requests


def fetch_weather(location, params):
    url = f"https://wttr.in/{location}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    locations = ['SVO', 'Череповец', 'Лондон']

    params = {
        'lang': 'ru',
        'm': '',
        'M': '',
        'q': '',
        '0': '' 
    }

    for location in locations:
        weather_text = fetch_weather(location, params)
        print(weather_text)


if __name__ == '__main__':
    main()

