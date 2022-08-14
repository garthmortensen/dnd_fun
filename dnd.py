# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:31:56 2022

@author: garth

make classes fun with dnd
"""
# %%

import random
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect
from sqlalchemy import Table, Column, Integer
from sqlalchemy import select, insert, update, delete

# engine = create_engine('sqlite:///db.sqlite')  # approach 1 //// for abs path
engine = create_engine('sqlite:///:memory:')  # approach 2

# Create a metadata object
metadata = MetaData()

# Build a census table
rolls = Table('rolls', metadata,
               Column('id', Integer(), primary_key=True),
               Column('roll_value', Integer(), nullable=False))

# Create the table in the database
# metadata.create_all(engine)  # method 1
rolls.create(engine)  # method 2

insp = inspect(engine)
print(insp.get_table_names())

# %%

# insert data
data = [
          {'id': 0, 'roll_value': 6}
        , {'id': 1, 'roll_value': 3}
        ]

insert_statement = insert(rolls)
# Use values_list to insert data: results
results = engine.execute(insert_statement, data)
print(results.rowcount)

# %%

# update
update_statement = update(rolls).values(roll_value='99')
update_statement = update_statement.where(rolls.columns.id == 1)
results = engine.execute(update_statement)

# %%

# select *
select_statement = select([rolls])
results = engine.execute(select_statement).fetchmany(size=100)
print(select_statement)
print(results)

# %%

# delete *
delete_statement = delete(rolls)
print(delete_statement)
results = engine.execute(delete_statement)

# select *
print(engine.execute(select_statement).fetchall())


# %%

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

# %%

cup = cup_of_dice()
cup.add_dice(die(4), die(6))

# %%

cup.roll_dice()

