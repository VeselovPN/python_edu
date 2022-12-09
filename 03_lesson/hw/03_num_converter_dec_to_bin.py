# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без использования:
# встроенной ф-и преобразования строк
# in >> 13
# out >> 1101
#
# in >> 88
# out >> 1011000


num_dec = int(input('Enter your number: '))
print(num_dec)


def convert_to_bin(num_d):
    bin_list = []
    for i in range(0, 2):
        while num_d != 0:
            # print(num_d % 2, end='')
            bin_list.append(num_d % 2)
            num_d = int(num_d / 2)
    return bin_list


def invert_bin_list(b_list):
    # for j in range(len(b_list)):
    for j in range(len(b_list)):
        print(b_list[len(b_list) - 1 - j], end='')


invert_bin_list(convert_to_bin(num_dec))
