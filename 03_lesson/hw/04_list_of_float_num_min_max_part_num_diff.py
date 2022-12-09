# задайте список из произвольных вещественных чисел, кол-во задает пользователь. Напишите программу, которая найдет
# разницу между максимальным и минимальным значением дробной части элементов
# in >> 3
# out >> [2.84, 9.42, 1.87]
# >> "Min: 0.42, Max: 0.87. Difference: 0.45"
#
# in >> 4
# out >> [4.83, 9.91, 7.74, 9.39]
# >> "Min: 0.39, Max: 0.91. Difference: 0.52"

import random

elements_num = int(input('Enter your number of elements: '))


def get_float_num_list(el_num):
    float_num_list = []
    for i in range(0, el_num):
        float_num_list.append(float('{:.2f}'.format(random.uniform(-9.99, 9.99))))
    print(float_num_list)

    for j in range(0, len(float_num_list)):
        float_num_list[j] = float('{:.2f}'.format(abs(float_num_list[j] - int(float_num_list[j]))))
    print(float_num_list)

    return float_num_list


def get_min_max(fl_num_list):
    print("Min:", min(fl_num_list), ", Max:", max(fl_num_list), \
          ", Difference: "'{:.2f}'.format(max(fl_num_list) - min(fl_num_list)))


# Version without min/max list functions
# def get_min_max(fl_num_list):
#     max_index = 0
#     buf_element = 0
#     max_element = fl_num_list[0]
#     for i in range(0, len(fl_num_list) - 1):
#         if fl_num_list[i] < fl_num_list[i + 1]:
#             max_element = fl_num_list[i + 1]
#         else:
#             max_element = fl_num_list[i]
#             fl_num_list[i] = fl_num_list[i + 1]
#             fl_num_list[i + 1] = max_element
#     min_element = len(fl_num_list) - 2
#     buf_element = 0
#     for i in range(0, len(fl_num_list) - 2):
#         if fl_num_list[i] > fl_num_list[i + 1]:
#             min_element = fl_num_list[i + 1]
#         else:
#             min_element = fl_num_list[i]
#             fl_num_list[i] = fl_num_list[i + 1]
#             fl_num_list[i + 1] = min_element
#     print(f'Min: {min_element}, Max: {max_element}, Difference: {max_element - min_element}')


get_min_max(get_float_num_list(elements_num))
