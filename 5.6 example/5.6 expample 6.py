n = int(input()) # Длина массива чисел
s = list(map(int, input().split())) #Массив чисел
for i in range(n): # проходим по массиву n раз
    for j in range(i,0,-1):
        if s[j]<s[j-1]:                  #Если число меньше чем предыдущее,
            s[j],s[j-1] = s[j-1],s[j]    # меняем их местами
        else:                            # если условие не выполняется, выходим из внутреннего цикла, т.к.предыдущие числа отсортированы
            break
print (*s)