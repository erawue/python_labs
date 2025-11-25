import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic(tmp_path):
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"

    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    src.write_text(json.dumps(data), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
    assert rows[1]["name"] == "Bob"


def test_csv_to_json_basic(tmp_path):
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.json"

    csv_content = "name,age\nAlice,25\nBob,30"
    src.write_text(csv_content, encoding="utf-8")

    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[1]["name"] == "Bob"


def test_json_to_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


def test_csv_to_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


def test_json_to_csv_invalid_json(tmp_path):
    src = tmp_path / "invalid.json"
    dst = tmp_path / "test.csv"

    src.write_text("{ invalid json }", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_round_trip(tmp_path):
    # JSON → CSV → JSON
    original_data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]

    json1 = tmp_path / "1.json"
    csv_file = tmp_path / "data.csv"
    json2 = tmp_path / "2.json"

    json1.write_text(json.dumps(original_data), encoding="utf-8")
    json_to_csv(str(json1), str(csv_file))
    csv_to_json(str(csv_file), str(json2))

    with json2.open(encoding="utf-8") as f:
        final_data = json.load(f)

    assert len(final_data) == len(original_data)
    assert final_data[0]["name"] == original_data[0]["name"]
