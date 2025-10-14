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
print(min_max([3, -1, 5, 5, 0]))     # (-1, 5)
print(min_max([42]))                 # (42, 42)
print(min_max([-5, -2, -9]))         # (-9, -2)
print(min_max([1.5, 2, 2.0, -3.1]))  # (-3.1, 2)
print(min_max([]))                   # ValueError

print("Тесты unique_sorted:")
print(unique_sorted([3, 1, 2, 1, 3]))        # [1, 2, 3]
print(unique_sorted([]))                     # []
print(unique_sorted([-1, -1, 0, 2, 2]))      # [-1, 0, 2]
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))  # [0, 1.0, 2.5]

print("Тесты flatten:")
print(flatten([[1, 2], [3, 4]]))        # [1, 2, 3, 4]
print(flatten([[1, 2], [3, 4, 5]]))     # [1, 2, 3, 4, 5]
print(flatten([[1], [], [2, 3]]))       # [1, 2, 3]
print(flatten([[1, 2], "ab"]))          # TypeError