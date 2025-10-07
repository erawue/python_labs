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