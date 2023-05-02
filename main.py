# Task_2

import requests


class YaUploader:
    TOKEN = ''
    PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    params = {'path': 'test_n.txt', 'overwrite': 'true'}
    headers = {'Accept': 'application/json', 'Authorization': TOKEN}

    file_path = 'test_n.txt'

    response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
    print(response.text)

    put_url = response.json().get('href')
    print(put_url)

    files = {'file': open(file_path, 'rb')}
    response = requests.put(put_url, files=files, headers=headers)
    print(response)
