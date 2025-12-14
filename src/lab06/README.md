# Лабораторная работа 6 — CLI‑утилиты с argparse
- cli_text.py
```
import argparse
import sys
from pathlib import Path
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        # Реализация команды cat
        file_path = args.input

        if not Path(file_path).exists():
            print(f"Ошибка: файл {file_path} не найден")
            sys.exit(1)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, 1):
                if args.n:
                    print(f"{i}: {line}", end="")
                else:
                    print(line, end="")

        except Exception as e:
            print(f"Ошибка: {e}")
            sys.exit(1)

    elif args.command == "stats":
        # Реализация команды stats
        file_path = args.input

        if not Path(file_path).exists():
            print(f"Ошибка: файл {file_path} не найден")
            sys.exit(1)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Очистка текста и разбивка на слова
            words = text.lower().split()
            words = [word.strip('.,!?;:()"') for word in words if len(word) > 2]

            # Подсчет частот
            word_counts = Counter(words)
            top_words = word_counts.most_common(args.top)

            # Вывод результатов
            print(f"Топ-{args.top} самых частых слов:")
            for i, (word, count) in enumerate(top_words, 1):
                print(f"{i}. {word} — {count}")

        except Exception as e:
            print(f"Ошибка: {e}")
            sys.exit(1)

    else:
        print("Используйте: cat --input <файл> или stats --input <файл>")
        parser.print_help()


if __name__ == "__main__":
    main()

```

- cli_convert.py
```
import argparse
import sys
import os

lab05_path = os.path.join(os.path.dirname(__file__), "..", "lab05")
sys.path.append(lab05_path)

from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    # Вызываем код в зависимости от аргументов
    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()

```

## Результат
- **cli_text**




![alt text](../../images/lab06/img01.png)
![alt text](../../images/lab06/img02.png)
![alt text](../../images/lab06/img03.png)

- **cli_convert**

![alt text](../../images/lab06/img04.png)

![alt text](../../images/lab06/img05.png)

![alt text](../../images/lab06/img06.png)

![alt text](../../images/lab06/img07.png)