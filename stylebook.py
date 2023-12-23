"""Author: Michael Willen"""

from flask import Flask, request, make_response, render_template
from database import get_stylebook_section, term_search, definition_search, keyword_search
from string import ascii_uppercase
from helper import standardize, highlight, reroute

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

    keyword = request.args.get('q')
    searchtype = request.args.get('t')
    full = int(request.args.get('f'))

    if keyword == '':
        return make_response('')

    # account for differing quotation marks
    
    keyword = standardize(keyword)

    # check whether or not to match full word

    if not full:
        keyword_s = f"%{keyword}%"
    else:
        keyword_s = keyword

    # determine which type of search is being done, and search
    
    if (searchtype == "term"):
        results = term_search(keyword_s)
    
    elif (searchtype == "entry"):
        results = definition_search(keyword_s)
        results = highlight(results, keyword)
    
    else:
        results = keyword_search(keyword_s)
        results = highlight(results, keyword)

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