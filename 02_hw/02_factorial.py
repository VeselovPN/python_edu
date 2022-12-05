# Show a list of products of the number (factorial)
# in >> 3
# out >> 1,2,6
#
# in >> 6
# out >> 1,2,6,24,120,720

num = int(input('Enter your number: '))
res = 1

for i in range(1,num + 1):
    res *= i
    print(res, end=' ')
