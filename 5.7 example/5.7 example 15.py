n, x = map(int, input().split())
a = []
for i in range(n):
    a.append([0] * n)
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        a[i - 1][j - 1] = i * j

    if x in a[i - 1]:
        count += 1
print(count)