"""Functions to enable the stylebook to access the database used for queries

Author: Michael Willen"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, select, collate, or_, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sys import stderr
import sys

#-----------------------------------------------------------------------

DATABASE_URL = 'sqlite:///stylebook.sqlite'
Base = declarative_base()

Engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=Engine)

#-----------------------------------------------------------------------

class Entry (Base):

    __tablename__ = 'dictionary'
    term =          Column('term', String, primary_key=True)
    definition =    Column('definition', String, nullable=False)

class Editor (Base):

    __tablename__ = 'editors'
    netid =         Column('netID', String, primary_key=True)
    last_name =     Column('last_name', String, nullable=False)
    first_name =    Column('first_name', String, nullable=False)
    year =          Column('year', Integer, nullable=False)

#-----------------------------------------------------------------------

def execute_query(query) -> list:
    """
    Params:
    * `query`: SQL query to execute

    Executes query provided in `query` and returns resulting table"""

    try:
        with Session() as session:
            return session.execute(query).fetchall()

    except SQLAlchemyError as ex:
        print(ex, file=stderr)
        sys.exit(1)

#-----------------------------------------------------------------------

def get_stylebook() -> list:

    query = select(Entry.term, Entry.definition).order_by(collate(Entry.term, 'NOCASE'))
    return execute_query(query)

#-----------------------------------------------------------------------

def get_stylebook_section(letter: str) -> list:

    args = [f"{letter}%", f"-{letter}%", f"“{letter}%"]

    query = (select(Entry.term, Entry.definition)
            .where(or_(*[Entry.term.like(keyword) for keyword in args]))
            .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def term_search(keyword: str) -> list:

    query = (select(Entry.term, Entry.definition)
             .where(Entry.term.contains(keyword))
             .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def definition_search(keyword: str) -> list:

    query = (select(Entry.term, Entry.definition)
             .where(Entry.definition.contains(keyword))
             .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def keyword_search(keyword: str) -> list:

    query = (select(Entry.term, Entry.definition)
             .where(or_(Entry.term.contains(keyword), Entry.definition.contains(keyword)))
             .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def get_editors() -> list:

    query = (select((Editor.first_name + " " + Editor.last_name).label("name"))
            .order_by(Editor.year, collate(text('name'), 'NOCASE')))
    
    return execute_query(query)
