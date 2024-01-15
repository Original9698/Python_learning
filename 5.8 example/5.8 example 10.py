n,m = map(int,input().split())

a = [list((input())) for i in range(n)]
count=0

for i in range(n):
    if 'S' not in a[i]:# Находим колличество строк где нет 'S'
        count+=m #Добавляем к счетчику колличество элементов строки
        a[i].clear()#Удаляем строку без клубничек
        for j in range(m):
            a[i].insert(j,1)#Маркируем ее единичками
for i in range(m):
    check = []
    for j in range(n):
        check.append(a[j][i])
    if 'S' not in check:
        count+=n - check.count(1)

print(count)



