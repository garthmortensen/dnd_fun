"""
carpal tunnel approach
DOES NOT WORK
"""

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String  # these modules can declare cols and dtypes
from sqlalchemy.orm import mapper
from sqlalchemy import Table

metadata = MetaData()

# define my table
character = Table(
    "Character",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("species", String(255)),
    Column("name", String(255)),
    Column("size", String(255)),
    Column('hero_info', String(255)),
    Column('monster_info', String(255)),
    Column('npc_info', String(255)),
    )


# Define the Character class
class Character(object):
    # constructor will be called whenever class is instantiated
    # all non-self params must be passed during instantiation
    def __init__(self, species, name, size):
        self.species = species
        self.name = name
        self.size = size
        print(f"species: {self.species}, name: {self.name}, size: {self.size}.")


class Hero(Character):
    def __init__(self, species, name, size, hp, gold, hit_dice, skill):
        super().__init__(species, name, size)
        self.hp = hp
        self.gold = gold
        self.hit_dice = hit_dice
        self.skill = skill


class Monster(Character):
    def __init__(self, species, name, size, hp, gold, hit_dice):
        super().__init__(species, name, size)
        self.hp = hp
        self.gold = gold
        self.hit_dice = hit_dice


class NPC(Character):
    def __init__(self, species, name, size, hp, gold):
        super().__init__(species, name, size)
        self.hp = hp
        self.gold = gold


# add Classical Mappings
mapper(Character, character,
       polymorphic_on=character.c.type,
       polymorphic_identity='character',
       exclude_properties={'hero_info', 'monster_info', 'npc_info'})

mapper(Hero,
       inherits=Character,
       polymorphic_on="hero",
       exclude_properties={'hero_info'})

mapper(Monster,
       inherits=Character,
       polymorphic_on="monster",
       exclude_properties={'monster_info'})

mapper(NPC,
       inherits=Character,
       polymorphic_on="npc",
       exclude_properties={'npc_info'})

if __name__ == '__main__':
    # create some characters
    drizzt = Hero("dark elf", "Drizzt", "medium", 100, 1000, 18, "panther attack")
    elminster = Hero("Human", "Elminster", "medium", 30, 50, 30, "Fireball")
    kobold = Monster("Kobold", "Cabbage Beak", "small", 15, 5, 5)
    flying_sword = Monster("Flying Sword", "Sharpie", "small", 10, 10, 0)
    griswold = NPC("Human", "Griswold the Blacksmith", "medium", 50, 1000)
