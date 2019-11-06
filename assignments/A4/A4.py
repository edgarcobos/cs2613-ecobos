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