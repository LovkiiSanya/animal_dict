import random


class Animal:
    def __init__(self, color, place):
        self.id = random.randint(1, 1000000)
        self.color = color
        self.place = place
