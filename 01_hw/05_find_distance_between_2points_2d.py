# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099

pointA_x_coordinate = int(input('Enter x coordinate of point A: '))
pointA_y_coordinate = int(input('Enter y coordinate of point A: '))

pointB_x_coordinate = int(input('Enter x coordinate of point B: '))
pointB_y_coordinate = int(input('Enter y coordinate of point B: '))

if (pointA_x_coordinate == pointB_x_coordinate) and (pointA_y_coordinate == pointB_y_coordinate):
    print('The coordinates of two points are equal')
else:
    print('distance between two points (2d): ',f'{((pointB_x_coordinate - pointA_x_coordinate)**2 + (pointB_y_coordinate - pointA_y_coordinate)**2)**0.5:0.3}')