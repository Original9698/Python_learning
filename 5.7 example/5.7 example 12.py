n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
count = 0

maxx = []
for i in a:
    maxx.append(max(i))

max_score = max(maxx)

for i in maxx:
    if i == max_score:
        count+=1

print(count)
