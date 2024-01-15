n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([0] * m)
count = -1
for i in range(n):
    for j in range(m):
        a[i][j] = count + 1
        count += 1

for i in range(n):
    if i % 2 == 1:
        a[i].reverse()

for i in range(n):
    print(*a[i])