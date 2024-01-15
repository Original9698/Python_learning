n = int(input())
n1 = []
last = 0
while n != 0:
    last = n % 10
    n = n // 10
    n1.append(last)
# print(n1)
n1.reverse()
# print(n1)
count = [0] * (max(n1)+1)
for i in n1:
    count[i] += 1
for i in range(len(count)):
    if count[i]>0:
        print(i, count[i])
