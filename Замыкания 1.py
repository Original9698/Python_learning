def create_accumulator():
    count = 0
    def inner(numbers):
        nonlocal count
        count +=numbers
        return count
    return inner

a = create_accumulator()
print(a(1))