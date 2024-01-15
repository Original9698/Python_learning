n, m = map(int, input().split())
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

# for x in a:
#     print(x)
for i in range(n):
    summ = 0
    for j in range(m):
        summ += a[i][j]
    print(summ, end= ' ')
print()

for i in range(m):
    summ = 0
    for j in range(n):
        summ += a[j][i]
    print(summ, end= ' ')