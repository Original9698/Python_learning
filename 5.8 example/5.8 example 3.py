n = int(input())

a = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    d = a[i][0]
    for j in range(n):
        if d == a[j][1] and [i] != [j]:
            count += 1
print(count)