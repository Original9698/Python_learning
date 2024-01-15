# функция merge_two_list должна объединить два списка
def merge_two_list(a, b):
    c=a+b
    r=[]
    while len(c)!=0:
           r.append(min(c))
           c.remove(min(c))
    return r
# функция merge_sort должна выполнить сортировку
def merge_sort(s,N):
    if len(s)==1:
        return s
    else:
        a = merge_sort(s[:(N//2)],N//2)
        b = merge_sort(s[(N//2):],N-N//2)
        return merge_two_list(a, b)

N = int(input())
s = list(map(int,input().split()))
print(*merge_sort(s,N))