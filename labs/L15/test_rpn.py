from rpn import process,stack,process_list

def test_push():
    process("1")
    process("2")
    assert stack == [1,2]

def test_plus():
    process("clear")
    process("1")
    process("2")
    process("+")
    assert stack == [3]

def test_minus():
    process("clear")
    process("4")
    process("2")
    process("-")
    assert stack == [2]

def test_mult():
    process("clear")
    process("2")
    process("2")
    process("*")
    assert stack == [4]

def test_div():
    process("clear")
    process("4")
    process("2")
    process("/")
    assert stack == [2]



def test_div2():
    process("clear")
    process("2")
    process("3")
    process("/")
    assert stack == [0]

def test_dup():
    process("clear")
    process("4")
    process("2")
    process("dup")
    assert stack == [4,2,2]

def test_pop():
    process("clear")
    process("4")
    process("2")
    process("pop")
    assert stack == [4]

def test_swap():
    process("clear")
    process("4")
    process("2")
    process("swap")
    assert stack == [2,4]

def test_print():
    process("clear")
    process("3")
    process("4")
    retv=process("print")
    otherv=process("+")
    assert retv == 4
    assert otherv == None
    assert stack == [7]

def test_list_plus():
    ops ='clear 3 4 + print'.split()
    assert process_list(ops) == [7]

def test_list_mult():
    ops ='clear 3 4 * print'.split()
    assert process_list(ops) == [12]

def test_list_combo():
    ops ='clear 3 4 * print 2 + print'.split()
    assert process_list(ops) == [12,14]

def test_list_quit():
    ops ='clear 3 4 * print 2 + quit print'.split()
    assert process_list(ops) == [12]

def test_a():
    ops='15 7 1 1 + - / 3 * 2 1 1 + + - print quit'.split()
    assert process_list(ops) == [5]

def test_b():
    ops='17 3 2 * print dup dup pop + 3 / print swap - 13 + 2 ^ print quit'.split()
    assert process_list(ops) == [6,4,0]

def test_c():
    ops='2 128 ^ 3 / -2 * print quit'.split()
    assert process_list(ops) == [-226854911280625642308916404954512140970]
