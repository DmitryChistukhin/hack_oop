class Thing:
    def __init__(self, name: str, attack: float, defence: float, health: float):
        self.name = name
        self.attack = attack
        self.defence = defence 
        self.health = health

    def __str__(self):
        return f'Вы получили {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'

class Person:
    def __init__(self, name: str, attack: float, defence: float, health: float):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health

    #def setThings(self, newthing: Thing):
        #self.setThings.append(newthing)

    def __str__(self):
        return f'Создан персонаж {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'


class Paladin(Person):
    def __init__(self, name: str, attack: float, defence: float, health: float):
        super().__init__(name, attack, defence, health)
        self.defence = defence * 2
        self.health = health * 2 

    def __str__(self):
        return f'Создан паладин {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'


class Warrior(Person):
    def __init__(self, name: str, attack: float, defence: float, health: float):
        super().__init__(name, attack, defence, health)
        self.attack = attack * 2

    def __str__(self):
        return f'Создан воин {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'

#создаем произвольное количество, % защиты не более 10%, сортировка по %защиты, по возрастанию
#создаем произвольно 10 персов с рандомными именами из списка 20 имен
#одеваем персонажей вещами, не более 4-х на руку
