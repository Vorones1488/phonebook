from logger import input_contact, print_contact, find_contact, change_contact, delete_contacts
def meny():
    text = '''
    Галвное меню:
Введите 1 для записи;
Введите 2 для вывода всего справочника;
Введите 3 для поиска контакта;
Введите 4 для редактирования контакта;
Введите 5 для удаления;
Вывод меню 9;
Введите 0 для завершения
        '''
    print(text)
    while True:
        
        command = int(input("Введите команду:  "))
        if command == 1:
            input_contact()
        if command == 2:
            print_contact()
        if command == 3:
            find_contact() 
        if command == 4:
            change_contact()
        if command == 5:
            delete_contacts()       
        if command == 9:
            meny()
        if command == 0:
            break


if __name__ == '__main__':
    meny()