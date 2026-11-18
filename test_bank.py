from bank.py import bankoper

def test_deposit():
    totalBal, updatedBal = bankoper(200000, 30000, 0)

    assert totalBal == 230000
    assert updatedBal == 230000

def test_withderaw():
    totalBal, updatedBal = bankoper(100000, 40000, 10000)

    assert totalBal == 140000
    assert updatedBal == 130000

def test_anyamont():
    totalBal, updatedBal = bankoper(150000, 0, 15000)

    assert totalBal == 150000
    assert updatedBal == 135000