# Задайте список, состоящий из произвольных чисел, кол-во задает пользователь. Напишите программу, которая найдет сумму
# элементов списка, стоящих на нечётных позициях (не индексах).
# in >> 4
# out >> [7,9,2,3]
# >> 9
#
# in >> 5
# out >> [2,5,2,7,9]
# >> 13

from random import choices


def create_list(el_num):
    num_list_init = choices(range(10), k=el_num)
    return num_list_init


def get_sum_odd_pos_el(cur_list):
    odd_el_sum = 0
    for i in range(0, len(cur_list), 2):
        odd_el_sum += cur_list[i]
        # print(f'index:{i}, sum:{odd_el_sum}')
    # ver.1 - without range increment
    # odd_el_sum = cur_list[0]
    # for i in range(1, len(cur_list)):
    # if i % 2 == 0:
    return odd_el_sum


num_list = create_list(int(input('Enter number of elements in a list: ')))
print(num_list)
print(get_sum_odd_pos_el(num_list))
