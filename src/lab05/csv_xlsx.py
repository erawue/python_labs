import csv
from openpyxl import Workbook
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX"""

    # Читаем CSV
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Создаем XLSX
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    # Записываем данные
    for row in rows:
        ws.append(row)

    # Автоширина колонок
    for column in ws.columns:
        max_length = 0
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        # Минимум 8 символов
        width = max(max_length + 2, 10)
        ws.column_dimensions[column[0].column_letter].width = width

    # Сохраняем
    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)


if __name__ == "__main__":
    print("Тестируем CSV → XLSX...")
    csv_to_xlsx("data/lab05/samples/people.csv", "data/lab05/out/people.xlsx")
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities_from_csv.xlsx")
    print("Готово!")
