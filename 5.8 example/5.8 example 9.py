n = int(input())
a = []
for i in range(n):
    a.append([0] * n)

i = 1
x = -1
y = 0
d_x = 1
d_y = 0

while i <= n ** 2:
    if 0 <= x + d_x < n and 0 <= y + d_y < n and a[y + d_y][x + d_x]==0:
        x += d_x
        y += d_y
        a[y][x] = i
        i += 1
    else:
        if d_x == 1:
            d_x = 0
            d_y = 1
        elif d_y == 1:
            d_y = 0
            d_x = -1
        elif d_x == -1:
            d_x = 0
            d_y = -1
        elif d_y == -1:
            d_y = 0
            d_x = 1

for i in range(n):
    print(*a[i])