a = list(map(str,input().lower().split(',')))
set_a = set()
for i in a:
    if i not in set_a:
        set_a.add(i)
        print('НЕТ')
    else:
        print('ДА')
