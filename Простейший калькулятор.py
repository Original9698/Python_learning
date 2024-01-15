def calculate(x: float, y: float, operation: str = 'a'):
    def addition(x, y):
        print(x + y)

    def subtraction(x, y):
        print(x - y)

    def division(x, y):
        if y == 0:
            print('На ноль делить нельзя!')
        else:
            print(x / y)

    def multiplication(x, y):
        print(x * y)

    c = {'a': addition,
         's': subtraction,
         'd': division,
         'm': multiplication}
    if operation in c:
        result = c[operation](x, y)
        return result
    else:
        print('Ошибка. Данной операции не существует')
        return float('nan')  # Возвращаем NaN в случае неподдерживаемой операции


x = float(input())
y = float(input())
operation = input()

calculate(x, y, operation)