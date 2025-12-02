import json
import sys
import os

# Решаем проблему импорта
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

try:
    from models import Student
except ImportError:
    # Пробуем относительный импорт
    from .models import Student


def students_to_json(students, path):
    students = sorted(students, key=lambda s: s.gpa, reverse=True)
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Student.from_dict(item) for item in data]


if __name__ == "__main__":
    # Используй абсолютный путь
    import os
    current_dir = os.path.dirname(__file__)
    input_path = os.path.join(current_dir, "..", "..", "data", "lab08", "students_input.json")
    
    students = students_from_json(input_path)
    
    for student in students:
        print(student)
    
    output_path = os.path.join(current_dir, "..", "..", "data", "lab08", "students_output.json")
    students_to_json(students, output_path)