n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

summ = []
for i in a:
    summ.append(sum(i))

maxx = []
for i in a:
    maxx.append(max(i))

index = []
for i in a:
    index.append(summ.index(sum(i)))

max_score = 0
max_sum = 0
max_index = 0

for i in range(n):
    if maxx[i]>max_score:
        max_score = maxx[i]
        max_sum = summ[i]
        max_index = index[i]
    elif maxx[i]==max_score and summ[i]>max_sum:
        max_score = maxx[i]
        max_sum = summ[i]
        max_index = index[i]

print(max_score, max_sum, max_index)
