"""Functions to enable the stylebook to access the database used for queries

Author: Michael Willen"""

from contextlib import closing
from sqlite3 import connect
from sys import stderr
import sys

DATABASE_URL = 'stylebook.sqlite'

#-----------------------------------------------------------------------

def execute_query(query: str, args: dict = None) -> list:
    """
    Params:
    * `query`: SQL query to execute
    * `args`: arguments to add to query

    Executes query provided in `query` and returns resulting table"""

    try:
        query = str(query)
        try:
            with connect(DATABASE_URL) as conn:
                with closing(conn.cursor()) as cursor:

                    cursor.execute(query, args)
                    tabl = cursor.fetchall()

            return tabl

        except FileNotFoundError:
            print("Error: could not access database", file=stderr)
            sys.exit(1)

    except TypeError:
        print("Error: value must be a string.")
        sys.exit(1)

#-----------------------------------------------------------------------

def get_stylebook() -> list:

    query = "SELECT term, definition FROM dictionary"
    return execute_query(query)

#-----------------------------------------------------------------------

def get_stylebook_section(letter: str) -> list:

    query = """
            SELECT term, definition FROM dictionary 
            WHERE term LIKE ? 
            OR term LIKE ?
            """

    return execute_query(query, [f"{letter}%", f"“{letter}%"])

#-----------------------------------------------------------------------

def term_search(keyword: str) -> list:

    query = """
            SELECT term, definition FROM dictionary 
            WHERE term LIKE ?
            """

    return execute_query(query, [f"%{keyword}%"])

#-----------------------------------------------------------------------

def definition_search(keyword: str) -> list:

    query = """
            SELECT term, definition FROM dictionary 
            WHERE definition LIKE ?
            """

    return execute_query(query, [f"%{keyword}%"])

#-----------------------------------------------------------------------

def keyword_search(keyword: str) -> list:

    query = """
            SELECT term, definition FROM dictionary 
            WHERE term LIKE ? 
            OR definition LIKE ?
            """

    return execute_query(query, [f"%{keyword}%", f"%{keyword}%"])
