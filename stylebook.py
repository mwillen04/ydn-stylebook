"""Author: Michael Willen"""

from flask import Flask, make_response, render_template
from database import get_stylebook_section
from string import ascii_uppercase

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

@app.route('/stylebook', methods=['GET'])
def stylebook():

    alphabet = tuple(ascii_uppercase)
    
    sections = []
    for letter in alphabet:
        sections.append(get_stylebook_section(letter))
    
    html = render_template('stylebook.html', dictionary = dict(zip(alphabet, sections)))
    response = make_response(html)
    return response