from A4 import read_csv, check_row, filter_table

table = read_csv('test3.csv')

def test_check_row_1():
    """Check row with negative numbers"""
    row = {'Month': 'January', 'High(deg C)': '-4', 'Low(deg C)': '-13', 'Rain(days)': '9'}
    assert check_row(row, ('Rain(days)', '==', 9))
    assert not check_row(row, ('Month', '==', 1))
    assert check_row(row, ('Month', '==', 'January'))
    assert check_row(row, ('Low(deg C)', '>=', -14))
    assert check_row(row, ('High(deg C)', '<=', -4))

def test_check_row_logical():
    row = {'Month': 'January', 'High(deg C)': '-4', 'Low(deg C)': '-13', 'Rain(days)': '9'}
    assert check_row(row, (('Rain(days)', '==', 9),'OR',('Month', '==', 1)))
    assert not check_row(row, (('Rain(days)', '==', 9),'AND',('Month', '==', 1)))

def test_filter_table1():
    """Filter table with negative numbers"""
    assert filter_table(table,('Low(deg C)', '>=', 15)) == [['Month', 'High(deg C)', 'Low(deg C)', 'Rain(days)'],
                                                            ['July', '26', '15', '9'],
                                                            ['August', '25', '15', '8']]

    assert filter_table(table,('High(deg C)', '<=', -1)) == [['Month', 'High(deg C)', 'Low(deg C)', 'Rain(days)'],
                                                             ['January', '-4', '-13', '9'],
                                                             ['February', '-2', '-12', '7']]

    assert filter_table(table,('Month', '==', 'January')) == [['Month', 'High(deg C)', 'Low(deg C)', 'Rain(days)'],
                                                              ['January', '-4', '-13', '9']]

    assert filter_table(table,('Rain(days)', '==', 11)) == [['Month', 'High(deg C)', 'Low(deg C)', 'Rain(days)'],
                                                             ['December', '0', '-7', '11']]

def test_filter_table2():
    assert filter_table(table,(('Low(deg C)', '>=', 11),'AND',('High(deg C)','<=','24'))) == [['Month', 'High(deg C)', 'Low(deg C)', 'Rain(days)'],
                                                                                              ['June', '23', '12', '9'],
                                                                                              ['September', '21', '11', '8']]


    assert filter_table(table,(('Rain(days)', '<=', 11),'AND',('Rain(days)','>=','11'))) == [['Month', 'High(deg C)', 'Low(deg C)', 'Rain(days)'],
                                                                                             ['December', '0', '-7', '11']]

    assert filter_table(table,(('Month', '==', 'January'),
                               'OR',
                               ('Rain(days)','==',11))) == [['Month', 'High(deg C)', 'Low(deg C)', 'Rain(days)'],
                                                            ['January', '-4', '-13', '9'],
                                                            ['December', '0', '-7', '11']]
