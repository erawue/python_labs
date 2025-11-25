import csv
import os
from typing import Iterable, Sequence


def read_text(path: str, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as file:
        content = file.read()
    return content


def write_csv(
    rows: Iterable[Sequence], path: str, header: tuple[str, ...] | None = None
) -> None:
    # Создаем папку если нет
    os.makedirs(os.path.dirname(path), exist_ok=True)

    rows = list(rows)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")
    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("Мини-тесты выполнены! Создан check.csv")
    print("Файл создан: data/lab04/check.csv")
