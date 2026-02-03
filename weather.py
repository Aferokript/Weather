import requests

def build_url():
    url_Sherementevo = 'https://wttr.in/SVO'
    url_Cherepovec = 'https://wttr.in/Череповец'
    url_London = 'https://wttr.in/Лондон'

    params = {
        'lang': 'ru',
        'm': '',
        'M': '',
        'q': '',
        '0': ''
    }

    list_of_place = [
        {'Шерементево': url_Sherementevo},
        {'Череповец': url_Cherepovec},
        {'Лондон': url_London}
    ]

    for place in list_of_place:
        if 'Шерементево' in place:
            response1 = requests.get(place['Шерементево'], params=params)
            response1.raise_for_status()
        elif 'Череповец' in place:
            response2 = requests.get(place['Череповец'], params=params)
            response2.raise_for_status()
        elif 'Лондон' in place:
            response3 = requests.get(place['Лондон'], params=params)
            response3.raise_for_status()

    print(f'Погода в Аэропорту Шерементево:{response1.text}')
    print(f'Погода в Череповце:{response2.text}')
    print(f'Погода в Лондоне:{response3.text}')


def main():
    build_url()


if __name__ == '__main__':
    main()
