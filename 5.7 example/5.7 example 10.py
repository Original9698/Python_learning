n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
summ = []
for i in a:
    summ.append(max(i))

winner = a[summ.index(max(summ))]

print(max(winner))

print(summ.index(max(summ)), winner.index(max(winner)))
