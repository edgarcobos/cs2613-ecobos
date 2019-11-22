from A5 import Type, Token, Scanner, ledger
import pytest

def test_enum():
    '''check that defined enum type matches assignment'''

    assert sorted([ member.name for member in Type ]) == ["BALANCE", "CURRENCY", "IDENT", "OPEN", "TRANSFER"]

def test_token():
    token=Token(Type.IDENT,"hello")
    assert token.type==Type.IDENT
    assert token.value=="hello"

def test_str():
    id=Token(Type.IDENT,"hello")
    assert str(id) == '[IDENT: hello]'
    money=Token(Type.CURRENCY,10042)
    assert str(money) == '[CURRENCY: 100.42]'

def test_equal_ident():
    assert Token(Type.IDENT,"Bob") == Token(Type.IDENT,"Bob")
    assert Token(Type.IDENT,"Bob") != Token(Type.IDENT,"bOb")

def test_equal_keywords():
    assert Token(Type.TRANSFER,"transfer") != Token(Type.OPEN,"open")
    assert Token(Type.OPEN,"OPEN") == Token(Type.OPEN,"open")
    assert Token(Type.BALANCE,"BALANCE") == Token(Type.BALANCE,"balance")

def test_equal_currency():
    assert Token(Type.CURRENCY,1000) == Token(Type.CURRENCY,1000)
    assert Token(Type.CURRENCY,1000) != Token(Type.CURRENCY,1001)

def test_equal_bad():
    '''test for class mismatch'''
    assert Token(Type.CURRENCY,1000) != '[Type.CURRENCY, 10.00]'

def test_scan_keywords():
    scanner=Scanner('''TrAnsFer transfer 
                       OPEN BALANCE balance''')
    toks = [Token(Type.TRANSFER,"TrAnsFer"), Token(Type.TRANSFER,"transfer"),
            Token(Type.OPEN,"OPEN"),
            Token(Type.BALANCE,"BALANCE"),  Token(Type.BALANCE,"balance")]

    assert [tok for tok in scanner] == toks
    # iterate a second time
    assert [tok for tok in scanner] == toks

def test_scan_identifiers():
    scanner=Scanner("equity cash end_of_the_world_fund")
    assert list(scanner) == [Token(Type.IDENT,"equity"),
                                        Token(Type.IDENT,"cash"),
                                        Token(Type.IDENT,"end_of_the_world_fund")]

def test_scan_currency():
    scanner=Scanner("100 100.00 100.42 -123.45")
    assert list(scanner) == [Token(Type.CURRENCY,10000),
                             Token(Type.CURRENCY,10000),
                             Token(Type.CURRENCY,10042),
                             Token(Type.CURRENCY,-12345)]

def test_scan_bad():
    scanner=Scanner("&crash")
    with pytest.raises(ValueError, match="&crash"):
        next(scanner)

def test_empty():
    assert list(ledger("")) == []
def test_balance():
    assert list(ledger('''
                    balance cash
                    balance stock
                    ''')) == [("cash",0),("stock",0)]
def test_open():
    assert list(ledger('''
                        open cash 100
                        balance cash
    ''')) == [("cash",10000)]
def test_transfer():
    assert list(ledger('''
                        open cash 100
                        open expenses 0
                        transfer cash expenses 50
                        balance cash
                        balance expenses
                        ''')) == [("cash",5000),("expenses",5000)]
def test_ledger():
    '''test assignment's example'''
    assert list(ledger('''
                        open cash 100
                        open expenses 0
                        open equity 0
                        transfer cash expenses 50
                        transfer equity cash 100
                        balance cash
                        balance expenses
                        ''')) == [("cash",15000),("expenses",5000)]

def test_crash():
    '''test exception for string with unexpected value'''
    ldgr = ledger("open &crash 100")
    with pytest.raises(ValueError, match="&crash"):
        next(ldgr)

def test_transfer2():
    '''test exception for string with transfer before both accounts involved are opened'''
    ldgr = ledger('''
                        open cash 100
                        transfer cash expenses 50
    ''')
    with pytest.raises(ValueError, match="transfer"):
        next(ldgr)

def test_open2():
    '''test exception for string with open that opens existing account'''
    ldgr = ledger('''
                        open cash 100
                        open cash 0
    ''')
    with pytest.raises(ValueError, match="open"):
        next(ldgr)