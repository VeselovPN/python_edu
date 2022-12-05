# Print a list filled with elements according to the formula (1+1/n)**n. Show the sum
# in >> 6
# out >> 2.0, 2.25, 2.37, 2.441, 2.488, 2.522
# out >> 14.071.

n = int(input('Enter your number: '))

list_result = []
sum_res = 0
next_element = 0

for i in range(1, n + 1):
    next_element = (1 + 1 / i) ** i
    list_result.append(next_element)
    sum_res += next_element

print('list: ',list_result)
print('sum of elements: ',sum_res)
