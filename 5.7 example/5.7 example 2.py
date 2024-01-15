n = int(input())
a=[]

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()