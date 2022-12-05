# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
#
# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

num_n = int(input('Enter your number: '))
num_pos1 = int(input('Enter position 1: '))
num_pos2 = int(input('Enter position 2: '))

list_res = []

for i in range(-num_n, num_n + 1):
    list_res.append(i)

print(list_res)

if (num_pos1 > len(list_res)) or (num_pos2 > len(list_res)):
    print('There are no values for these indexes!')
else:
    print(list_res[num_pos1-1]*list_res[num_pos2-1])
