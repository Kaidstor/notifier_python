import os
import requests
from env_loader import load_environment_variables

# Загрузка переменных окружения
load_environment_variables()

# Получение значения URL
api_url = os.getenv('API_URL')
threadId = os.getenv('THREAD_ID')

if not api_url or not threadId:
    print("Ошибка: Не удалось получить значения URL или threadId из переменных окружения.")
    exit(1)

def send_telegram_alert(message):
    data = {
        "threadId": threadId,
        "type": "warning",
        "text": message
    }

    # Отправляем запрос
    try:
        response = requests.post(api_url, json=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        