import os
from tg_notify import send_telegram_alert

def check_disk_space():
    statvfs = os.statvfs('/')
    free_space_gb = statvfs.f_frsize * statvfs.f_bavail / (1024 ** 3)
    return free_space_gb

# Проверка свободного места
free_space = check_disk_space()
min_disk_free_space = float(os.getenv('MIN_DISK_FREE_SPACE'))

print(f"Свободно {free_space:.2f} ГБ")

if free_space < min_disk_free_space:
    message = f"Внимание: на сервере осталось менее {min_disk_free_space} ГБ свободного пространства! Свободно {free_space:.2f} ГБ."
    response = send_telegram_alert(message)
    print(response.text)
