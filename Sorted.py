x = []

while 'конец' not in x:
    x.append(input())

x = x[:-1]

y = {str((i.split(':'))[0]): str((i.split(':'))[1]) for i in x}
[print(i[0]) for i in sorted(y.items(), key= lambda x:x[1], reverse = True)]