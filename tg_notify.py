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

# Путь к сертификату CA в текущей директории
ca_cert_path = os.path.join(os.getcwd(), 'ca.crt')

def send_telegram_alert(message):
    data = {
        "threadId": threadId,
        "type": "warning",
        "text": message
    }

    # Отправляем запрос
    try:
        verify_param = ca_cert_path if os.path.exists(ca_cert_path) else True
        response = requests.post(api_url, json=data, verify=verify_param)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        