"""Helper functions for the stylebook

Author: Michael Willen"""

import re

def standardize(string):
    """convert straight quotes to curly ones"""
    string = re.sub(r'\b"',r'”',string)   # closing double on word    
    string = re.sub(r'"\b',r'“',string)   # opening double on word
    string = re.sub(r'\b\'',r'’',string)  # closing single on word
    string = re.sub(r'\'\b',r'‘',string)  # opening single on word

    string = re.sub(r'([^\w\d\s:])"',r'\1”',string)  # closing double on punctuation
    string = re.sub(r'([^\w\d\s:])\'',r'\1’',string) # closing single on punctuation

    string = re.sub(r'\S\'\S',r'’',string)   # apostrophe can be virtually anywhere

    # FIXME: what about single and double quotes not next to word or punctuation? Pairs?

    return(string)