def check_password(x):
    a = [int(i) for i in x if i.isdigit()]
    t = [i for i in x if i.istitle()]
    s = [i for i in x if i in '!@#$%*']
    if len(x) >= 10 and len(a) >= 3 and len(t) > 0 and len(s)>0:
        print('Perfect password')
    else:
        print('Easy peasy')