# Calculate the sum of the digits of the input number
# in
# >>6731
# out
# >>17
# in
# >> 0.67
# out
# >>13

num = float(input('Enter your number: '))

num_sum = 0

# In this solution, the fractional part of the number is limited to two digits (0.00)
# Move the fractional part of the number to the left side of the point.
num = num * 100

while num > 9:
    num_sum = num_sum + num % 10
    # print('num_sum(temporary): ', num_sum)
    num = int(num / 10)
    # print('num/10 result(temporary): ', num)
else:
    num_sum = num_sum + num

print(int(num_sum))
