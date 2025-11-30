import requests
from bs4 import BeautifulSoup

# 1. Определяем URL страницы логина и учетные данные
LOGIN_URL = 'https://topol-dt.ru/personal'  # Замените на актуальный URL
USERNAME = 'USERNAME'                  # Замените на ваш логин
PASSWORD = 'PASSWORD'                  # Замените на ваш пароль

# 2. Создаем сессию для сохранения cookies
session = requests.Session()

# 3. (Опционально) Получаем страницу логина для извлечения CSRF-токена
response_get = session.get(LOGIN_URL)
soup = BeautifulSoup(response_get.text, 'html.parser')

