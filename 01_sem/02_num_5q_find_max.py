# Find max number among 5 numbers
num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
num3 = int(input('Enter number3: '))
num4 = int(input('Enter number4: '))
num5 = int(input('Enter number5: '))

numbers = [num1,num2,num3,num4,num5]
# numbers = [num1,num2,num3,num4,num5]

i = 0
max_num = numbers[0]

while i < (len(numbers)-1):
    if (numbers[i] < numbers[i+1]):
        max_num = numbers[i+1]
        i+=1
    else:
        i+=1

print(max_num)