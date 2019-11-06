import re

def split_csv(string):
    #return [[strip_quotes(col) for col in row.split(",")] for row in string.splitlines()]
    #rows = []
    #for row in string.splitlines():
        #rows.append([strip_quotes(col) for col in row.split(",")])
    #return rows
    return [split_row(row) for row in string.splitlines()]
"""
def strip_quotes(string):
        strip_regex = re.compile(r'^"?([^"]+)"?$')
        search = strip_regex.search(string)
        if search:
            return search.group(1)
        else:
            return None

def split_row_3(string):
    split_regex=re.compile(
        r'''^   # start
        ("[^"]*"|"[^"]*"|[^,]+) # first column
        ,
        ("[^"]*"|[^,]+) # second column
        ,
        ("[^"]*"|[^,]+) # third column
        $''', re.VERBOSE)
    search = split_regex.search(string)
    if search:
        return [ strip_quotes(col) for col in search.groups() ]
    else:
        return None

def split_row(string):
    split_regex=re.compile(r'("[^"]*"|[^,]+)')
    search = split_regex.findall(string)
    if search:
        return [ strip_quotes(col) for col in search ]
    else:
        return None
"""
