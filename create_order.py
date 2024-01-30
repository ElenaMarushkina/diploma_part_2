import configuration
import data
import requests


def post_new_order(order_body):  # функция POST-запроса с созданием заказа
    return requests.post(configuration.URL + configuration.ORDER_CREATE_PATH, json=order_body)


def getting_order_data(track):
    return requests.get(configuration.URL + configuration.GET_ORDER_DATA_PATH, params=track)
