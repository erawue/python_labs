# Лабораторная работа 2

## Задание A
# Массивы
```
# Задание А
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return "ValueError"
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    R = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            return "TypeError"  
        R.append(i)
    return R

print("Тесты min_max:")
print(min_max([3, -1, 5, 5, 0]))    
print(min_max([42]))                
print(min_max([-5, -2, -9]))      
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))                  

print("Тесты unique_sorted:")
print(unique_sorted([3, 1, 2, 1, 3]))        
print(unique_sorted([]))                    
print(unique_sorted([-1, -1, 0, 2, 2]))      
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))  

print("Тесты flatten:")
print(flatten([[1, 2], [3, 4]]))       
print(flatten([[1, 2], [3, 4, 5]]))  
print(flatten([[1], [], [2, 3]]))      
print(flatten([[1, 2], "ab"]))   
```
![alt text](images/lab02/img01.png)

## Задание B
# Матрицы
```
#Задание B
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return [] # если матрица пустая
    for i in mat:
        if len(i) != len(mat[0]): 
            return "ValueError" # если строки разной длины
    R = []
    for i in range(len(mat[0])): # проходим по всем столбцам
        N = []
        for j in range(len(mat)): # проходим по всем строкам
            N.append(mat[j][i])
        R.append(N)
    return R

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    for i in mat:
        if len(i) != len(mat[0]):
            return "ValueError"
    return [sum(i) for i in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    for i in mat:
        if len(i) != len(mat[0]):
            return "ValueError"
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]

print("Тесты transpose:")
print(transpose([[1, 2, 3]])) 
print(transpose([[1], [2], [3]]))  
print(transpose([[1, 2], [3, 4]]))  
print(transpose([]))  
print(transpose([[1, 2], [3]]))  

print("Тесты row_sums:")
print(row_sums([[1, 2, 3], [4, 5, 6]]))  
print(row_sums([[-1, 1], [10, -10]]))  
print(row_sums([[0, 0], [0, 0]]))  
print(row_sums([[1, 2], [3]]))  

print("Тесты col_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))  
print(col_sums([[-1, 1], [10, -10]]))  
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]])) 
```
![alt text](images/lab02/img02.png)

## Задание C
# Кортежи
```
# Задание C
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    group_ = group.strip()
    parts = (fio.strip().title()).split() # убираем лишнии пробелы, изменяем регист и разбиваем на части
    # инициалы
    if len(parts) < 2:  # если только фамилия - возвращаем только фамилию
        inicial = ""
    elif len(parts) == 2:  # фамилия + имя
        inicial = f"{parts[1][0]}."
    else:   # фамилия + имя + отчество
        inicial = f"{parts[1][0]}.{parts[2][0]}."
    # полное имя с инициалами
    name = f"{parts[0]} {inicial}" if inicial else parts[0]
    gpa_ = f"{gpa:.2f}" # gpa с двуми знаками после запятой
    return f"{name}, гр. {group_}, GPA {gpa_}"

print(format_record(("Иванов Иван Иванович", "ВIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record((" сидорова вина сергеевна ", "ABB-01", 3.999)))
```
![alt text](images/lab02/img03.png)