import os

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def add_shelf(directories):
    """ функция для создания нового шкафа """
    new_shelf = input("Введите номер шкафа, который мы будем создавать")
    if new_shelf in list(directories):
        print("Простите, но такой шкаф существует")
    else:
        directories[new_shelf] = []
        print(f"Шкаф с номером {new_shelf} создан")


def doc_move(directories):
    """ функция для переноса документов из шкафа в шкаф """
    while True:
        num_doc = input("Введите номер документа")

        if get_shelf_num(directories, num_doc, True):
            print("Такой документ есть")
            old_shelf = get_shelf_num(directories, num_doc, True)
            break
        else:
            print("Такого документа нет")

    while True:
        num_shelf = input("Введите номер шкафа куда перенести")
        if num_shelf in list(directories):
            print("Такой шкаф есть")
            break
        else:
            print("Такого шкафа нет")
    directories[old_shelf].remove(num_doc)
    directories[num_shelf].append(num_doc)


def doc_delete(documents, directories):
    """ функция для полного удаления документа из программы """

    while True:
        num = input("Введите номер документа для удаления")
        for i, id in enumerate(documents):
            if id["number"] == num:
                print(f'{id["type"]} "{id["number"]}" "{id["name"]}" удален')
                documents.pop(i)
                print(f'документ удален из шкафа {get_shelf_num(directories, num, True)}')
                directories[get_shelf_num(directories, num, True)].remove(num)
                return
        print("Такого документа нету, попробуйте еще раз")


def clear_scren():
    """ функция для очиски экрана консоли """
    os.system('cls||clear')
    welcome_print(True)


def welcome_print(help=False):
    """
    функция для вывода приветствия и(или) справки
    если не передать значение то приветствие будет выведено
    """
    if not help:
        print("Добро пожаловать!")
    print("Список моих возможностей:")
    print("1 - найти человека по номеру документа")
    print("2 - выводит номер шкафа, в котором лежит документ")
    print("3 - вывод всех документов, содержащихся в каталоге")
    print("4 - добавление документа")
    print("5 - удаление документа")
    print("6 - перенос документа из шкафа в шкаф")
    print("7 - создание нового шкафа")
    print("help - вызов справки моих возможностей")
    print("clear - очистка окна вывода")
    print("exit - выход из программы")


def doc_add(documents, directories):
    """ функция для добавления нового документа """
    type = input("Введирте тип документа")
    number = input("Введирте номер документа")
    name = input("Введирте своё имя")
    documents.append({"type": type, "number": number, "name": name})
    while True:
        shelf = input("Введирте номер шкафа, для сохранения")
        if shelf in directories:
            break
        else:
            print("Такого шкафа нет, уточните куда положить документ")
    directories[shelf].append(number)
    print(f"Документ добавлен в шкаф {shelf}")


def get_shelf_num(directories, input_num="", ret=False):
    """ функция для получения номера шкафа
     input_num служит для того, чтобы передать в функцию номер документа сразу
     ret служит для того, чтобы вернуть значение, если это необходимо, если не проставить это значение вернется None
     """
    if not input_num:
        doc_num = input("Введите номер документа:")
    else:
        doc_num = input_num
    for i in directories:
        if doc_num in directories[i] and not ret:
            print(f"Документ находится в шкафу {i}")
        elif doc_num in directories[i] and ret:
            return i


def doc_list(documents):
    """ Функция возвращает полный список документов"""
    for i in documents:
        print(f'{i["type"]} "{i["number"]}" "{i["name"]}"')


def get_person_by_doc_num(documents):
    """команда, которая спросит номер документа
    и выведет имя человека, которому он принадлежит"""

    doc_num = input("Введите номер документа:")
    for i, id in enumerate(documents):
        if doc_num == id["number"]:
            print(id["name"])
            print()
            return
    print("Человека с таким номером документа не существует")
    print()


comand_list = {
    "1": get_person_by_doc_num,
    "2": get_shelf_num,
    "3": doc_list,
    "4": doc_add,
    "5": doc_delete,
    "6": doc_move,
    "7": add_shelf,
    "Clear": clear_scren,
    "Help": welcome_print
}


def comand_check(documents, directories):
    while True:
        comand = input("Введите команду:")
        # if comand == "1":+++
        #     get_person_by_doc_num(documents)
        # elif comand == "2":+++
        #     get_shelf_num(directories)
        # elif comand == "3":+++
        #     doc_list(documents)
        # elif comand == "4":+++
        #     doc_add(documents, directories)
        # elif comand == "5":+++
        #     doc_delete(documents, directories)
        # elif comand == "6":+++
        #     doc_move(directories)
        # elif comand == "7":+++
        #     add_shelf(directories)
        # elif comand.capitalize() == "Clear":+++
        #     clear_scren()
        # elif comand.capitalize() == "Help":+++
        #     welcome_print(True)
        # elif comand.capitalize() == "Exit":+++
        #     return
        # else:
        #     print("Не знаю такую команду =(")
        if comand.capitalize() in ["Clear"]:
            comand_list[comand.capitalize()]()
        elif comand.capitalize() in ["Help"]:
            comand_list[comand.capitalize()](True)
        elif comand in ["1", "3"]:
            comand_list[comand](documents)
        elif comand in ["2", "6", "7"]:
            comand_list[comand](directories)
        elif comand in ["4", "5"]:
            comand_list[comand](documents, directories)
        elif comand.capitalize() in ["Exit"]:
            return
        else:
            print("Не знаю такую команду =(")


def main(documents, directories):
    welcome_print()
    comand_check(documents, directories)
    print("До свидания!")


main(documents, directories)
