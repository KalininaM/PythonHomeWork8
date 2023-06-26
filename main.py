# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных
phone_book = {}

#Открытие файла и запись его в переменную
def open_file():
    phone_book.clear()
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'address': nc[3]}
    print('\nТелефонная книга успешно загружена!')

#Показать на экран данные
def show_contacts(book: dict[int,dict]):
    if book:
        print('\n' + '=' * 100)
        for i, cnt in book.items():
            print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("address"):<20}')
        print('=' * 100 + '\n')
    else:
        print('Телефонная книга пуста или файл не открыт')

#Добавление контакта в переменную
def add_contact():
    print('Введите данные нового контакта')
    uid = max(list(phone_book.keys())) + 1
    name = input("Введите имя контакта: ")
    phone = input("Введите телефон контакта: ")
    address = input("Введите адрес контакта: ")
    phone_book[uid] = {'name': name, 'phone': phone, 'address': address}

    print(f'\nКонтакт {name} успешно добавлен!')
    print('=' * 100 + '\n')

#Сохранение добавленного контакта
def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ":".join([str(i),contact.get('name'),contact.get('phone'),contact.get('address')])
        data.append(new)
    data = '\n'.join(data)
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write(data)
    print('\nТелефонная книга успешно сохранена!')    
    print('=' * 100 + '\n')

#Поиск контакта
def search(word: str) -> list[dict]:
    result ={}
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
    return result

#Удалить контакт
def remove():
    result = search()
    show_contacts(result)
    index  = int(input('Введите ID контакта, который удалить: '))
    del_cnt = phone_book.pop(index)
    print(f'\nКонтакт {del_cnt.get("name")} успешно удален!')
    print('=' * 100 + '\n')

#Изменить контакт
def change_contact():
    word = input('Введите искомый элемент: ')
    result = search(word)
    show_contacts(result)

    index = int(input('Введите индекс изменяемого контакта: '))
    change_menu = '''Изменить: 
        1. ФИО 
        2. Номер телефона
        3. Адрес
        4. Оставить без изменений'''
    print(change_menu)

    field = int(input("Введите номер действия: "))
    match field:
        case 1:
           change(index, 'name') 
        case 2:
            change(index, 'phone') 
        case 3:
            change(index, 'address') 
        case 4:
            print('Изменения отменены')
            
def change(index: int, field):
    new = input('Введите данные изменяемого контакта: ')
    old_name = phone_book[int(index)].get(field)
    phone_book[index][field] = new
    print(f' {old_name} успешно изменен на {new}')    

#Показать меню
def menu() -> int:
    main_menu = '''Главное меню
        1. Открыть файл
        2. Сохранить файл
        3. Показать все контакты
        4. Создать новый контакт
        5. Найти контакт
        6. Изменить контакт
        7. Удалить контакт
        8. Выход
        '''
    print(main_menu)
    while True:
        select = input("Введите номер действия: ")
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода, введите ЧИСЛО от 1 до 8')

open_file()  
while True:

    command = menu()
    match command:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            word = input('Введите искомый элемент: ')
            result = search(word)
            show_contacts(result)
        case 6:
            change_contact()
        case 7:
            remove()
        case 8:
            print("Всего доброго!")
            break