# Задайте два числа. Найдите наименьшее общее кратное этих двух чисел
# >>17
# >>11
# out: 187
#
# >>14
# >>18
# out: 126
#
# >>0
# >>0
# out: 0

from math import gcd

num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))

print((num1*num2) // gcd(num1,num2))