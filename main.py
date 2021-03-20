import random


class Thing:            #Создаем полностью рандомную вещь в определенном диапазоне статов
    Names = ['Магическое кольцо', 'Волшебный посох', 'Поющий кристалл', 
    'Огненный меч', 'Ледяной топор', 'Волшебный фонарь', 
    'Плащ вседозволенности', 'Лапти счастья', 'Копье благости', 
    'Щит разрушения', 'Матрас удачи', 'Белый капюшон', 'Черный платок', 
    'Кольчуга печали', 'Броня рокота', 'Шпага рассвета', 
    'Кинжал великолепия', 'Трусы семейные', 'Просто кирпич', 
    'Перчатки юности']
    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = random.randint(0, 10)
        self.defence = random.randint(1, 10) * 0.01
        self.health = random.randint(0, 10)

    def __str__(self):
        return f'{self.name}: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'


Things_list = []   #генерим список предметов перед боем
things_count = random.randint(1, 40)
for i in range(1, things_count):
    Things_list.append(Thing())

Sorted_Things_list = sorted(Things_list, key=lambda x: x.defence) #создаем отсортированный список
 


class Person:    #создаем родительский класс для бойцов
    Names = ['Егор', 'Вася', 'Петя', 'Тоша', 'Дима', 'Вова', 'Маша', 'Люся', 'Даша', 'Коля', 
    'Витя', 'Макс', 'Надя', 'Платон', 'Миша', 'Кеша', 'Настя', 'Лиля', 'Яна', 'Юра']
    
    max_possible_attack = 30
    max_possible_defence = 10
    max_possible_health = 20

    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = random.randint(0, self.max_possible_attack)
        self.defence = random.randint(1, self.max_possible_defence) * 0.01
        self.health = random.randint(0, self.max_possible_health)
        self.things = []

    def setThings(self): #тут выбираем 4 случайных вещи из списка, созданного перед боем
        n = random.randint(1, 4)
        for i in range (1, n+1):
            newthing = random.choice(Sorted_Things_list)
            self.things.append(newthing(i))

    def updated_attack(self): #тут статы с учетом предметов
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

    def health_left(self, damage)
        self.damage = damage
        health_left = self.updated_health - self.attack_damage
        return health_left
        

    def __str__(self):
        return f'Создан персонаж {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'
                
        


class Paladin(Person):
    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = random.randint(0, self.max_possible_attack)
        self.defence = random.randint(1, self.max_possible_defence) * 0.01 * 2
        self.health = random.randint(0, self.max_possible_health) * 2 
        self.things = []

    def __str__(self):
        return f'Паладин {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'


class Warrior(Person):
    def __init__(self):
        self.name = random.choice(self.Names)
        self.attack = random.randint(0, self.max_possible_attack) * 2
        self.defence = random.randint(1, self.max_possible_defence) * 0.01
        self.health = random.randint(0, self.max_possible_health)
        self.things = []

    def __str__(self):
        return f'Воин {self.name} с параметрами: атака = {self.attack}, защита = {self.defence}, здоровье = {self.health}'


# тут пошла подготовка к бою, генерим список из 10 бойцов
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

# Пошел сам бой:
while len(Fighters_list) > 1:
    defender = random.choice(Fighters_list)
    attaker = random.choice(Fighters_list)
    aa = attacker.updated_attack()
    dd = defender.updated_defence()
    damage = aa - aa*dd
    hp_left = defender.health_left(damage) - damage
    print(f'{attacker.name} наносит удар по {defender.name} на {damage} урона')
    if hp_left <= 0:
        Fighters_list.remove(defender)
    else:
        defender.updated_health() =- hp_left
else:
    winner = random.choice(Fighters_list)
    print (f'победитель: {winner}')   
