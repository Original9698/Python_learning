n = int(input())
a = [list(([0] * n)) for i in range(n)]
A, B, C = map(int, input().split())
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = C
        elif i > j:
            a[i][j] = B
        else:
            a[i][j] = A
for i in a:
    print(i)
