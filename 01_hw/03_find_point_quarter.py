# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_coordinate = int(input('Enter x coordinate: '))
y_coordinate = int(input('Enter y coordinate: '))

if (x_coordinate == 0 or y_coordinate == 0):
    print('The point is located on one of the coordinate axes')
elif (x_coordinate > 0 and y_coordinate > 0):
    print('1')
elif (x_coordinate < 0 and y_coordinate > 0):
    print('2')
elif (x_coordinate < 0 and y_coordinate < 0):
    print('3')    
elif (x_coordinate > 0 and y_coordinate < 0):
    print('4')