number = 0

while True:
    try:
        number = int(input("Введите положительное число: "))
        if number <= 0:
            print("Число должно быть положительным!")
            continue
        break
    except ValueError:
        print("Вы ввели не число!")

print("Делители числа", number, ":")

for i in range(1, number+1):
    if number % i == 0:
        print(i)
