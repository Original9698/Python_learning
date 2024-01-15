n = int(input())
a=[]
sum=0
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    for j in range(n):
        if i==j:
            sum+=a[i][j]
print(sum)