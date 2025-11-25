from collections import Counter
from io_txt_csv import read_text, write_csv
import sys
import os

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.text import normalize, tokenize


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


text = read_text("data/lab04/input.txt", encoding="utf-8")
freq = frequencies_from_text(text)
sorted_counts = sorted_word_counts(freq)

write_csv(sorted_counts, "data/lab04/report.csv", header=("word", "count"))

total_words = sum(freq.values())
unique_words = len(freq)

print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")
for word, count in sorted_counts[:5]:
    print(f"  {word}: {count}")
