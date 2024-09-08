import requests
import pytest

# Переменные
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4c6a62dfc800ad9fbc0ba8c3cffdbe78'
HEADER = {'Content-type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '5137'

# Проверка, что статус код ответа - 200
def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200

# Проверка, что в ответе приходит строчка с именем своего тренера
def test_trainer_name():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Джорджо'