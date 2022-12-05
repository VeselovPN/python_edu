# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет


weekday = int(input('Enter the number of the day of the week (to define the holiday): '))


if weekday in range(6,8):
    print(True)
elif weekday in range(1,6):
    print(False)
else:
    print('Incorrect input data')
