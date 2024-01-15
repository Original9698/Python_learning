n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

diagonal = []

for i in range(n):
    diagonal.append((a[i][(n - 1) - i]))

print(max(diagonal))
