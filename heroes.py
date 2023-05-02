# Task_1

import requests

heroes_list = ['Hulk', 'Captain America', 'Thanos']
heroes_dict = {}


def comparison_heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url).json()
    hero_dict = {}
    for hero in response:
        if hero['name'] in heroes_list:
            heroes_dict.setdefault(hero['name'], hero['powerstats']['intelligence'])
    print(f'Самый умный из героев - {max(heroes_dict, key=heroes_dict.get)}')


if __name__ == '__main__':
    comparison_heroes()
