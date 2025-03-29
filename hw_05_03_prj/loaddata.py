from pathlib import Path


def load_data(filename: str) -> list[str]:
    """Загружает логи из файла и возвращает список строк."""
    file_path = Path(__file__).parent / filename
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            return f.readlines()
    else:
        print(f"Файл {filename} не найден!")
        return []
