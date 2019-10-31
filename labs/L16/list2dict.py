#!/usr/bin/python3

def list2dict(lst):
    return {i+1: lst[i] for i in range(len(lst))}

def swapem(dict):
    return {val: key for key, val in dict.items()}