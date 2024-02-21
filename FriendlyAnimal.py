from Animal import Animal


def init_friendly_animal():
    animalcolor = input("Введите цвет животного: ")
    animalplace = input("Введите место обитания животного: ")
    animaltail = input("Введите длинну хвоста в см: ")
    typefriendlyanimal = FriendlyAnimal(animalcolor, animalplace, animaltail)
    return typefriendlyanimal


class FriendlyAnimal(Animal):  # дочка с особенностью хвоста
    def change_info(self):
        animalcolor = input("Введите цвет животного: ")
        animalplace = input("Введите место обитания животного: ")
        animaltail = input("Введите длинну хвоста в см: ")
        self.color = animalcolor
        self.place = animalplace
        self.tail = animaltail

    def __init__(self, color, place, tail):
        super().__init__(color, place)
        self.tail = tail

    def __repr__(self):
        animal = type(self).__name__
        return (
            f"{animal}({self.id!r},{self.color!r},{self.place!r},{self.tail!r})"
        )

    def __str__(self):
        return f"Ваш ID: {self.id} Цвет: {self.color} Место обитания: {self.place} Длинна хвоста: {self.tail}"
