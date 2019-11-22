from A5 import Type

def test_enum():
    '''check that defined enum type matches assignment'''

    assert sorted([ member.name for member in Type ]) == ["BALANCE", "CURRENCY", "IDENT", "OPEN", "TRANSFER"]