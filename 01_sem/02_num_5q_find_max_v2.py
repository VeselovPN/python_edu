# Find max number among 5 numbers

max_num = 0

for i in range(5):
    number_tmp = int(input('Enter next number: '))
    if (number_tmp > max_num):
        max_num = number_tmp

print('Max number is: ',max_num)
