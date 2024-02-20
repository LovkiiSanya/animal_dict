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

    def askinfo():
        animalID = rndnumb()
        animalcolor = input("Введите цвет животного: ")
        animalplace = input("Введите место обитания животного: ")
        animalname = input("Введите кличку животного: ")
        typehomeanimal = HomeAnimal(animalID, animalcolor, animalplace, animalname)
        animal_dict[animalID] = typehomeanimal
        return print(
            "Ваш ID:",
            typehomeanimal.id,
            typehomeanimal.color,
            typehomeanimal.place,
            typehomeanimal.name,
        )

    def changeinfo(animalID):
        if type(animal_dict[changeanimal]) == HomeAnimal:
            animalID = changeanimal
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animalname = input("Введите кличку животного: ")
            typehomeanimal = HomeAnimal(
                changeanimal, animalcolor, animalplace, animalname
            )
            animal_dict[changeanimal] = typehomeanimal

    def __repr__(self):
        HomeAnimal = type(self).__name__
        return f"{HomeAnimal}({self.id!r},{self.color!r},{self.place!r},{self.name!r})"

    def __str__(self):
        return f"Ваш ID: {self.id} Цвет: {self.color} Место обитания: {self.place} Кличка: {self.name}"


class FriendlyAnimal(Animal):  # дочка с особенностью хвоста
    def __init__(self, id, color, place, tail):
        super().__init__(id, color, place)
        self.tail = tail

    def askinfo():
        animalID = rndnumb()
        animalcolor = input("Введите цвет животного: ")
        animalplace = input("Введите место обитания животного: ")
        animaltail = input("Введите длинну хвоста в см: ")
        typefriendlyanimal = FriendlyAnimal(
            animalID, animalcolor, animalplace, animaltail
        )
        animal_dict[animalID] = typefriendlyanimal
        return print(
            "Ваш ID:",
            typefriendlyanimal.id,
            typefriendlyanimal.color,
            typefriendlyanimal.place,
            typefriendlyanimal.tail,
        )

    def changeinfo(animalID):
        if type(animal_dict[changeanimal]) == FriendlyAnimal:
            animalID = changeanimal
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animaltail = input("Введите длинну хвоста в см: ")
            typefriendlyanimal = FriendlyAnimal(
                changeanimal, animalcolor, animalplace, animaltail
            )
            animal_dict[changeanimal] = typefriendlyanimal

    def __repr__(self):
        FriendlyAnimal = type(self).__name__
        return (
            f"{FriendlyAnimal}({self.id!r},{self.color!r},{self.place!r},{self.tail!r})"
        )

    def __str__(self):
        return f"Ваш ID: {self.id} Цвет: {self.color} Место обитания: {self.place} Длинна хвоста: {self.tail}"


class AgressiveAnimal(Animal):  # дочка с особенностью клыка
    def __init__(self, id, color, place, fang):
        super().__init__(id, color, place)
        self.fang = fang

    def askinfo():
        animalID = rndnumb()
        animalcolor = input("Введите цвет животного: ")
        animalplace = input("Введите место обитания животного: ")
        animalfang = input("Введите длинну клыков в см: ")
        typeagressiveanimal = AgressiveAnimal(
            animalID, animalcolor, animalplace, animalfang
        )
        animal_dict[animalID] = typeagressiveanimal
        return print(
            "Ваш ID:",
            typeagressiveanimal.id,
            typeagressiveanimal.color,
            typeagressiveanimal.place,
            typeagressiveanimal.fang,
        )

    def changeinfo(animalID):
        if type(animal_dict[changeanimal]) == AgressiveAnimal:
            animalID = changeanimal
            animalcolor = input("Введите цвет животного: ")
            animalplace = input("Введите место обитания животного: ")
            animalfang = input("Введите длинну клыков в см: ")
            typeagressiveanimal = AgressiveAnimal(
                changeanimal, animalcolor, animalplace, animalfang
            )
            animal_dict[changeanimal] = typeagressiveanimal

    def __repr__(self):
        AgressiveAnimal = type(self).__name__
        return f"{AgressiveAnimal}({self.id!r},{self.color!r},{self.place!r},{self.fang!r})"

    def __str__(self):
        return f"Ваш ID: {self.id} Цвет: {self.color} Место обитания: {self.place} Длинна клыков: {self.fang}"


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
            HomeAnimal.askinfo()
        if addAnimal == 2:
            FriendlyAnimal.askinfo()
        if addAnimal == 3:
            AgressiveAnimal.askinfo()

    if kindofaction == 3:
        infodel = int(input("Отлично,введите номер ID который удаляем: "))
        animal_dict.pop(infodel)
        print("Готово!")

    if kindofaction == 4:
        changeanimal = int(input("По какому ID будем вносить изменения?: "))
        HomeAnimal.changeinfo(changeanimal)
        FriendlyAnimal.changeinfo(changeanimal)
        AgressiveAnimal.changeinfo(changeanimal)
