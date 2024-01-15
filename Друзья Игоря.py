def flatten(x):
    if not x:
        return ()
    if isinstance(x[0],tuple):
        return flatten(x[0]) + flatten(x[1:])
    return x[:1] + flatten(x[1:])


n = int(input())
friends = tuple(input().split() for i in range(n))
friends_dict = {}
for i in friends:
    if i[2] not in friends_dict.keys():
        friends_dict.setdefault(i[2], i[0])
    else:
        a = friends_dict.pop(i[2])
        friends_dict.setdefault(i[2], (i[0],a))

m = int(input())
search = [input() for i in range(m)]

for i in search:
    if type(friends_dict.get(i,'Нет данных')) is not tuple:
        print(friends_dict.get(i,'Нет данных'))
    else:
        print(*sorted(flatten(friends_dict.get(i, 'Нет данных')),key = lambda x: x[1]))