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