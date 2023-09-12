import os

def clear():
    os.system('cls')

def delete_abonent_telephone_book(file_name = "text_file.txt"):
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
    
    num = int(input("Абонента под каким номером вы хотели бы удалить: "))
    clear()
    del lines[num - 1]
    print(f"Абонемент успешно удален!")
    
    with open(file_name,"a") as file:
        file.write("".join(lines))
#     # menu_telephone_book()
        
def print_telephone_book(file_name = "text_file.txt"):
    with open(file_name,'r') as file:
        print("Режим чтения телефонной книги\n")
        count = 1
        for line in file:
            print(f'{count}. {line}',end="")
            count += 1
            
# if __name__ == "__main__":
#     delete_abonent_telephone_book()
#     print_telephone_book()