# Print range from -N to N

N = int(input('Enter your number: '))

if N > 0:
    print(*range(-N,N+1))
else:
    # print (*range(N,-N+1))
    print(*range(-N,N-1,-1))