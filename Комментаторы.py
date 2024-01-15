x = []
x1 = str()
while 'конец' not in x1:
    x1 = input()
    x += [x1.split(':')]

x = x[:-1]
y = {}
for i in x:
    if i[0] not in y.keys():
        y.setdefault(i[0], [i[1]])
    else:
        y[i[0]].append(i[1])

for i in y.keys():
    y[i] = set(y[i])

[print(f'Количество уникальных комментаторов у {i[0]} - {len(i[1])}') for i in sorted(y.items(), key = lambda x: len(x[1]), reverse = True)]