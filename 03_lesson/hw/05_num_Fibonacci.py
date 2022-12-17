# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
# in >> 8
# out >> -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in >> 3
# out >> 2 -1 1 0 1 1 2

el_number = int(input('Enter your number: '))


def check_el_num_value(el_num):
    get_fib_list(el_num) if el_num > 1 else print('Please, re-enter your number')


def get_fib_list(el_n):
    fib_list = [0] * (el_n * 2 + 1)
    j = int(len(fib_list) / 2)
    fib_list[j] = 0
    fib_list[j + 1] = 1
    fib_list[j - 1] = 1

    for i in range(j + 2, len(fib_list)):
        fib_list[i] = fib_list[i - 2] + fib_list[i - 1]
        fib_list[len(fib_list) - i - 1] = (-1) ** (i - j + 1) * fib_list[i]

    print(fib_list)


check_el_num_value(el_number)
