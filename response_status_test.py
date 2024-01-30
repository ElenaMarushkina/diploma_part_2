#Марушкина Елена дипломный проект практический блок вторая часть
import create_order
import data

def test_status_of_order_is_200():
    response_order = create_order.post_new_order(data.order_body_full)  # 1 шаг - запрос на создание заказа
    track = {"t": response_order.json()["track"]}  # 2 шаг - сохраняем номер трека заказа
    response = create_order.getting_order_data(track)
    assert response.status_code == 200  # Проверка, что код ответа 200
