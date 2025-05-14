from ya_test.myapp.delivery_cost import delivery_cost_calculator
import pytest
    
def test_positive_1():
    assert delivery_cost_calculator(2, 0, False, 2) == 400

def test_positive_2():
    assert delivery_cost_calculator(10, 1, True, 3) == 840

def test_positive_3():
    assert delivery_cost_calculator(30, 1, False, 4) == 640

def test_positive_4():
    assert delivery_cost_calculator(31, 1, True, 1) == "Can't be delivered"