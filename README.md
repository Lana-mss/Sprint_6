# Проект автоматизации тестирования сервиса Самокат https://qa-scooter.praktikum-services.ru/ 
```
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска тестов — pytest -v --cache-clear.
4. Команда для запуска тестов с сохранением результатов — pytest --alluredir=allure_results
5. Команда для генерации и открытия Allure-отчёта — allure serve allure_results
```

# **Структура проекта**
```
Sprint_6/
│── allure_results/   # Директория для отчетов Allure
│── locators/         # Локаторы для страниц
│   │── order_locators.py     # Локаторы для страницы заказа самоката 
│   │── main_page_locators.py # Локаторы для главной страницы, включая вопросы и логотипы
│── pages/
│   │── base_page.py          # Базовые методы         
│   │── order_page.py         # Page Object для страницы заказа
│   │── main_page.py          # Методы для работы с главной страницей (клик по вопросам, переход по логотипам) 
│── tests/            
│   │── test_order.py         # Тесты на создание заказа с разными наборами данных
│   │── test_questions.py     # Тесты для раздела "Вопросы о важном"
│   │── test_navigation.py    # Тесты на переход по логотипам "Самокат" и "Яндекс"
│── data.py          # Тестовые данные
│── conftest.py       # Фикстура для WebDriver
│── README.md         # Описание проекта
│── requirements.txt  # Список зависимостей
│── .gitignore
```
