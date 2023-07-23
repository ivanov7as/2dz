first = input(('Введите число формата a/b: '))
second = input(('Введите число формата a/b: '))


def fractionsum(first, second):
    f = first.split("/")
    s = second.split("/")
    sum = []
    if f[1]!=s[1]:
        sum.append(int(int(f[0]) * int(f[1]) * int(s[1]) / int(f[0]) + int(s[0]) * int(f[1]) * int(s[1]) / int(s[0])))
        sum.append((int(int(f[1]) * int(s[1]))))
        return print('Cумма дробей:', sum[0] / sum[1])
    else:
        sum.append(int(int(f[0])+int(s[0])))
        sum.append(int(f[1]))
        return print('Cумма дробей:', sum[0] / sum[1])


def fractionmult(first, second):
    f = first.split("/")
    s = second.split("/")
    mult = []
    mult.append(int(f[0]) * int(s[0]))
    mult.append(int(f[1]) * int(s[1]))
    return print('Произведение дробей:', mult[0] / mult[1])


a = first
b = second
fractionsum(a, b)
fractionmult(a, b)
