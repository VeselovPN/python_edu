# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меноьшее число. В качестве разделителя
# используйте пробел.
# in>> 11 23 90 -8 12 7 45
# out>> -44 90
#
# in >> 1, 6. 8: 9! -4
# out >> -4 9
#
# in >> 1 y 6 g 8
# out >> 'the data is incorrect"


def cleaner(user_string: str):
    user_list = user_string.split()
    for i, item in enumerate(user_list):
        user_list[i] = item.strip('.,:!')
        if not user_list[i].replace('-', '').isdigit():
            print('incorrect data')
            return []
    return user_list


def diff(list_for_diff: list):
    if list_for_diff: # if list_for_diff is empty > FALSE, else go to next string
        min_value = min(list_for_diff, key=int)
        max_value = max(list_for_diff, key=int)
        return min_value, max_value
    return 0, 0


user_input = input()
input_list = cleaner(user_input)
min_val, max_val = diff(input_list)
print(f'Min value = {min_val}, max value = {max_val}')
