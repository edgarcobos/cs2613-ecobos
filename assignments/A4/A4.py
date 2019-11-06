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