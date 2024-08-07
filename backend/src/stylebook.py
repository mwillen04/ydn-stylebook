"""Routing and methods for the website's flask server.

Author: Michael Willen"""

from string import ascii_uppercase
from flask import Flask, request
from database import get_stylebook_section, get_editors, get_random_entry, get_top10
from database import term_search, definition_search, keyword_search
from helper import standardize, highlight, reroute, clean_results

#-----------------------------------------------------------------------

app = Flask(__name__)

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """Website homepage. Displays opening blurb and searchbar.

    Returns:
        Response: HTML page rendered from the index template
    """

    return

#-----------------------------------------------------------------------

@app.route('/search', methods=['GET'])
def search():
    """Search results. Usually displayed on homepage but can be rendered separately.

    Returns:
        Response: HTML page rendered from the search template
    """

    # get arguments from query

    keyword = request.args.get('q').lower() # word to search for
    searchtype = request.args.get('t')      # value to be searched (term, entry, both)
    full = request.args.get('f')            # whether to only search for full words

    # if no word searched, display nothing

    if keyword == '':
        return {"results" : []}

    # Ensure default search settings exist and avoid faulty searches
    
    if searchtype != "keyword" and searchtype != "term" and searchtype != "entry":
        searchtype = "keyword"

    try:
        full = int(full)
    except TypeError:
        full = 0

    if full > 1 or full < 0:
        full = 0

    # account for differing quotation marks

    keyword = standardize(keyword)

    # determine which type of search is being done, and search

    if searchtype == "term":
        results = term_search(keyword)

    elif searchtype == "entry":
        results = definition_search(keyword)

    else:
        results = keyword_search(keyword)

    # remove results found in HTML tags (and non-full words if full == 1)

    results = clean_results(results, keyword, searchtype, full)

    # highlight search word in results, if searching entries

    if searchtype != "term":
        results = highlight(results, keyword)

    # reroute links to the stylebook page

    results = reroute(results)

    if len(results) == 0:
        results = "No results."
    
    print(results)
    return {"results" : results}

#-----------------------------------------------------------------------

@app.route('/random', methods=['GET'])
def random_entry():
    """Gets a random entry to display.
    
    Returns:
        Response: a random entry from the stylebook
    """

    entry = get_random_entry()
    entry = reroute(entry)[0]

    return {"entry" : entry}

#-----------------------------------------------------------------------

@app.route('/top10', methods=['GET'])
def top10():
    """Retrieves and displays the top 10 rules.

    Returns:
        Response: a list of the top 10 rules
    """

    top10 = get_top10()

    rules = [list(ele) for ele in top10]

    return {"rules" : rules}

#-----------------------------------------------------------------------

@app.route('/stylebook', methods=['GET'])
def stylebook():
    """Displays the full stylebook.

    Returns:
        Response: HTML page rendered from the stylebook template
    """

    alphabet = tuple(ascii_uppercase)

    # retrieve the full stylebook, divided by first letter

    sections = []
    for letter in alphabet:
        sections.append(get_stylebook_section(letter))

    return { "dictionary" : dict(zip(alphabet, sections)) }

#-----------------------------------------------------------------------

@app.route('/ask', methods=['GET'])
def ask():
    """Under Construction. Will host Q&A for writers to ask copy style questions.
    
    Returns:
        Response: Data for Q&A page
    """

    return

#-----------------------------------------------------------------------

@app.route('/about', methods=['GET'])
def about():
    """Retrieves and displays current Copy Desk editors.

    Returns:
        Response: HTML page rendered from the staff template
    """

    editors = get_editors()

    return {"editors" : editors}

#-----------------------------------------------------------------------

@app.route('/edits', methods=['GET'])
def edits():
    """Under Construction. Will host stylebook editing and marking of potential edits.
    
    Returns:
        Response: HTML page rendered from the edits template
    """

    return

#-----------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)