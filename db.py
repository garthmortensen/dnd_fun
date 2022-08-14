# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:19:33 2022

@author: garth
"""


from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect
from sqlalchemy import Table, Column, Integer, DateTime
from sqlalchemy import select, insert, update, delete
from sqlalchemy import func  # agg calcs, count, sum, min
import random  # for dice rolling


def setup_db(in_memory: bool=True):
    """CREATE DATABASE function.
        Input: Set boolean to determine if db should be in_memory (default),
        or sqlite.
        Output: engine, metadata
    """

    if in_memory:
        engine = create_engine('sqlite:///:memory:')  # better for git, dev
    else:
        engine = create_engine('sqlite:///db.sqlite')  # approach 1 //// for abs path
    
    # Create a metadata object
    metadata = MetaData()

    return engine, metadata


def setup_tables(engine, metadata):
    """CREATE TABLE function.
        Input: Provide engine and metadata
        Output: Returns engine, metadata and table
    """

    # Build a census table
    rolls = Table('rolls', metadata,
                   # pk autoincrement so you can skip assigning pk value in insert
                   Column('id', 
                          Integer(), 
                          primary_key=True, 
                          autoincrement=True),
                   Column('roll_value', 
                          Integer(), 
                          nullable=False),
                   Column('timestamp_created', 
                          DateTime(timezone=True),
                          # leave timestamp to db to calc, else latency issues
                          server_default=func.now(),
                          # anytime row updates, inserts new timestamp
                          onupdate=func.now()
                          ))
    
    # Create the table in the database
    # metadata.create_all(engine)  # method 1
    rolls.create(engine)  # method 2
    
    insp = inspect(engine)
    print(insp.get_table_names())

    return engine, metadata, rolls


def insert_rows(engine, tablename):
    """INSERT INTO function. 
        Input: engine, tablename
        Output: None
    """

    roll_value = random.randint(1, 100)
    data = [
              {'roll_value': roll_value}
            , {'roll_value': roll_value}
            ]
    
    insert_statement = insert(tablename)
    # Use values_list to insert data
    results = engine.execute(insert_statement, data)
    print(results.rowcount)  # row count


def update_rows(engine, tablename):
    """UPDATE function. 
        Input: engine, tablename
        Output: None
    """

    update_statement = update(tablename).values(roll_value='99')
    update_statement = update_statement.where(tablename.columns.id == 1)
    # results = engine.execute(update_statement)


def select_rows(engine, tablename):
    """SELECT function. 
        Input: engine, tablename
        Output: None
    """

    select_statement = select([tablename])
    results = engine.execute(select_statement).fetchmany(size=100)
    print(select_statement)
    print(results)


def count_rows(engine, tablename) -> int:
    """SELECT count(*) function. Executes on database side, instead of len()
        Input: engine, tablename
        Output: row_count int
    """

    count_statement = func.count(rolls.columns.id)
    row_count = engine.execute(count_statement).scalar()
    print(row_count)

    return row_count


def delete_rows_all(engine, tablename):
    """DELETE FROM function.
        Input: engine, tablename
        Output: None
    """

    delete_statement = delete(rolls)
    print(delete_statement)
    # results = engine.execute(delete_statement)
    print(engine.execute(select([tablename])).fetchall())



engine, metadata = setup_db()

engine, metadata, rolls = setup_tables(engine, metadata)

insert_rows(engine, rolls)

update_rows(engine, rolls)

select_rows(engine, rolls)

row_count = count_rows(engine, rolls)

delete_rows_all(engine, rolls)

