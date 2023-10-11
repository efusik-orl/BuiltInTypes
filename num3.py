lst = []

# запрашиваем количество элементов списка и проверяем, что введено число
while True:
    try:
        n = int(input("Введите количество элементов списка: "))
        break
    except ValueError:
        print("Вы ввели не число!")

# заполняем список элементами и проверяем, что введено число
for i in range(n):
    while True:
        try:
            element = int(input("Введите элемент списка: "))
            lst.append(element)
            break
        except ValueError:
            print("Вы ввели не число!")

# находим наибольший четный элемент списка
max_even = None
for element in lst:
    if element % 2 == 0:
        if max_even is None or element > max_even:
            max_even = element

# выводим результаты
if max_even is None:
    print("Наибольший четный элемент отсутствует")
    print("Первый элемент списка:", lst[0])
else:
    print("Наибольший четный элемент:", max_even)

# сортируем список по убыванию положительных чисел
lst.sort(reverse=True)

print("Список после преобразования:", lst)

