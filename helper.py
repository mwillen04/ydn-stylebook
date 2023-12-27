"""Helper functions for the stylebook

Author: Michael Willen"""

import re

#-----------------------------------------------------------------------

def standardize(string: str) -> str:
    """convert straight quotes to curly ones. Found on Stack Overflow."""

    string = re.sub(r'\b"',r'”',string)   # closing double on word    
    string = re.sub(r'"\b',r'“',string)   # opening double on word
    string = re.sub(r'\b\'',r'’',string)  # closing single on word
    string = re.sub(r'\'\b',r'‘',string)  # opening single on word

    string = re.sub(r'([^\w\d\s:])"',r'\1”',string)  # closing double on punctuation
    string = re.sub(r'([^\w\d\s:])\'',r'\1’',string) # closing single on punctuation

    string = re.sub(r'\S\'\S',r'’',string)   # apostrophe can be virtually anywhere

    return string

#-----------------------------------------------------------------------

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
            if within_html_tag(entry, i):
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

#-----------------------------------------------------------------------

def reroute(results: list) -> list:
    """changes search result links to route to the stylebook"""

    for k in range (len(results)):

        results[k] = list(results[k])

        results[k][1] = results[k][1].replace('#', 'stylebook#')

    return results

#-----------------------------------------------------------------------

def clean_results(results: list, keyword: str, searchtype: str, full: bool):
    """
    * Remove results where the keyword was only found in an HTML tag
    * Remove results that don't fully match the keyword when `full` is toggled"""

    # check each row

    k = 0
    while (k < len(results)):

        if searchtype == "term": string = results[k][0].lower()
        if searchtype == "entry": string = results[k][1].lower()
        if searchtype == "keyword": string = results[k][0].lower() + "||" + results[k][1].lower()

        # check if the search term is solely a tag; if so remove it
        if re.search(rf"{keyword}([^>]|$)", string) is None:
            results.pop(k)

        # check if the search term is solely a link; if so remove it
        elif re.search(rf"([^#<]|^){keyword}", string) is None:
            results.pop(k)

        # if searching for full terms, remove non-full terms
        elif full and re.search(rf"([^\w#<]|^){keyword}([^\w>]|$)", string) is None:
            results.pop(k)

        # if not removed, continue through results
        else: 
            k += 1

    return results

#-----------------------------------------------------------------------

def within_html_tag(string: str, index: int) -> bool:
    """check if current location in string is within an HTML tag"""

    if (index < 0): return False

    start = string[index:].find('<')
    end = string[index:].find('>')

    if (end == -1): return False        # no more end tags to even be inside
    if (start == -1): return True       # no more start tags but an end tag remains
    if (start < end): return False      # both tags remain but a start comes before an end
    return True                         # next end tag comes before next start tag
