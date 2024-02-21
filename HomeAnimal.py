from Animal import Animal


def init_home_animal():
    animalcolor = input("Введите цвет животного: ")
    animalplace = input("Введите место обитания животного: ")
    animalname = input("Введите кличку животного: ")
    typehomeanimal = HomeAnimal(animalcolor, animalplace, animalname)
    return typehomeanimal


class HomeAnimal(Animal):  # дочка с особенностью клички
    def change_info(self):
        animalcolor = input("Введите цвет животного: ")
        animalplace = input("Введите место обитания животного: ")
        animalname = input("Введите кличку животного: ")
        self.color = animalcolor
        self.place = animalplace
        self.name = animalname

    def __init__(self, color, place, name):
        super().__init__(color, place)
        self.name = name

    def __repr__(self):
        animal = type(self).__name__
        return f"{animal}({self.id!r},{self.color!r},{self.place!r},{self.name!r})"

    def __str__(self):
        return f"Ваш ID: {self.id} Цвет: {self.color} Место обитания: {self.place} Кличка: {self.name}"
