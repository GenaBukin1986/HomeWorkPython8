# Задача 38: Дополнить телефонный справочник возможностью изменения
# и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

import os
import time
from test_file import redactor_telephone_book
from delete_data import delete_abonent_telephone_book

def clear():
    os.system('cls')

def print_telephone_book(file_name = "text_file.txt"):
    with open(file_name,'r') as file:
        print("Режим чтения телефонной книги\n")
        count = 1
        for line in file:
            print(f'{count}. {line}',end="")
            count += 1
    print("\n")
    input("Нажмите Enter для перехода в меню ")
    menu_telephone_book()        
    
def add_telephone_book(file_name = "text_file.txt"):
    with open(file_name,"a") as file:
        file.write('\n')
        print("Режим добаления в телефонную книгу")
        famaly = input("Введите фамилию: ")
        name = input("Введите имя: ")
        telephone = input("Введите номер телефона: ")
        info = famaly + " " + name + " " + telephone
        file.write(info)
        print("Абонент успешно добавлен в телефонную книгу")
        
    menu_telephone_book()
        
def find_telephone_book(file_name = "text_file.txt"):
    with open(file_name,"r") as file:
        
        fake = input("""
              Введите цифру по какому параметру найти абонента
              1. Фамилия
              2. Имя
              3. Номер телефона
              4. Выход из поиска
              Введите цифру: """) 
        if fake == "4":
            return menu_telephone_book()
        while fake != '1' and fake != '2' and fake != '3' and  fake != '4':
            clear()
            print("\tВы ввели некорректные данные!")
            print("\tПопробуйте еще раз")
            fake = input("""
              Введите цифру по какому параметру найти абонента
              1. Фамилия
              2. Имя
              3. Номер телефона
              4. Выход из поиска
              Введите цифру: """)  
        if fake == "4":
            return
        if fake == "1":
            info = input("Введите фамилию, которую хотете найти: ")
        elif fake == "2":
            info = input("Введите имя, которое хотели найти: ")
        else:
            info = input("Введит номер телефона, по которому хотели найти абонента: ")
        for line in file:
            if info.lower() in line.lower():
                print(line,end="")
        time.sleep(2)        
    menu_telephone_book()

# def redactor_telephone_book(file_name = "text_file.txt"):
#     pass

# def delete_abonent_telephone_book(file_name = "text_file.txt"):
#     pass
                
def menu_telephone_book(file_name = "text_file.txt"):
    time.sleep(2)
    clear()
    text_menu = """
          Телефонная книга 1.0
          
          Меню:
          1. Вывод всех абонентов телефонной книги
          2. Добавление абонента в телефонную книгу
          3. Поиск абонента в телефонной книге
          4. Редактировать данные абонента
          5. Удалить абонента из телефонной книги
          6. Выход из телефонной книги
          """
    print(text_menu)
    value = input("\tВведите номер пункта меню: ")
    while value != "1" and value != "2" and value != "3" and value != "4" and value != "5" and value != "6":
        clear()
        print("Вы ввели некорректные данные")
        print("Попробуйте еще раз")
        print(text_menu)
        value = input("Введите номер пункта меню: ")
    clear()
    if value == "6":
        return
    if value == "1":
        print_telephone_book()
    elif value == "2":
        add_telephone_book()        
    elif value == "3":
        find_telephone_book()
    elif value == "4":
        redactor_telephone_book()
        menu_telephone_book()
    elif value == "5":
        
        delete_abonent_telephone_book()
        menu_telephone_book()

if __name__ == "__main__":
    menu_telephone_book()