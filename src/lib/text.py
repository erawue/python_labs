import re
from collections import Counter

def normalize(text: str) -> str:
    text = text.lower()
    # Убираем все знаки препинания
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text: str) -> list[str]:
    # Просто разбиваем по пробелам
    return text.split()

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]