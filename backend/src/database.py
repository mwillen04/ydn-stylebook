"""Functions to enable the stylebook to access the database used for queries

Author: Michael Willen"""

import sys
from sys import stderr
from random import randrange
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, select, collate, or_, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

#-----------------------------------------------------------------------

DATABASE_URL = 'sqlite:///stylebook.sqlite'
Base = declarative_base()

Engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=Engine)

#-----------------------------------------------------------------------

class Entry (Base):
    """Individual entry within the stylebook."""

    __tablename__ = 'dictionary'
    term =          Column('term', String, primary_key=True)
    definition =    Column('definition', String, nullable=False)

class Editor (Base):
    """Data for an individual Copy desk editor."""

    __tablename__ = 'editors'
    netid =         Column('netID', String, primary_key=True)
    last_name =     Column('last_name', String, nullable=False)
    first_name =    Column('first_name', String, nullable=False)
    year =          Column('year', Integer, nullable=False)

#-----------------------------------------------------------------------

def execute_query(query) -> list:
    """Executes provided query and returns resulting table

    Args:
        `query`: SQL query to execute

    Returns:
        list: results from querying the database
    """

    try:
        with Session() as session:
            results = session.execute(query).fetchall()
            results = [tuple(row) for row in results]
            return results

    except SQLAlchemyError as ex:
        print(ex, file=stderr)
        sys.exit(1)

#-----------------------------------------------------------------------

def get_stylebook() -> list:
    """Gets all current stylebook entries.

    Returns:
        list: all entries in the stylebook
    """

    query = select(Entry.term, Entry.definition).order_by(collate(Entry.term, 'NOCASE'))
    return execute_query(query)

#-----------------------------------------------------------------------

def get_stylebook_section(letter: str) -> list:
    """Get a specific section of the stylebook by its starting letter.

    Args:
        `letter` (str): starting letter to search for

    Returns:
        list: all entries in the stylebook that start with `letter`
    """

    # include terms that start with a quote (“) or dash (-) but otherwise start with that letter
    args = [f"{letter}%", f"-{letter}%", f"“{letter}%"]

    query = (select(Entry.term, Entry.definition)
            .where(or_(*[Entry.term.like(keyword) for keyword in args]))
            .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def term_search(keyword: str) -> list:
    """Search for terms in the stylebook that contain a given keyword.

    Args:
        `keyword` (str): keyword to search for

    Returns:
        list: all entries in the stylebook that contain the keyword in their term
    """

    query = (select(Entry.term, Entry.definition)
             .where(Entry.term.contains(keyword))
             .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def definition_search(keyword: str) -> list:
    """Search for definitions in the stylebook that contain a given keyword.

    Args:
        `keyword` (str): keyword to search for

    Returns:
        list: all entries in the stylebook that contain the keyword in their definition
    """

    query = (select(Entry.term, Entry.definition)
             .where(Entry.definition.contains(keyword))
             .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def keyword_search(keyword: str) -> list:
    """Search for terms and definitons in the stylebook that contain a given keyword.

    Args:
        `keyword` (str): keyword to search for

    Returns:
        list: all entries in the stylebook that contain the keyword in any part of the entry
    """

    query = (select(Entry.term, Entry.definition)
             .where(or_(Entry.term.contains(keyword), Entry.definition.contains(keyword)))
             .order_by(collate(Entry.term, 'NOCASE')))

    return execute_query(query)

#-----------------------------------------------------------------------

def get_random_entry() -> list:
    """Get a single entry from the stylebook, chosen randomly.
    
    Returns:
        list: a random entry from the stylebook
    """

    rowCount = len(get_stylebook())
    query = select(Entry.term, Entry.definition).offset(randrange(rowCount)).limit(1)

    return execute_query(query)

#-----------------------------------------------------------------------

def get_editors() -> list:
    """Gets the names of all current Copy desk editors.

    Returns:
        list: names of all Copy desk editors, sorted by year, first name, then last name
    """

    query = (select((Editor.first_name + " " + Editor.last_name).label("name"))
            .order_by(Editor.year, collate(text('name'), 'NOCASE')))

    return execute_query(query)
