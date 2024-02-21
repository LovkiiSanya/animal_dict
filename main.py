from AggressiveAnimal import *
from FriendlyAnimal import *
from HomeAnimal import *

animal_dict = {}


def create_animal():
    animal_type = int(
        input(
            "Отлично! Какого типа ваше животное ? Домашнее (1), Дружелюбное (2), Хищное (3)"
        )
    )
    if animal_type == 1:
        animal = init_home_animal()
    elif animal_type == 2:
        animal = init_friendly_animal()
    else:
        animal = init_aggressive_animal()
    animal_dict[animal.id] = animal
    print(animal)


def get_animals():
    get_animal_option = int(
        input("будем смотреть всех животных (1) или по конкретному номеру id (2)?")
    )
    if get_animal_option == 1:
        print(animal_dict)
    if get_animal_option == 2:
        animal_id = int(input("Введите номер животного (id)"))
        if is_animal_exist(animal_id):
            print(animal_dict.get(animal_id))
        else:
            print("Такого id нет в базе!")


def delete_animal():
    animal_id = int(input("Отлично, введите номер ID который удаляем:"))
    if is_animal_exist(animal_id):
        animal_dict.pop(animal_id)
        print("Готово!")
    else:
        print("Такого id нет в базе!")


def is_animal_exist(animal_id):
    return animal_id in animal_dict.keys()


def update_animal():
    animal_id = int(input("По какому ID будем вносить изменения?:"))
    if is_animal_exist(animal_id):
        animal = animal_dict[animal_id]
        animal.change_info()


while True:
    kind_of_action = int(
        input(
            "Привет,какое действие выполняем? 1) посмотреть животных из справочника! 2) добавить животное в справочник! 3)удалить животное из справочника 4)изменить данные о животном\n"
        )
    )
    if kind_of_action == 1:
        get_animals()
    if kind_of_action == 2:
        create_animal()
    if kind_of_action == 3:
        delete_animal()
    if kind_of_action == 4:
        update_animal()
