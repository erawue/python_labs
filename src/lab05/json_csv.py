import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON в CSV"""
    
    # Читаем JSON
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    
    # Получаем все ключи
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    fieldnames = sorted(all_keys)
    
    # Создаем папку если нужно
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Пишем CSV
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            row = {field: item.get(field, '') for field in fieldnames}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON"""
    
    # Читаем CSV
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    # Создаем папку если нужно
    Path(json_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Пишем JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print("Тестируем JSON → CSV...")
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")
    
    print("Тестируем CSV → JSON...")
    csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json")
    
    print("Готово!")