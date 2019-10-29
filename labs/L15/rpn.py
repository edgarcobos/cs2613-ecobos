#!/usr/bin/python3

import sys

stack = []

def _binop(op, a, b):
    if (op == "+"):
        stack.append(a+b)
    elif (op == "-"):
        stack.append(a-b)
    elif (op == "*"):
        stack.append(a*b)
    elif (op == "/"):
        stack.append(a//b)
    elif (op == "^"):
        stack.append(a**b)
    elif (op == "swap"):
        stack.append(b)
        stack.append(a)

def process(line):
    if line in ["+", "-", "*", "/", "^", "swap"]:
        b = stack.pop()
        a = stack.pop()
        _binop(line, a, b)
    elif (line == "dup"):
        stack.append(stack[-1])
    elif (line == "pop"):
        stack.pop()
    elif (line == "swap"):
        _binop(line, a, b)
    elif (line == "clear"):
        stack.clear()
    elif line == "print":
        return int(stack[-1])
    else:
        stack.append(int(line))

def process_list(lines):
    out = []
    for line in lines:
        if (line == "quit"):
            break
        retv = process(line)
        if retv != None:
            out.append(retv)
        
    return out

if __name__ == '__main__':
    ops=[]
    for line in sys.stdin:
        line = line.strip()
        ops.append(line)

    out = process_list(ops)
    for line in out:
        print(line)