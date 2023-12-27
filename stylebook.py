"""Author: Michael Willen"""

from flask import Flask, request, make_response, render_template
from database import get_stylebook_section, term_search, definition_search, keyword_search, get_editors
from string import ascii_uppercase
from helper import standardize, highlight, reroute, clean_results

#-----------------------------------------------------------------------

app = Flask(__name__)

#-----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/search', methods=['GET'])
def search():

    keyword = request.args.get('q').lower()
    searchtype = request.args.get('t')
    full = int(request.args.get('f'))

    if keyword == '':
        return make_response('')

    # account for differing quotation marks
    
    keyword = standardize(keyword)

    # determine which type of search is being done, and search
    
    if (searchtype == "term"):
        results = term_search(keyword)
    
    elif (searchtype == "entry"):
        results = definition_search(keyword)
    
    else:
        results = keyword_search(keyword)

    # remove results found in HTML tags (and non-full words if full == 1)

    results = clean_results(results, keyword, searchtype, full)

    # highlight results

    if (searchtype != "term"): results = highlight(results, keyword)

    # reroute links to the stylebook page

    results = reroute(results)

    html = render_template('components/search.html', results=results)
    response = make_response(html)

    return response

#-----------------------------------------------------------------------

@app.route('/stylebook', methods=['GET'])
def stylebook():

    alphabet = tuple(ascii_uppercase)

    sections = []
    for letter in alphabet:
        sections.append(get_stylebook_section(letter))
    
    html = render_template('stylebook.html', dictionary = dict(zip(alphabet, sections)))
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

@app.route('/staff', methods=['GET'])
def staff():
    
    editors = []
    for row in get_editors(): editors.extend(row)
    
    html = render_template('staff.html', editors = editors)
    response = make_response(html)
    return response
