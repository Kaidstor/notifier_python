import subprocess
import argparse
import os
from tg_notify import send_telegram_alert


def is_container_running(container_name):
    result = subprocess.run(['docker', 'ps', '--filter', f"name={container_name}", '--format', '{{.Names}}'], capture_output=True, text=True)
    return container_name in result.stdout.strip()

def main(container_names):
    for container_name in container_names:
        if not is_container_running(container_name):
            message = f"Внимание: контейнер {container_name} не запущен!"
            response = send_telegram_alert(message)
            
            if (response.status_code != 204):
                print(response.text)  # Вывод ответа от серверa

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Проверяет статус контейнеров и сообщает в Telegram, если отключен один из списка.")
    parser.add_argument("--container_names", nargs='+', required=True, help="Имена контейнеров через пробел")
    
    args = parser.parse_args()
    
    main(args.container_names)
 