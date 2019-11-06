from A4 import read_csv, check_row, filter_table

table = read_csv('test2.csv')

def test_check_row():
    """Check row with floating point values"""
    row = {'INSTNM': 'Oakwood University','ADM_RATE_ALL': '0.3435', 'SAT_AVG_ALL': '924'}
    assert check_row(row, ('SAT_AVG_ALL', '==', 924))
    assert not check_row(row, ('INSTNM', '==', 'Tuskegee University'))
    assert check_row(row, ('INSTNM', '==', 'Oakwood University'))
    assert check_row(row, ('ADM_RATE_ALL', '>=', 0.3))
    assert check_row(row, ('ADM_RATE_ALL', '<=', 0.49))

def test_check_row_logical():
    row = {'INSTNM': 'Oakwood University','ADM_RATE_ALL': '0.3435', 'SAT_AVG_ALL': '924'}
    assert check_row(row, (('SAT_AVG_ALL', '==', 924),'OR',('INSTNM', '==', 924)))
    assert not check_row(row, (('SAT_AVG_ALL', '==', 924),'AND',('INSTNM', '==', 924)))

def test_filter_table1():
    """Filter table, discarding rows with NULL"""
    assert filter_table(table,('SAT_AVG_ALL', '>=', 1150)) == [['INSTNM', 'CITY', 'STABBR', 'ZIP', 'ADM_RATE', 'ADM_RATE_ALL', 'SAT_AVG', 'SAT_AVG_ALL'],
                                                               ['University of Alabama in Huntsville', 'Huntsville', 'AL', '35899', '0.8062', '0.8062', '1180', '1180'],
                                                               ['The University of Alabama', 'Tuscaloosa', 'AL', '35487-0166', '0.5655', '0.5655', '1171', '1171'],
                                                               ['Auburn University', 'Auburn', 'AL', '36849', '0.8274', '0.8274', '1215', '1215'],
                                                               ['Birmingham Southern College', 'Birmingham', 'AL', '35254', '0.6422', '0.6422', '1177', '1177'],
                                                               ['Samford University', 'Birmingham', 'AL', '35229-2240', '0.7697', '0.7697', '1153', '1153']]

    assert filter_table(table,('SAT_AVG_ALL', '<=', 900)) == [['INSTNM', 'CITY', 'STABBR', 'ZIP', 'ADM_RATE', 'ADM_RATE_ALL', 'SAT_AVG', 'SAT_AVG_ALL'],
                                                              ['Alabama A & M University', 'Normal', 'AL', '35762', '0.8989', '0.8989', '823', '823'],
                                                              ['Alabama State University', 'Montgomery', 'AL', '36104-0271', '0.5125', '0.5125', '830', '830'],
                                                              ['Stillman College', 'Tuscaloosa', 'AL', '35401', '0.43', '0.43', '882', '882']]

    assert filter_table(table,('ADM_RATE_ALL', '==', 0.3435)) == [['INSTNM', 'CITY', 'STABBR', 'ZIP', 'ADM_RATE', 'ADM_RATE_ALL', 'SAT_AVG', 'SAT_AVG_ALL'],
                                                                    ['Oakwood University', 'Huntsville', 'AL', '35896', '0.3435', '0.3435', '924', '924']]

    assert filter_table(table,('INSTNM', '==', 'Embry-Riddle Aeronautical University-Prescott')) == [['INSTNM', 'CITY', 'STABBR', 'ZIP', 'ADM_RATE', 'ADM_RATE_ALL', 'SAT_AVG', 'SAT_AVG_ALL'],
                                                                                                     ['Embry-Riddle Aeronautical University-Prescott', 'Prescott', 'AZ', '86301-3720', '0.7898', '0.7814', '1171', '1126']]

def test_filter_table2():
    """Filter table, discarding rows with NULL values"""
    assert filter_table(table,(('ADM_RATE_ALL', '>=', 0.30),'AND',('ADM_RATE_ALL','<=','0.39'))) == [['INSTNM', 'CITY', 'STABBR', 'ZIP', 'ADM_RATE', 'ADM_RATE_ALL', 'SAT_AVG', 'SAT_AVG_ALL'],
                                                                                                     ['Oakwood University', 'Huntsville', 'AL', '35896', '0.3435', '0.3435', '924', '924'],
                                                                                                     ['Tuskegee University', 'Tuskegee', 'AL', '36088-1920', '0.3511', '0.3511', '937', '937'],
                                                                                                     ['Alaska Pacific University', 'Anchorage', 'AK', '99508', '0.3745', '0.3745', '1008', '1008']]

    assert filter_table(table,(('SAT_AVG_ALL', '<=', 924),'AND',('SAT_AVG_ALL','>=','924'))) == [['INSTNM', 'CITY', 'STABBR', 'ZIP', 'ADM_RATE', 'ADM_RATE_ALL', 'SAT_AVG', 'SAT_AVG_ALL'],
                                                                                                 ['Oakwood University', 'Huntsville', 'AL', '35896', '0.3435', '0.3435', '924', '924']]

    assert filter_table(table,(('ADM_RATE_ALL', '==', 0.3435),
                               'OR',
                               ('INSTNM','==','Embry-Riddle Aeronautical University-Prescott'))) == [['INSTNM', 'CITY', 'STABBR', 'ZIP', 'ADM_RATE', 'ADM_RATE_ALL', 'SAT_AVG', 'SAT_AVG_ALL'],
                                                                                                     ['Oakwood University', 'Huntsville', 'AL', '35896', '0.3435', '0.3435', '924', '924'],
                                                                                                     ['Embry-Riddle Aeronautical University-Prescott', 'Prescott', 'AZ', '86301-3720', '0.7898', '0.7814', '1171', '1126']]