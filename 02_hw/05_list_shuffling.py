# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import copy
import datetime
import time

num = int(input('Enter your number to create a list: '))
mixing_num = int(input('Enter the number for elements mixing (n=20, mixing=1000 ~ 5sec): '))


# Create base list.
list_base = []
for i in range(0, num):
    list_base.append(i)
print('initial list', list_base)


# Get number of digits in the length of the list.
def get_number_length(num_n):
    depth_num = 0
    if num_n < 10:
        depth_num = 1
    else:
        while num_n > 9:
            depth_num += 1
            num_n = int(num_n / 10)
        depth_num += 1
    return depth_num


# Get random replacement index from current microsecond time
def get_random_replacement_index(depth_num_n, num_n):
    last_digits = 0
    time_now = datetime.datetime.now()
    last_digits = int(time_now.microsecond % (10 ** depth_num_n))
    while last_digits > (num_n - 1):
        last_digits = int(last_digits / 2)
    return last_digits


# Swap elements around the middle of the list
def swap_elements(source_list, half_length, rand_num):
    buf_num = 0
    if rand_num <= half_length:
        buf_num = source_list[rand_num]
        source_list[rand_num] = source_list[half_length + rand_num - 1]
        source_list[half_length + rand_num - 1] = buf_num
    elif rand_num > half_length:
        buf_num = source_list[rand_num]
        source_list[rand_num] = source_list[rand_num - half_length]
        source_list[rand_num - half_length] = buf_num
    return source_list


# Multiple swapping of elements
def mix_list(shuffling_list, rotate_num):
    list_renew = []
    for j in range(rotate_num):
        list_renew = swap_elements(shuffling_list, int(num / 2), get_random_replacement_index(list_depth, num))
        shuffling_list = copy.deepcopy(list_renew)
        # print(list_renew)
        time.sleep(0.01)
    return list_renew


list_depth = get_number_length(num)
print('Number length/list depth: ', list_depth)
random_index = get_random_replacement_index(list_depth, num)
print('Random digits(index for swap) ', random_index)
one_mod_list = swap_elements(list_base, int(num / 2), get_random_replacement_index(list_depth, num))
result_list = mix_list(one_mod_list, mixing_num)
print('result list: ', result_list)