def my_func(*args):
    args = sorted(list(args), reverse=True)
    return args[0] + args[1]


try:
    print(my_func(1, 2, 3, 5))
except:
    print('Ошибка вызова функции!')

try:
    print(my_func(1, 0, 4))
except:
    print('Ошибка вызова функции!')
