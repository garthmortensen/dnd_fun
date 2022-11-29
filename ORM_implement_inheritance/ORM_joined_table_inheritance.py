"""
DOES NOT WORK
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # base is used to construct classes
from sqlalchemy import Column, Integer, String  # these modules can declare cols and dtypes
from sqlalchemy.orm import Session
from sqlalchemy import inspect  # used to explore existing db schema. no purpose here other than to experiment
from sqlalchemy import ForeignKey  # for joined table inheritance

Base = declarative_base()


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_type = Column(String(255), nullable=False)
    species = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    size = Column(String(255), nullable=False)
    # all the following columns were relocated to Base class, due to conflicting column names in subclasses
    # https://docs.sqlalchemy.org/en/20/orm/inheritance.html#resolving-column-conflicts
    # A tricky case comes up when two subclasses want to specify the same column
    hp = Column(Integer)
    gold = Column(Integer)
    hit_dice = Column(Integer)
    __mapper_args__ = {'polymorphic_on': 'character_type'}


class Hero(Character):
    __mapper_args__ = {'polymorphic_identity': 'hero'}
    __tablename__ = 'hero'
    id = Column(None, ForeignKey('character.id'), primary_key=True)
    skill = Column(String(255))


class Monster(Character):
    __mapper_args__ = {'polymorphic_identity': 'monster'}
    __tablename__ = 'monster'
    id = Column(None, ForeignKey('character.id'), primary_key=True)


class NPC(Character):
    __mapper_args__ = {'polymorphic_identity': 'npc'}
    __tablename__ = 'npc'
    id = Column(None, ForeignKey('character.id'), primary_key=True)

    @staticmethod
    def trade():
        print("Let's make a trade. Here are my wares.")


# create some characters
drizzt = Hero(species="dark elf", name="Drizzt", size="medium", hp=100, gold=1000, hit_dice=18, skill="panther attack")
elminster = Hero(species="Human", name="Elminster", size="medium", hp=30, gold=50, hit_dice=30, skill="Fireball")
kobold = Monster(species="Kobold", name="Cabbage Beak", size="small", hp=15, gold=5, hit_dice=5)
flying_sword = Monster(species="Flying Sword", name="Sharpie", size="small", hp=10, gold=10, hit_dice=0)
griswold = NPC(species="Human", name="Griswold the Blacksmith", size="medium", hp=50, gold=1000)

engine = create_engine("sqlite:///dnd.sqlite")  # echo=True
conn = engine.connect()
Base.metadata.create_all(conn)
session = Session(bind=engine)

# insert records
session.add_all([drizzt, elminster,
                 kobold, flying_sword,
                 griswold, ])
session.commit()

# verify commit via queries
heros = session.query(Hero)
for hero in heros:
    print(f"hero.species={hero.species}, hero.name={hero.name}, hero.size={hero.size}")

kobold_record = session.query(Monster).filter_by(name="Cabbage Beak").first()
print(f"Monster lookup: {kobold_record.name}")

# explore db
inspector = inspect(engine)

# what tables exist?
print(f"tables: {inspector.get_table_names()}")

# what cols in table exist?
columns = inspector.get_columns('monster')
for column in columns:
    print(column["name"], column["type"])

griswold.trade()