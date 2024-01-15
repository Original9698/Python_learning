def flatten(x):
    if not x:
        return []
    if isinstance(x[0],list):
        return flatten(x[0]) + flatten(x[1:])
    return x[:1] + flatten(x[1:])

def mean(x):
    return sum(x)/len(x)

x = []
x1 = str()
while 'конец' not in x1:
    x1 = input()
    x += [x1.split(',')]

x = x[:-1]
y = {}
for i in x:
    if i[0] not in y.keys():
        y.setdefault(i[0], [int(i[1])])
    else:
        y[i[0]].append(int(i[1]))

abs_y = {i: mean(j) for i,j in y.items()}


[print(f'{i[0]}, {i[1]}') for i in sorted(abs_y.items(), key = lambda x: x[1], reverse = True)]