from timeit import timeit


def my_func(x, y):
    if y >= 0:
        print(f'Значение переменной y, равное {y} не удовлетворяет условию задачи!')
        return None

    result = 1
    for i in range(0, y, -1):
        result *= x

    return 1 / result


x = 6
y = -6
result = my_func(x, y)
if result:
    print(f'{x} в степени {y} равно {result}')

x = 3
y = -1
result = my_func(x, y)
if result:
    print(f'{x} в степени {y} равно {result}')

print(timeit("my_func(x, y)", globals=(globals())))
