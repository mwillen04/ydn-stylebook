"""Helper functions for the stylebook

Author: Michael Willen"""

import re

def standardize(string: str) -> str:
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

def highlight(results: list, keyword: str) -> list:
    """Adds a marker to the entries to highlight the searched word"""

    for k in range (len(results)):

        results[k] = list(results[k])

        entry = results[k][1]
        new_str = ""

        # case-insensitive search for matching strings
        i = entry.lower().find(keyword.lower())

        # replace until no more matches
        while (i >= 0):

            # make sure matching string is not within an HTML tag
            if (i > 0 and ((entry[i:].find('>') < entry[i:].find('<')) or entry[i:].find('<') == -1)):
                new_str += entry[:i+len(keyword)]
            
            # otherwise, add span tags around the matching string and add the matching string back with its original case
            else:
                new_str += entry[:i]
                new_str += "<span class='highlight'>" + entry[i:i+len(keyword)] + "</span>"

            # slice entry and search again past the previous match
            entry = entry[i+len(keyword):]

            i = entry.lower().find(keyword.lower())

        # add remaining part of entry
        results[k][1] = new_str + entry

    return results