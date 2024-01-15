n = int(input())
n1 = list(map(int, input().split()))
count = 0
for run in range(n - 1):
    for i in range(n - 1 - run):
        if n1[i] > n1[i + 1]:
            n1[i], n1[i + 1] = n1[i + 1], n1[i]
            count += 1
print(*n1)
print(count)
