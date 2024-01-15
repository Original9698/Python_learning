row, line = map(int, input().split())
a = [input() for i in range(row)]
input()
b = [input() for i in range(row)]
count = 0
for i in range(row):
    for j in range(line):
        if a[i][j] == b[i][j]:
            count += 1
print(count)
