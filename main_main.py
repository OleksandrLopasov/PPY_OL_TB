from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from itertools import islice
from sqlalchemy import select, inspect
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import Select
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_columns
import psycopg2

# Connect to the database
engine = create_engine('postgresql://postgres:pass@localhost:5433')

# Create the Session
Session = sessionmaker(bind=engine)
session = Session()

# Declare a Base without arguments
Base = declarative_base()

# Define the models
@dataclass
class Dare(Base):
    __tablename__ = 'Dare'
    idDare = Column(Integer, primary_key=True, autoincrement=True)
    Text = Column(String(150))

@dataclass
class Dare_Pack(Base):
    __tablename__ = 'Dare_Pack'
    idDare = Column(Integer, ForeignKey('Dare.idDare'), primary_key=True, autoincrement=True)
    idPack = Column(Integer, ForeignKey('Pack.idPack'), nullable=False)

@dataclass
class Pack(Base):
    __tablename__ = 'Pack'
    idPack = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50))
    idUser = Column(Integer, ForeignKey('User.idUser'))

@dataclass
class Truth(Base):
    __tablename__ = 'Truth'
    idTruth = Column(Integer, primary_key=True, autoincrement=True)
    Text = Column(String(150))

@dataclass
class Truth_Pack(Base):
    __tablename__ = 'Truth_Pack'
    idTruth = Column(Integer, ForeignKey('Truth.idTruth'), primary_key=True)
    idPack = Column(Integer, ForeignKey('Pack.idPack'), nullable=False)

@dataclass
class User(Base):
    __tablename__ = 'User'
    idUser = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String(20))
    Password = Column(String(50))

# Create the tables
Base.metadata.create_all(engine)

# Define the relationships
Dare.packs = relationship('Dare_Pack', backref='dare', primaryjoin='Dare.idDare == Dare_Pack.idDare')
Pack.dares = relationship('Dare_Pack', backref='pack', primaryjoin='Pack.idPack == Dare_Pack.idPack')
Pack.user = relationship('User', backref='pack')
Truth.packs = relationship('Truth_Pack', backref='truth', primaryjoin='Truth.idTruth == Truth_Pack.idTruth')
Pack.truths = relationship('Truth_Pack', backref='pack', primaryjoin='Pack.idPack == Truth_Pack.idPack')

# Commit the data to the database
session.commit()

# Query the data
dares = session.query(Dare).all()
truths = session.query(Truth).all()
packs = session.query(Pack).all()

# Print the data
for dare in dares:
    print(dare.Text)

for truth in truths:
    print(truth.Text)

for pack in packs:
    print(pack.Name)
