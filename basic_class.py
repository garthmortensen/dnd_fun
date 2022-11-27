"""
@startuml
class Hero extends Character
class Monster extends Character
class NPC extends Character

class Weapon extends Item
class Armor extends Item
@enduml
"""

# Define the Character class
class Character(object):
    # constructor will be called whenever class is instantiated
    # all non-self params must be passed during instantiation
    def __init__(self, species, name, size):
        self.species = species
        self.name = name
        self.size = size
        print(f"species: {self.species}, name: {self.name}, size: {self.size}.")

    def laugh(self):
        print("Hahaha!")

    def move(self, distance):
        print(f"I move {distance}")

    def drop_items(self):
        pass

    def __repr__(self):
        return f"Species: {self.species}, name: {self.name}, size: {self.size}."

class Hero(Character):
    def __init__(self, species, name, size, hp, gold, hit_dice, skill):
        super().__init__(species, name, size)
        self.hp = hp
        self.gold = gold
        self.hit_dice = hit_dice
        self.skill = skill

    def tell_skill(self):
        print(f"Ny skill is {self.skill}.")

# what makes a monster a monster vs a hero, in the eyes of a programmer? Not alignment.
class Monster(Character):
    def __init__(self, species, name, size, hp, gold, hit_dice):
        super().__init__(species, name, size)
        self.hp = hp
        self.gold = gold
        self.hit_dice = hit_dice

    def roar(self):
        print("ROOOAAAARRR!")

class NPC(Character):
    def __init__(self, species, name, size, hp, gold):
        super().__init__(species, name, size)
        self.hp = hp
        self.gold = gold

    def trade(self):
        print("Let's make a trade. Here are my wares.")


if __name__ == '__main__':
    # create some characters
    drizzt = Hero("dark elf", "Drizzt", "medium", 100, 1000, 18, "panther attack")
    elminster = Hero("Human", "Elminster", "medium", 30, 50, 30, "Fireball")
    kobold = Monster("Kobold", "Cabbage Beak", "small", 15, 5, 5)
    flying_sword = Monster("Flying Sword", "Sharpie", "small", 10, 10, 0)
    griswold = NPC("Human", "Griswold the Blacksmith", "medium", 50, 1000)

