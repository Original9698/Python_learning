n, m = map(int, input().split())
a = [list((input())) for i in range(n)]
a.append(['.']*(m))
a.insert(0,['.']*(m))
for i in range(n+2):
    a[i].append('.')
    a[i].insert(0,'.')

count = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j] == '.' and a[i-1][j] == a[i][j+1] == a[i+1][j] == a[i][j-1] == a[i][j]:
            count += 1
        else:
            continue
print(count)