n = int(input())
k_off, k_on = 0,0
for i in range(n):
    s = input().split()
    f = s[-1]
    if f == "True":
        k_off += 1
    else:
        k_on += 1
print(f"{k_off} {k_on}")