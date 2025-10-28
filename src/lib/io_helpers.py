#Вспомогательные функции для работы с файлами
from pathlib import Path

def check_file_exists(file_path: str) -> None:
    """Проверяет существование файла"""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")

def ensure_directory_exists(file_path: str) -> None:
    """Создает директорию для файла, если она не существует"""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)