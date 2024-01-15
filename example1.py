x = input()
a = [int(i) for i in x if i.isdigit()]
t = [i for i in x if i.istitle()]
if len(x) > 10 and len(a) >= 3 and len(t) >= 1 and '!' in x or '@' in x or '#' in x or '$' in x or '%' in x:
    print('Perfect password')
else:
    print('Easy peasy')