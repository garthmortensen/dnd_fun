# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 19:56:34 2022

@author: garth

OOP demo
"""


class Game(object):
    def __init__(self, title, genre, price=0, playtime=0, rating=0):
        self.title = title
        self.genre = genre
        self.price = price
        self.playtime = playtime
        self.rating = rating

    def play_game(self, hours: int):
        """Adds to game's total playtime"""
        self.playtime += hours
        print(f"You are played {self.title} for {hours} more hours.")

    def rate_game(self, rating: int):
        """Give game a rating"""
        self.rating = rating
        print(f"You rated {self.title} as a {rating}/5")


class Library(object):
    def __init__(self):
        self.games = []

    def buy_games(self, *args: str):
        """Purchase game, adding it to library"""
        self.games += args

    def library_value(self):
        """Calculate value of all games in library"""
        value = sum([game.price for game in lib.games])
        print(f"The value of your library is: {value}")
        return value


# create some game objects
g1 = Game(title="Dying Light 2", genre="FPS", price=50, playtime=60, rating=4)
g2 = Game("Stardew Valley", "sim", 10, 20, 5)
g3 = Game("The Last Stand", "survial", 25, 10, 3)

# run some game methods
g1.play_game(30)
g1.rate_game(3)

# create and fill a library
lib = Library()
lib.buy_games(g1, g2, g3)
value = lib.library_value()
