import random


class Animal:  # Основной класс
    def __init__(self, id, color, place):
        self.id = id
        self.color = color
        self.place = place


class HomeAnimal(Animal):  # дочка с особенностью клички
    def __init__(self, id, color, place, name):
        super().__init__(id, color, place)
        self.name = name


class FriendlyAnimal(Animal):  # дочка с особенностью хвоста
    def __init__(self, id, color, place, tail):
        super().__init__(id, color, place)
        self.tail = tail


class AgressiveAnimal(Animal):  # дочка с особенностью клыка
    def __init__(self, id, color, place, fang):
        super().__init__(id, color, place)
        self.fang = fang


def rndnumb():
    numb = random.randint(1, 1000000)
    return numb


animal_dict = {1: "кобан"}

while True:

    kindofaction = int(
        input(
            "Привет,какое действие выполняем? 1) посмотреть животных из справочника! 2) добавить животное в справочник! 3)удалить животное из справочника 4)изменить данные о животном"
            "\n"
        )
    )
    if kindofaction == 1:
        lookanimal = int(
            input("будем смотреть всех животных(1) или по конкретному номеру id(2)?")
        )
        if lookanimal == 1:
            print(animal_dict)
        if lookanimal == 2:
            animalId = int(input("Введите номер животного(id)"))
            if animalId in animal_dict:
                print(animal_dict.get(animalId))
            else:
                print("Такого id нет в базе!")
    if kindofaction == 2:
        addAnimal = int(
            input(
                "Отлично!какого типа ваше животное ? Домашнее(1),Дружелюбное(2),Хищное(3)"
            )
        )
        if addAnimal == 1:
            animalID = rndnumb()
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animalname = input("Введите кличку животного: ")
            typehomeanimal = HomeAnimal(animalID, animalcolor, animalplace, animalname)
            animal_dict[animalID] = typehomeanimal
            print(animal_dict[animalID])
            print(
                "Ваш ID:",
                typehomeanimal.id,
                typehomeanimal.color,
                typehomeanimal.place,
                typehomeanimal.name,
            )
        if addAnimal == 2:
            animalID = rndnumb()
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animaltail = input("Введите длинну хвоста в см: ")
            typefriendlyanimal = FriendlyAnimal(
                animalID, animalcolor, animalplace, animaltail
            )
            animal_dict[animalID] = typefriendlyanimal
            print(animal_dict[animalID])
            print(
                "Ваш ID:",
                typefriendlyanimal.id,
                typefriendlyanimal.color,
                typefriendlyanimal.place,
                typefriendlyanimal.tail,
            )

        if addAnimal == 3:
            animalID = rndnumb()
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animalfang = input("Введите длинну клыков в см: ")
            typeagressiveanimal = AgressiveAnimal(
                animalID, animalcolor, animalplace, animalfang
            )
            animal_dict[animalID] = typeagressiveanimal
            print(animal_dict[animalID])
            print(
                "Ваш ID:",
                typeagressiveanimal.id,
                typeagressiveanimal.color,
                typeagressiveanimal.place,
                typeagressiveanimal.fang,
            )

    if kindofaction == 3:
        infodel = int(input("Отлично,введите номер ID который удаляем: "))
        animal_dict.pop(infodel)
        print("Готово!")

    if kindofaction == 4:
        changeanimal = int(input("По какому ID будем вносить изменения?: "))
        if type(animal_dict[changeanimal]) == HomeAnimal:
            animalID = changeanimal
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animalname = input("Введите кличку животного: ")
            typehomeanimal = HomeAnimal(
                changeanimal, animalcolor, animalplace, animalname
            )
            animal_dict[changeanimal] = typehomeanimal

        if type(animal_dict[changeanimal]) == FriendlyAnimal:
            animalID = changeanimal
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animaltail = input("Введите длинну хвоста в см: ")
            typefriendlyanimal = FriendlyAnimal(
                changeanimal, animalcolor, animalplace, animaltail
            )
            animal_dict[changeanimal] = typefriendlyanimal

        if type(animal_dict[changeanimal]) == AgressiveAnimal:
            animalID = changeanimal
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animalfang = input("Введите длинну клыков в см: ")
            typeagressiveanimal = AgressiveAnimal(
                changeanimal, animalcolor, animalplace, animalfang
            )
            animal_dict[changeanimal] = typeagressiveanimal
