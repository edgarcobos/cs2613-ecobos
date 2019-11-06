from A4 import read_csv, header_map, select, row2dict, check_row

def test_read_csv():
    assert read_csv('test1.csv') == [['name', 'age', 'eye colour'],
                                     ['Bob', '5', 'blue'],
                                     ['Mary', '27', 'brown'],
                                     ['Vij', '54', 'green']]
                                     
table = read_csv('test1.csv')

def test_header_map_1():
    hmap = header_map(table[0])
    assert hmap == { 'name': 0, 'age': 1, 'eye colour': 2 }

def test_select_1():
    assert select(table,{'name','eye colour'}) == [['name', 'eye colour'],
                                                   ['Bob',  'blue'],
                                                   ['Mary', 'brown'],
                                                   ['Vij',  'green']]

def test_select_2():
    """Select with unordered dictionary"""
    assert select(table,{'eye colour','age'}) == [['age', 'eye colour'],
                                                   ['5',  'blue'],
                                                   ['27', 'brown'],
                                                   ['54',  'green']]

def test_row2dict():
    hmap = header_map(table[0])
    assert row2dict(hmap, table[1]) == {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}

def test_check_row_1():
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    assert check_row(row, ('age', '==', 5))
    assert not check_row(row, ('eye colour', '==', 5))
    assert check_row(row, ('eye colour', '==', 'blue'))
    assert check_row(row, ('age', '>=', 4))
    assert check_row(row, ('age', '<=', 1000))

def test_check_row_2():
    """Check row for header"""
    hmap = header_map(table[0])
    row = row2dict(hmap, table[0])
    assert check_row(row, ('eye colour', '==', 'eye colour'))