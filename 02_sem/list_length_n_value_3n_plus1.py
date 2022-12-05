# create list, length n, value formula 3k+1, where k = range(1,n)

num = int(input('Enter your number: '))

list1 = []

for i in range(1, num+1):
    list1.append(3*i+1)

print(list1)



