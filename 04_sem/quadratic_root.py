# Найдите корни квадратного уравнения Ax^2 + Bx + C = 0, с помощью модуля. Запросите значения A,B,C 3 раза. Уравнения
# и крони запишите в файл
# Enter the coefficient 'a':1
# Enter the coefficient 'b':2
# Enter the coefficient 'c':-3
# 1x ** 2 + 2x + -3
# The first root: 1.00
# The first root: -3.00

from math import sqrt


def discr(a: int, b: int, c: int):
    res = b ** 2 - 4 * a * c
    with open("new_file.txt", 'a', encoding='utf-8') as cur_file:

        if res > 0:
            q_root1 = (-b + sqrt(res)) / (2 * a)
            q_root2 = (-b - sqrt(res)) / (2 * a)
            cur_file.writelines([f'{q_root1},{q_root2}\n'])
        elif res == 0:
            q_root1 = (-b) / (2 * a)
            cur_file.write(f'{q_root1}\n')
        else:
            # pass
            cur_file.write('there are not roots\n')


for i in range(3):
    a, b, c = int(input()), int(input()), int(input())
    discr(a, b, c)
