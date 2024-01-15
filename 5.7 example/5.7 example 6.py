n = 5
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            print(abs(2-i)+ abs(2-j))
