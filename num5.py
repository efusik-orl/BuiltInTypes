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
    print("6. До свидания")
    choice = input("Выберите пункт меню: ")

    # выводим описание каждого изделия
    if choice == '1':
        for item, description in jewelry_store.items():
            print(item, "-", description[0])

    # выводим цену каждого изделия
    elif choice == '2':
        for item, info in jewelry_store.items():
            print(item, "-", info[1])

    # выводим количество каждого изделия
    elif choice == '3':
        for item, info in jewelry_store.items():
            print(item, "-", info[2])

    # выводим всю информацию о каждом изделии
    elif choice == '4':
        for item, info in jewelry_store.items():
            print(item, "-", info[0], "-", info[1], "-", info[2])

    # осуществляем покупку изделия
    elif choice == '5':
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            item_quantity = int(input("Введите количество: "))
            if item_quantity <= jewelry_store[item_name][2]:
                price = item_quantity * jewelry_store[item_name][1]
                jewelry_store[item_name][2] -= item_quantity
                print("Покупка совершена. Цена:", price)
                print("Осталось в магазине:", jewelry_store[item_name][2])
            else:
                print("Недостаточно товара.")
        elif item_name == 'n':
            break
        else:
            print("Такого изделия нет в магазине.")

    # завершаем работу программы
    elif choice == '6':
        break
    else:
        print("Некорректный выбор.")
