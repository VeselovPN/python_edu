# Напишите программу, которая найдет произведение пар чисел из списка. Парой считаем первый и последний эл-т,
# второй и предпоследний.
# in >> 4
# out >> [8,9,10,10]
# >> [80,90]
#
# in >> 5
# out >> [3,3,6,8,4]
# >> [12,24,6]


from random import choices


def create_list(el_num):
    num_list_init = choices(range(10), k=el_num)
    return num_list_init


def get_opposite_el_pair_product(cur_list):
    result_list = []
    for i in range(0, int(len(cur_list) / 2)):
        result_list.append(cur_list[i] * cur_list[len(cur_list) - 1 - i])
    if len(cur_list) % 2 != 0:
        result_list.append(cur_list[int(len(cur_list) / 2)])
    return result_list


num_list = create_list(int(input('Enter number of elements in a list: ')))
print(num_list)

print(get_opposite_el_pair_product(num_list))
