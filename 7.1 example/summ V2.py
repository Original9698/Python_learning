# def sum_num(n):
#     s = [int(i) for i in n if i.isdigit()]
#     print(sum(s))
#
# sum_num(input())
def sum_num(n):
    S = 0
    for i in n:
        if i.isdigit():
            S+=int(i)
    print(S)

sum_num(input())