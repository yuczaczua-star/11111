
print("Двузначные числа, сумма цифр которых равна 10:")
for number in range(10, 100):
    first = number // 10
    second = number % 10
    if first + second == 10:
        print(number)
