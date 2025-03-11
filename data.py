import random
from datetime import datetime, timedelta

ORDER_DATA_SETS = [
    {
        "name": "Иван",
        "surname": "Петров",
        "address": "ул. Ленина, д. 10",
        "phone": "+79001234567",
        "date": (datetime.today() + timedelta(days=random.choice([1, 30]))).strftime("%d.%m.%Y"),
        "color": ["black"],
        "comment": "Позвоните за 30 минут"
    },
    {
        "name": "Мария",
        "surname": "Сидорова",
        "address": "пр-т Мира, д. 25",
        "phone": "+79007654321",
        "date": (datetime.today() + timedelta(days=random.choice([1, 30]))).strftime("%d.%m.%Y"),
        "color": [],
        "comment": ""
    }
]
