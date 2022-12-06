# Задайте список, состоящий из произвольных слов, кол-во задает пользователь. Напишите программу, которая
# определеит индекс второго вхождения строки в списке, либо сообщит, что ее нет
# in >> 6
# out >> ['xzy','yxz','xxz','xzy','yzz','xzy']
# in >> xzy
# out >> 3

from random import choices, sample, randint


def create_list(k):
    word_list = []
    for i in range(k):
        letter_list = choices('xyz', k=3)
        word_list.append("".join(letter_list))
    return word_list


gen_word_list = create_list(int(input('Enter your number: ')))
print(gen_word_list)

find_text = input('Enter text to search: ')


def find_second_occurence(cur_list, find_text):
    if cur_list.count(find_text) > 1:
        first_index = cur_list.index(find_text)
        return cur_list.index(find_text, first_index + 1)
    else:
        return -1


print(find_second_occurence(gen_word_list, find_text))
