# Print a first digit of a fractional part of a number

number = float(input('Enter the number: '))

if number%1 != 0:
    # print(number%1)
    # print(int(number%1*10//1))
    # print(float(number)%int(number))
    print(int(number*10%10))
else:
    print('no')
