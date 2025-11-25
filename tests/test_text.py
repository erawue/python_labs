import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello, world!", ["hello", "world"]),
        ("test one two three", ["test", "one", "two", "three"]),
        ("", []),
    ],
)
def test_tokenize_basic(text, expected):
    assert tokenize(text) == expected


def test_count_freq_and_top_n():
    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    freq = count_freq(tokens)
    assert freq == {"apple": 3, "banana": 2, "cherry": 1}

    top = top_n(freq, 2)
    assert top == [("apple", 3), ("banana", 2)]


def test_top_n_tie_breaker():
    # Все слова с одинаковой частотой, проверяем алфавитную сортировку
    freq = {"s": 2, "i": 2, "r": 2, "t": 2}
    result = top_n(freq, 4)
    # Правильный алфавитный порядок: i, r, s, t
    assert result == [("i", 2), ("r", 2), ("s", 2), ("t", 2)]
