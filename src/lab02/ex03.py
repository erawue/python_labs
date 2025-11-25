# Задание C
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    group_ = group.strip()
    parts = (
        fio.strip().title()
    ).split()  # убираем лишнии пробелы, изменяем регист и разбиваем на части
    # инициалы
    if len(parts) < 2:  # если только фамилия - возвращаем только фамилию
        inicial = ""
    elif len(parts) == 2:  # фамилия + имя
        inicial = f"{parts[1][0]}."
    else:  # фамилия + имя + отчество
        inicial = f"{parts[1][0]}.{parts[2][0]}."
    # полное имя с инициалами
    name = f"{parts[0]} {inicial}" if inicial else parts[0]
    gpa_ = f"{gpa:.2f}"  # gpa с двуми знаками после запятой
    return f"{name}, гр. {group_}, GPA {gpa_}"


print(format_record(("Иванов Иван Иванович", "ВIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record((" сидорова вина сергеевна ", "ABB-01", 3.999)))
