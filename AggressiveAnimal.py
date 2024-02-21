from Animal import Animal


def init_aggressive_animal():
    animalcolor = input("Введите цвет животного: ")
    animalplace = input("Введите место обитания животного: ")
    animalfang = input("Введите длинну клыков в см: ")
    animal = AggressiveAnimal(
        animalcolor, animalplace, animalfang
    )
    return animal


class AggressiveAnimal(Animal):  # дочка с особенностью клыка
    def change_info(self):
        animalcolor = input("Введите цвет животного: ")
        animalplace = input("Введите место обитания животного: ")
        animalfang = input("Введите длинну клыков в см: ")
        self.color = animalcolor
        self.place = animalplace
        self.fang = animalfang

    def __init__(self, color, place, fang):
        super().__init__(color, place)
        self.fang = fang

    def __repr__(self):
        animal = type(self).__name__
        return f"{animal}({self.id!r},{self.color!r},{self.place!r},{self.fang!r})"

    def __str__(self):
        return f"Ваш ID: {self.id} Цвет: {self.color} Место обитания: {self.place} Длинна клыков: {self.fang}"
