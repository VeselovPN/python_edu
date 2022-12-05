# Verify a number for multiplicity 5,10,15 excluding the number 30

number = int(input('Enter the number: '))

# if (((number%5)==0 and (number%10)==0) or (number%15==0)) and number%30!=0:
if (((number%5)==0 and (number%10)==0) or (number%15==0)) and number%30:
    print('yes')
else:
    print('no')

