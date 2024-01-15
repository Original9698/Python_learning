n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

for i in a:
    print(sum(i), end=' ')
print()

for i in range(m):
    print(sum([j[i] for j in a]), end=' ')
