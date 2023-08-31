sum = 0
count = 0
third = 0.03
commision = 0.015
multiplicity = 50
low = 30
high = 600
while True:
    command = input("Введите действие: ")
    if command == "+":
        count += 1
        money = int(input("Введите сумму: "))
        if money % multiplicity == 0:
            sum += money
            print(sum)
        elif money % multiplicity == 0:
            sum += money
        else:
            print("сумма введена некорретно")
        if count % 3 == 0:
            sum -= sum * third
            print("комиссия - ", sum * third)
    if command == "-" and sum > multiplicity:
        count += 1
        money = int(input("Введите сумму: "))
        if money % multiplicity == 0:
            if money * commision < low:
                sum -= (money + low)
            elif money * commision > high:
                sum -= (money + high)

            else:
                sum -= (money + (money * commision))
            print(sum)
        else:
            print("сумма введена некорретно")
            if count % 3 == 0:
                sum -= sum * third
                print("комиссия - ", sum * third)
    if command == "e":
        print(sum)
        break
