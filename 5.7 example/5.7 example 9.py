n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
summ = []
for i in a:
    summ.append(sum(i))

print(max(summ))
print(summ.index(max(summ)))