# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти


quarter_num = int(input('Enter quarter number: '))

if quarter_num == 1:
    print('x > 0, y > 0')
elif quarter_num == 2:
    print('x < 0, y > 0')
elif quarter_num == 3:
    print('x < 0, y < 0')
elif quarter_num == 4:
    print('x > 0, y < 0')
else:
    print('The entered number does not match the quarter in the Cartesian coordinate system')