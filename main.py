num = int(input('Введите число: '))

h = []
hh = 16
while num > 0:
    if num % hh <= 9:
        h.append(num % 16)
        num //= hh
    if num % hh == 10:
        h.append("A")
        num //= hh
    if num % hh == 11:
        h.append("B")
        num //= hh
    if num % hh == 12:
        h.append("C")
        num //= hh
    if num % hh == 13:
        h.append("D")
        num //= hh
    if num % hh == 14:
        h.append("E")
        num //= hh
    if num % hh == 15:
        h.append("F")
        num //= hh
h.reverse()

for i in h:
    print(i, end='')
