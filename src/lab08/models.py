from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate.replace('.', '-'), "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {self.birthdate}")
        
        if not 0 <= self.gpa <= 5:
            raise ValueError(f"GPA должен быть от 0 до 5")
    
    def age(self):
        birth_date = datetime.strptime(self.birthdate.replace('.', '-'), "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    
    def to_dict(self):
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )
    
    def __str__(self):
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}, Возраст: {self.age()}"


if __name__ == "__main__":
    # Тестовый запуск
    test = Student("Иванов Иван Иванович", "2005.01.01", "BIVT-25", 4.5)
    print(test)
    print(f"Словарь: {test.to_dict()}")