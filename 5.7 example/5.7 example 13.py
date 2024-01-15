a = [input() for i in range(4)]
count=0
for i in range(3):

    for j in range(3):
        if a[i][j] == a[i+1][j] == a[i][j+1] == a[i+1][j+1]:
            print('No')
            break
        else:
            continue

    if a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1]:
        break
    else:
        count+=1

if count==3:
    print('Yes')


