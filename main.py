num = int(input('Введите число: '))

h = []

while num > 0:
    if num % 16 <= 9:
        h.append(num % 16)
        num //= 16
    if num % 16 == 10:
        h.append("A")
        num //= 16
    if num % 16 == 11:
        h.append("B")
        num //= 16
    if num % 16 == 12:
        h.append("C")
        num //= 16
    if num % 16 == 13:
        h.append("D")
        num //= 16
    if num % 16 == 14:
        h.append("E")
        num //= 16
    if num % 16 == 15:
        h.append("F")
        num //= 16
h.reverse()

for i in h:
    print(i, end='')
