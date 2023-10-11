# создаем словарь с информацией о ювелирных изделиях
jewelry_store = {
    'Кольцо': ['Золото', 5000, 10],
    'Серьги': ['Серебро', 2000, 5],
    'Браслет': ['Золото', 8000, 3],
    'Подвеска': ['Золото', 3000, 7],
    'Цепочка': ['Серебро', 1500, 8]
}

# создаем бесконечный цикл для работы с меню
while True:
    print("Меню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        jewelry_name = input('\nВведите название украшения: ')
        if jewelry_name in jewelry_store:
            print(jewelry_store[jewelry_name][0])
        else:
            print('\nТакого украшения нет в магазине')

    elif choice == '2':
        jewelry_name = input('\nВведите название украшения: ')
        if jewelry_name in jewelry_store:
            print(jewelry_store[jewelry_name][1])
        else:
            print('\nТакого украшения нет в магазине')

    elif choice == '3':
        jewelry_name = input('\nВведите название украшения: ')
        if jewelry_name in jewelry_store:
            print(jewelry_store[jewelry_name][2])
        else:
            print('\nТакого украшения нет в магазине')

    elif choice == '4':
        print('\nИнформация о товарах в магазине:\n')
        for jewelry, info in jewelry_store.items():
            print(jewelry, info[0], info[1], info[2])

    elif choice == '5':
        jewelry_name = input('\nВведите название украшения: ')
        if jewelry_name in jewelry_store:

            while True:
                quantity = input("Введите количество товара: ")
                if quantity.isdigit():
                    quantity = int(quantity)
                    break
                else:
                    print("Вы ввели неверное значение")

            if quantity <= jewelry_store[jewelry_name][2]:
                total_price = quantity * jewelry_store[jewelry_name][1]
                print('\nС вас: ', total_price, 'рублей\nОплатить?\n\n1. Да\n 2. Нет')
                while True:
                    q = input("\n\nВведите свой вариант: ")
                    if q.isdigit():
                        q = int(q)
                        if q == 1:
                            print('\n\nПокупка совершена успешно')
                        elif q == 2:
                            print('\n\nПокупка была отменена')
                        break
                    else:
                        print("Вы ввели неверное значение")
            else:
                print('\nНедостаточно товара в магазине')
        else:
            print('\nТакого украшения нет в магазине')

    elif choice == '6':
        break

    else:
        print('\nТакой функции не существует =(')
