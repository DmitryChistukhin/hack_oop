import random


class Thing:
    Names = ['Магическое кольцо', 'Волшебный посох', 'Поющий кристалл', 
    'Огненный меч', 'Ледяной топор', 'Волшебный фонарь', 
    'Плащ вседозволенности', 'Лапти счастья', 'Копье благости', 
    'Щит разрушения', 'Матрас удачи', 'Белый капюшон', 'Черный платок', 
    'Кольчуга печали', 'Броня рокота', 'Шпага рассвета', 
    'Кинжал великолепия', 'Трусы семейные', 'Просто кирпич', 
    'Перчатки юности']
    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = float(random.randint(0, 10))
        self.defence = random.randint(1, 10) * 0.01
        self.health = random.randint(0, 100)

    def __str__(self):
        return f'Вы получили {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'


Things_list = []
things_count = random.randint(1, 100)
for i in range(1, things_count):
    Things_list.append(Thing())


class Person:
    Names = ['Егор', 'Вася', 'Петя', 'Тоша', 'Дима', 'Вова', 'Маша', 'Люся', 'Даша', 'Коля', 
    'Витя', 'Макс', 'Надя', 'Платон', 'Миша', 'Кеша', 'Настя', 'Лиля', 'Яна', 'Юра']

    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = random.randint(0, 30)
        self.defence = random.randint(1, 10) * 0.01
        self.health = random.randint(0, 15)
        self.things = []

    def setThings(self):
        n = random.randint(1, 4)
        for i in range (1, n+1):
            newthing = random.choice(Things_list)
            self.things.append(newthing(i))

    def updated_attack(self):
        updated_attack = self.attack + sum(
            Thing.attack for Thing in self.things)
        return updated_attack
    
    def updated_defence(self):
        updated_defence = self.defence + sum(
            Thing.defence for Thing in self.things)
        return updated_defence
    
    def updated_health(self):
        updated_health = self.health + sum(
            Thing.health for Thing in self.things)
        return updated_health
        
    def __str__(self):
        return f'Создан персонаж {self.name} с параметрами: атака = {self.updated_attack}, защита = {self.defence}, здоровье = {self.health}'

p1 = Person()
print(p1)


class Paladin(Person):
    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = random.randint(0, 30)
        self.defence = random.randint(1, 10) * 0.01 * 2
        self.health = random.randint(0, 15) * 2 
        self.things = []

    def __str__(self):
        return f'Паладин {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'


class Warrior(Person):
    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = random.randint(0, 30) * 2
        self.defence = random.randint(1, 10) * 0.01
        self.health = random.randint(0, 15)
        self.things = []

    def __str__(self):
        return f'Воин {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'

n=10
Paladin_list = []
for i in range(1, n+1):
    Paladin_list.append(Paladin())


Warrior_list = []
for i in range(1, n+1):
    Warrior_list.append(Warrior())

Fighters_list = []
Classes_list = Paladin_list + Warrior_list
for i in range(1, n+1):
    Fighter = random.choice(Classes_list)
    Fighters_list.append(Fighter)

while len(Fighters_list) > 1:
    attacker = random.choice(Fighters_list)
    defender = random.choice(Fighters_list)
    dh = defender.updated_health()
    aa = attacker.updated_attack()
    dd = defender.updated_defence()
    damage = aa - aa*dd
    hp_left = dh - damage
    print(f'{attacker.name} наносит удар по {defender.name} на {damage} урона')
    if hp_left <= 0:
        Fighters_list.remove(defender)
else:
    winner = random.choice(Fighters_list)
    print (f'победитель: {winner}')   
