import os

def load_environment_variables(env_file=".env"):
    """Загрузка переменных окружения из файла .env."""
    try:
        with open(env_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Warning: '{env_file}' file not found.")
    except Exception as e:
        print(f"Error loading the .env file: {e}")
