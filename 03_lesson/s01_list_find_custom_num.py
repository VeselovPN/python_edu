# Задайте список, состоящий из произвольных чисел, количество задает пользователь. Напишите программу,
# определяющую присутствует ли в заданном списке число, полученное от пользователя
# in >> 10
# in >> 13
# out >> [13,11,21,7,14,5,1,16,14,15]
# >> "the number - 13 is present in the list"

from random import sample


def find_num(list_len, my_num):
    mylist = sample(range(1, list_len * 2), my_num)
    print(mylist)
    # if my_num in mylist:
    #     return (f'The number {my_num} is present in the list')
    # return 'no'
    return 'yes' if my_num in mylist else 'no'

print(find_num(int(input('Enter a list length: ')), int(input('Enter your number: '))))
