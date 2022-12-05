# 2 numbers. Is number A/B square of number A/B?
numA = int(input('Enter numberA: '))
numB = int(input('Enter numberB: '))

if (numA == numB**2 or numA == numB**(0.5)):
    print('yes')
else:
    print('no')    
