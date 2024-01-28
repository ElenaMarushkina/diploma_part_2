order_body_full = {
    "firstName": "Абдурахмангаджи",
    "lastName": "Убдурахмангаджи",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 204,
    "phone": "+34916123451",
    "rentTime": 5,
    "deliveryDate": "2024-01-17",
    "comment": "Привет, Абдурахмангаджи!",
    "color": [
        "WHITE"
    ]
}
order_body_only_necessary = {
"firstName": "Абдурахмангаджи",
    "lastName": "Убдурахмангаджи",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 204,
    "phone": "+34916123451",
    "rentTime": 5,
    "deliveryDate": "2024-01-17",
    "comment": "",
    "color": [
    ]
}
order_body_example_with_requirements = {
    'firstName' : 'Имя',  # Только русские буквы, пробел, тире. Длина не менее 2 и не более 15 символов.
    'lastName' :  'Фамилия',  # Только русские буквы. Длина не менее 2 и не более 15 символов.
    'address' : 'Адрес, дом 69',  # Только русские буквы, цифры, пробел, тире, точка, запятая. Длина не менее 5 и не более 50 символов.
    'metroStation' : 69,  # Номер станции метро (узнается запросом на бэкенд
    'phone' : '+79852992929',  # Только цифры и знак +. Длина не менее 10 и не более 12 символов.
    'rentTime' : 4,  # Кол-во суток, от 1 до 7
    'deliveryDate' : '2024-01-30',  # Дата заказа, в формате гггг-мм-дд
    'comment' : 'привет!',  # Только русские буквы, цифры, пробел, тире, точка, запятая. Длина не более 24 символов.
    'color' : ['BLACK']  # Либо ['BLACK'], либо ['WHITE']. Либо пустое поле оставить
}



