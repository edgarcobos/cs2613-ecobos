#!/usr/bin/python3

import csv

def read_csv(filename):
    """Read a CSV file, return list of rows"""
    lst = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            lst.append([item.lstrip() for item in row])
        return lst

def header_map(row):
    """Build a dictionary from labels to column numbers"""
    return {row[i]: i for i in range(len(row))}
    
def select(table, dct):
    """Create a new table with specific columns of the given table""" 
    lst = []
    header = header_map(table[0])
    vals = [header[key] for key in header if key in dct]
    for row in table:
        lst.append([row[i] for i in vals])
    return lst

def row2dict(hmap, row):
    """Take the output from header_map and a row, return a dictionary representing that row"""
    dct = {}
    rmap = header_map(row)
    for key in hmap:
        for val in rmap:
            if hmap[key] == rmap[val]:
                dct[key] = val
    return dct

def compare(left, op, right):
    """Helper function to make comparisons between left and right"""
    if op == '==':
        return left == right
    elif op == '<=':
        if left == 'NULL' or right == 'NULL':
            return left == 'NULL' and right == 'NULL'
        return left <= right
    elif op == '>=':
        if left == 'NULL' or right == 'NULL':
            return left == 'NULL' and right == 'NULL'
        return left >= right

def check_row(row, query):
    """Check if a row matches a query tuple"""
    left = query[0]
    op = query[1]
    right = query[2]
    if left in row:
        left = row[left]
    if right in row:
        right = row[right]
    if op in ['==', '<=', '>=']:
        left = str(left)
        right = str(right)
        try:
            left = int(left)
            right = int(right)
        except ValueError:
            pass
        return compare(left, op, right)
    elif op == 'AND':
        return check_row(row,left) and check_row(row,right)
    elif op == 'OR':
        return check_row(row,left) or check_row(row,right)

def filter_table(table, query):
    """Select certain rows of the table according to a query"""
    lst = []
    for row in table:
        if row == table[0]:
            lst.append(table[0])
        else:
            if check_row(row2dict(header_map(table[0]), row), query):
                lst.append(row)
    return lst