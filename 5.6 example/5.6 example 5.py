n, m = map(int, input().split())
count = 0
a = 0
b = 0
while a ** 2 <= n:
    a += 1
    b = n - a ** 2
    if a + b ** 2 == m and b >= 0:
        count += 1

print(count)
