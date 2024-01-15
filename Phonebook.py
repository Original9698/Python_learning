n = int(input())
phonebook = tuple(input().split() for i in range(n))
phonebook_dict = {}
for i in phonebook:
    if i[1] not in phonebook_dict.keys():
        phonebook_dict.setdefault(i[1], int(i[0]))
    else:
        a = phonebook_dict.pop(i[1])
        phonebook_dict.setdefault(i[1], (int(a),int(i[0])))

m = int(input())
search = [input() for i in range(n)]

for i in search:
    if type(phonebook_dict.get(i,'Неизвестный номер')) is not tuple:
        print(phonebook_dict.get(i,'Неизвестный номер'))
    else:
        print(*phonebook_dict.get(i, 'Неизвестный номер'))
