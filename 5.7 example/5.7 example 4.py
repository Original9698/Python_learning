n, m = map(int, input().split())
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    for j in range(m-1,-1,-1):
        print(a[i][j], end=' ')
    print()
