n = int(input())
n1 = list(map(int, input().split()))
count = [0] * 201
for i in n1:
    count[i + 100] += 1
for i in range(201):
    if count[i] > 0:
        print((str(i - 100)+' ') * count[i],end='')
