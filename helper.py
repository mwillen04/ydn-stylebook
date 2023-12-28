"""Helper functions for the stylebook.

Author: Michael Willen"""

import re

#-----------------------------------------------------------------------

def standardize(string: str) -> str:
    """convert straight quotes to curly ones. Found on Stack Overflow.
    
    Args:
        `string` (str): string that was searched and will be queried

    Returns:
        str: searched word with quotation marks adjusted to match stylebook
    """

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
    """Adds a span tag to the entries to highlight the searched word
    
    Args:
        `results` (list): list of results from a database query
        `keyword` (str): string that was searched for

    Returns:
        list: results with highlighting html tags added
    """

    length = len(results)

    for k in range (length):

        results[k] = list(results[k])

        entry = results[k][1]
        new_str = ""

        # case-insensitive search for matching strings
        i = entry.lower().find(keyword.lower())

        # replace until no more matches
        while i >= 0:

            # make sure matching string is not within an HTML tag
            if within_html_tag(entry, i):
                new_str += entry[:i+len(keyword)]

            # otherwise, add span tags around the matching string and add it to the string
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
    """changes links in search results to route to the stylebook page
    
    Args:
        `results` (list): list of results from querying database

    Returns:
        list: results, with any anchors routing to their spot in the stylebook
    """

    length = len(results)

    for k in range (length):

        results[k] = list(results[k])

        results[k][1] = results[k][1].replace('#', 'stylebook#')

    return results

#-----------------------------------------------------------------------

def clean_results(results: list, keyword: str, searchtype: str, full: bool):
    """Remove results that were found only within tags (or weren't full words)

    Args:
        `results` (list): original list of results from querying the database
        `keyword` (str): string that was searched for
        `searchtype` (str): which values were search (term, entry, or both)
        `full` (bool): True if searching just for full words, False otherwise

    Returns:
        list: results with all faulty search results removed
    """

    # check each row

    k = 0
    while k < len(results):

        # determine which values are being checked in the results

        if searchtype == "term":
            string = results[k][0].lower()

        if searchtype == "entry":
            string = results[k][1].lower()

        if searchtype == "keyword":
            string = results[k][0].lower() + "||" + results[k][1].lower()

        # check if the search term is solely a tag; if so remove it
        if re.search(rf"{keyword}([^>]|$)", string) is None:
            results.pop(k)

        # check if the search term is solely a link; if so remove it
        elif re.search(rf"([^#<]|^){keyword}", string) is None:
            results.pop(k)

        # if searching for full-word terms, remove non-full-word terms
        elif full and re.search(rf"([^\w#<]|^){keyword}([^\w>]|$)", string) is None:
            results.pop(k)

        # if not removed, continue through results
        else:
            k += 1

    return results

#-----------------------------------------------------------------------

def within_html_tag(string: str, index: int) -> bool:
    """Check if current location in string is within an HTML tag
    
    Args:
        `string` (str): string to check
        `index` (int): position in the string at which to check
    
    Returns:
        bool: whether or not the index position is inside an HTML tag 
    """

    if index < 0:
        return False

    start = string[index:].find('<')
    end = string[index:].find('>')

    if end == -1:
        return False      # no more end tags to even be inside
    if start == -1:
        return True       # no more start tags but an end tag remains
    if start < end:
        return False      # both tags remain but a start comes before an end

    return True           # next end tag comes before next start tag
