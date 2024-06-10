import os
import requests
from env_loader import load_environment_variables

# Загрузка переменных окружения
load_environment_variables()

# Получение значения URL
api_url = os.getenv('API_URL')

def send_telegram_alert(message):
    data = {
        "threadId": "3500",
        "type": "warning",
        "text": message
    }

    # Отправляем запрос
    try:
        response = requests.post(api_url, json=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        