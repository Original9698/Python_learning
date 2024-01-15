n = int(input())
name = {(f'name{str(i)}'): None for i in range(1, n + 1)}
# print(name)
a= []
for key in name.keys():
    name[key] = input()
    a.append(name[key])
    if list(name.values()).count(name[key]) == 1:
        print('OK')
    else:
        name[key] += str(a.count(name[key])-1)
        print(name[key])

