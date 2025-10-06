#Задание B
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return [] # если матрица пустая
    len_s = len(mat[0]) # длина первой строчки
    for i in mat:
        if len(i) != len_s: 
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
    len_s = len(mat[0])
    for i in mat:
        if len(i) != len_s:
            return "ValueError"
    R = []
    for i in mat:
        R.append(sum(i))
    return R

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    len_s = len(mat[0])
    for i in mat:
        if len(i) != len_s:
            return "ValueError"
    R = []
    for i in range(len(mat[0])):
        sum_s = 0
        for j in range(len(mat)):
            sum_s += mat[j][i]
        R.append(sum_s)
    return R

print("Тесты transpose:")
print(transpose([[1, 2, 3]]))  # [[1], [2], [3]]
print(transpose([[1], [2], [3]]))  # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([]))  # []
print(transpose([[1, 2], [3]]))  # ValueError

print("Тесты row_sums:")
print(row_sums([[1, 2, 3], [4, 5, 6]]))  # [6, 15]
print(row_sums([[-1, 1], [10, -10]]))  # [0, 0]
print(row_sums([[0, 0], [0, 0]]))  # [0, 0]
print(row_sums([[1, 2], [3]]))  # ValueError

print("Тесты col_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))  # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))  # [9, -9]
print(col_sums([[0, 0], [0, 0]]))  # [0, 0]
print(col_sums([[1, 2], [3]]))  # ValueError 