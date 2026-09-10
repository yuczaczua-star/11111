import math


while True:
    try:
        x = float(input("Введите число x: "))

        if x < math.sqrt(2):
            print("Ошибка! При x < корень 2 подкоренные выражения отрицательны.")
            print("Введите x >= 1.4142")
            continue

        if math.tan(math.sqrt(x)) == 0:
            print("Ошибка! Деление на ноль: tg(корень 0x) = 0. Введите другое x")
            continue

        y = -(math.sqrt(x**2 - 2) * 4 * x) / (2 * math.pi * math.tan(math.sqrt(x))) * math.e ** math.pi
        print("y =", y)

        if y > 0:
            print("Значение положительное")
        elif y < 0:
            print("Значение отрицательное")
        else:
            print("Значение равно нулю")

        if y == int(y):
            if int(y) % 2 == 0:
                print("Значение четное")
            else:
                print("Значение нечетное")
        else:
            print("Значение не целое - четность определить нельзя")

        break

    except ValueError:
        print("Ошибка! Введено не число")