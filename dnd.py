# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:31:56 2022

@author: garth

make classes fun with dnd
"""
# %%

import random


class die(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))
        return random.randint(1, self.sides)


class cup_of_dice(object):
    def __init__(self):
        self.dice = []

    def add_dice(self, *add_dice):
        self.dice += add_dice

    def remove_dice(self, *del_dice):
        self.dice -= del_dice

    def roll_dice(self):
        for die in self.dice:
            die.roll_die()


cup = cup_of_dice()

cup.add_dice(die(4), die(6))

cup.roll_dice()

