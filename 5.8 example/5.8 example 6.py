n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        a[i][j] = a[i + 1][j] + a[i][j + 1]

for i in range(n):
    print(*a[i])
print()
