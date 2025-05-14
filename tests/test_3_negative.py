from ya_test.myapp.delivery_cost import delivery_cost_calculator
import pytest
import pytest_check as check

def test_negative_1():
    assert delivery_cost_calculator(31, 1, True, 1) == "Can't be delivered"

def test_negative_2():
    check.equal(delivery_cost_calculator(-3, 0, False, 2), "Wrong parameter", msg='distance must be > 0')

def test_negative_3():
    check.equal(delivery_cost_calculator(3, 2, True), "Wrong parameter", msg='dimensions out of range')

def test_negative_4():
    #check.equal(delivery_cost_calculator(29, 1, yes, 4), "Wrong parameter", msg='fragile must be True or False')
    with pytest.raises(NameError):
        delivery_cost_calculator(29, 1, yes, 4)

def test_negative_5():
    with pytest.raises(KeyError):
        delivery_cost_calculator(5, 0, True, 6)