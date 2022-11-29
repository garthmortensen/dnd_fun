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

    @staticmethod
    def move(distance):
        print(f"I move {distance}")

    def drop_items(self):
        pass

    def __repr__(self):
        return f"Species: {self.species}, name: {self.name}, size: {self.size}."


class Hero(object):
    def __init__(self, species, name, size, hp, gold, hit_dice, skill):
        self.hp = hp
        self.gold = gold
        self.hit_dice = hit_dice
        self.skill = skill
        # build the hero class using character
        # part of a hero is character data and operations
        # @!!!: hero has a species. Hero has a name. Hero has a size!
        # @!!!: hero has an ability to move and drop_items!
        self.character = Character(species, name, size)

    # this is an `interface` to expose functionality of the embedded object
    def move(self):
        self.character.move()  # hero.move invokes character.move()
        # UML for Java Programmers for definition of composition, aggregation, etc
        # pg 32

    def tell_skill(self):
        print(f"Ny skill is {self.skill}.")


class Monster(object):
    def __init__(self, species, name, size, hp, gold, hit_dice):
        self.hp = hp
        self.gold = gold
        self.hit_dice = hit_dice
        self.character = Character(species, name, size)  # composition

    @staticmethod
    def roar():
        print("ROOOAAAARRR!")


class NPC(object):
    def __init__(self, species, name, size, hp, gold):
        self.hp = hp
        self.gold = gold
        self.character = Character(species, name, size)  # composition

    @staticmethod
    def trade():
        print("Let's make a trade. Here are my wares.")


if __name__ == '__main__':
    # create some characters
    drizzt = Hero("dark elf", "Drizzt", "medium", 100, 1000, 18, "panther attack")
    elminster = Hero("Human", "Elminster", "medium", 30, 50, 30, "Fireball")
    kobold = Monster("Kobold", "Cabbage Beak", "small", 15, 5, 5)
    flying_sword = Monster("Flying Sword", "Sharpie", "small", 10, 10, 0)
    griswold = NPC("Human", "Griswold the Blacksmith", "medium", 50, 1000)

