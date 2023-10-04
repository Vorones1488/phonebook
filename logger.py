def input_contact():
    with open('data.txt', 'a', encoding='UTF8') as f:
        user = input("введите имя, фамилию, телефон: ").strip().split()
        f.write(','.join(user) + '\n')

def print_contact():
    with open('data.txt', 'r', encoding='UTF8') as f:
        contacts = f.readlines()
        for contact in contacts:
            print(*contact.strip().split(','))


def find_contact():
    with open('data.txt', 'r', encoding='UTF8') as f:
        contacts = f.readlines()
        while True:
            choice = input("для поиска по имени нажмите - 0 " \
            'Для поиска по фамилии нажмите - 1 \n Для поска по номеру нажмите - 2 \n')
            if choice not in '012':
                print('Других данных нет!!!')
            else:
                choice = int(choice)
                if choice == 0:
                    name = "Введите имя: "
                elif choice == 1:
                    name = "Ведите фамилию: "
                elif choice == 2:
                    name = "Введите номер телефона: "
                break
        surnami = input(f'{name}')
        print("Найденные контакты: \n")
        for contact in contacts:
            ful_contact = contact.strip().split(',')
            if surnami.lower() == ful_contact[choice].lower():
                print(*ful_contact)


def change_contact():
    with open('data.txt', 'r+', encoding='UTF8') as f:
        contacts = f.readlines()
        while True:
            choice = input("для поиска по имени нажмите - 0 " \
            'Для поиска по фамилии нажмите - 1 \n Для поска по номеру нажмите - 2 \n')
            if choice not in '012':
                print('Других данных нет!!!')
            else:
                choice = int(choice)
                if choice == 0:
                    name = "Введите имя: "
                elif choice == 1:
                    name = "Ведите фамилию: "
                elif choice == 2:
                    name = "Введите номер телефона: "
                break
        surnami = input(f'{name}')
        id = 0
        count = 0
        print("Найденные контакты: \n")
        print('id   Контакт')
        for contact in contacts:
            ful_contact = contact.strip().split(',')
            if surnami.lower() == ful_contact[choice].lower():
                print(id + 1, *ful_contact)
                count += 1
            id =+ 1
        if not count == 0:
            id_inp = int(input("Введите id редактируемого контакта: ")) -1
            new_text = input("Введите, имя, фамилию, номер телефона с изменениями:  ").strip().split()
            contacts[id_inp ] = ','.join(new_text) + '\n'
            f.seek(0)
            f.writelines(contacts) 
        else:
            print("Контакт не найден")


def delete_contacts():
    with open('data.txt', 'r+', encoding='UTF8') as f:
        contacts = f.readlines()
        id = 0
        for contact in contacts:
             print((id + 1), *contact.strip().split(','))
             id += 1
        del_lines = int(input("Введите номер строки для удаления: ")) - 1
        with open('data.txt', 'w', encoding='UTF8') as f:
            del_txt = contacts[del_lines].strip()
            for contact in contacts:
                if contact.strip() != del_txt:
                    f.write(contact)
            print("Строка успешно удалена")
       
        



