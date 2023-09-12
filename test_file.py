import os
# from task38 import *

def clear():
    os.system('cls')

def redactor_telephone_book(file_name = "text_file.txt"):
    with open(file_name,"r") as file:
        clear()
        lines = file.readlines()
        count = 1
        for i in lines:
            print(f'{count}. {i}',end="")
            count += 1
        print("\n")
    file = open(file_name,"w")
    file.close()
    
    num = int(input("Абонента под каким номером вы хотели бы отредактировать: "))
    clear()
    data = lines[num - 1].split()
    data[2] = " ".join(data[2:])
    del data[3:]
    print(lines[num - 1])
    redac = input(f"""
                  Какие данные вы хотите отредактировать?
                  1. Фамилия: {data[0]}
                  2. Имя: {data[1]}
                  3. Номер: телефона {data[2]}
                  
                  Введите пункт редактирования: """)
    print()
    if redac == "1":
        data[0] = input("Введите фамилию: ")
    elif redac == "2":
        data[1] = input("Введите имя: ")
    elif redac == "3":
        data[2] = input("Введите номер телефона: ")
    print("Данные изменены и успешно записаны!")
    if num != len(lines):
        lines[num - 1] = " ".join(data) + "\n"
    else:
        lines[num - 1] = " ".join(data)
    with open(file_name,"a") as file:
        file.write("".join(lines))
    # menu_telephone_book()
        
# def print_telephone_book(file_name = "copy_text_file.txt"):
#     with open(file_name,'r') as file:
#         print("Режим чтения телефонной книги\n")
#         count = 1
#         for line in file:
#             print(f'{count}. {line}',end="")
#             count += 1
