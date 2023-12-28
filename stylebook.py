"""Routing and methods for the website's flask server.

Author: Michael Willen"""

from string import ascii_uppercase
from flask import Flask, request, make_response, render_template
from database import get_stylebook_section, get_editors
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

    html = render_template('index.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/search', methods=['GET'])
def search():
    """Search results. Usually displayed on homepage; can be rendered separately.

    Returns:
        Response: HTML page rendered from the search template
    """

    # get arguments from query

    keyword = request.args.get('q').lower() # word to search for
    searchtype = request.args.get('t')      # value to be searched (term, entry, both)
    full = int(request.args.get('f'))       # whether to only search for full words

    # if no word searched, display nothing

    if keyword == '':
        return make_response('')

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

    html = render_template('components/search.html', results=results)
    response = make_response(html)

    return response

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

    html = render_template('stylebook.html', dictionary = dict(zip(alphabet, sections)))
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/staff', methods=['GET'])
def staff():
    """Retrieves and displays current Copy Desk editors.

    Returns:
        Response: HTML page rendered from the staff template
    """

    editors = []

    # results come as list of 1-item tuples; flattens this 2D list/tuple
    for row in get_editors():
        editors.extend(row)

    html = render_template('staff.html', editors = editors)
    response = make_response(html)
    return response
