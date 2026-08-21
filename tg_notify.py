import os
import socket
import requests
from env_loader import load_environment_variables

# Загрузка переменных окружения
load_environment_variables()

# Получение значения URL
api_url = os.getenv('API_URL')
# Пустой THREAD_ID — сообщение уходит в основной чат группы алертов,
# а не в топик; тогда в текст добавляется префикс [сервер]
threadId = (os.getenv('THREAD_ID') or '').strip() or None
serverName = (os.getenv('SERVER_NAME') or '').strip() or socket.gethostname()

if not api_url:
    print("Ошибка: Не удалось получить значение API_URL из переменных окружения.")
    exit(1)

# Путь к сертификату CA в текущей директории
ca_cert_path = os.path.join(os.getcwd(), 'ca.crt')

def send_telegram_alert(message):
    data = {
        "type": "warning",
        "text": message if threadId else f"[{serverName}] {message}"
    }
    if threadId:
        data["threadId"] = threadId

    # Отправляем запрос
    try:
        verify_param = ca_cert_path if os.path.exists(ca_cert_path) else True
        response = requests.post(api_url, json=data, verify=verify_param)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
