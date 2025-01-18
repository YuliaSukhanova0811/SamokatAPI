import requests
import data
import configuration


def create_order():
    url = configuration.URL_SERVICE + configuration.NEW_ORDER
    order_data = data.order_body
    
    response = requests.post(url, json=order_data)
    if response.status_code == 201:
        return response.json()["track"]
    else:
        return None


def get_order_by_track(track_number):
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.TRACK_ORDER}{track_number}")
    if response.status_code != 200:
        raise Exception(f"Ошибка при получении заказа: {response.status_code} - {response.text}")
    
    return response


def test_order_creation_and_retrieval():
    track_number = create_order()
    order_details = get_order_by_track(track_number)
    assert order_details.status_code == 200
