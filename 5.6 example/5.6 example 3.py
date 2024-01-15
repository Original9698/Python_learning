n = int(input())
count = 0
for p in range(n + 1, 2 * n+1):
    for i in range(2,int(p**0.5+1)):
        if p%i==0:
            break
    else:
        count+=1

print(count)