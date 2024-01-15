def count_letters(letter):
    a = [i for i in letter if i.isalpha()]
    N = [i for i in a if i.istitle()]
    K = len(a)-len(N)
    print(f'Количество заглавных символов: {len(N)}\nКоличество строчных символов: {K}')

count_letters(input())