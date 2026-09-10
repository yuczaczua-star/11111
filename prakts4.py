print("Программа возведения чисел в квадрат.")
print("Введите 0, чтобы завершить работу.\n")

while True:
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Ошибка! Нужно ввести целое число.")
        continue

    if number == 0:
        print("Введен ноль. Программа завершена.")
        break

    result = number ** 2
    print(f"Квадрат числа {number} равен {result}\n")