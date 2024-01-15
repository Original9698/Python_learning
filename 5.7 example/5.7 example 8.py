n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            print('No')
            break
        else:
            continue

    if a[i][j] != a[j][i]:
        break
    else:
        print('Yes')
        break
