# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа)
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2,4),(8,64), (38,1444)]


# path = "D:\ego\edu\gb\edu\2022-1q_python\_coding\03_lec\textfile.txt"
path = "textfile.txt"
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':  # While string not empty
    space_pos = data.index(' ')  # find first space position index
    numbers.append(int(data[:space_pos]))  # take all data from first symbol to th first space position index
    data = data[space_pos + 1:]  # renew string

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))

print(out)
