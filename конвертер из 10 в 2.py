a= int(input())
b=a
a1 = []
while b//2!=0 or b==1:
    a1.append(b % 2)
    b=int(b/2)
a1.reverse()
if a<0:
    for i in range(len(a1)):
        if a1[i]==0:
            a1[i]=1
        elif a1[i]==1:
            a1[i]=0
    a1[-1]+=1

print(*a1)