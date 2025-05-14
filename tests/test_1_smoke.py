from ya_test.myapp.delivery_cost import delivery_cost_calculator
import pytest

def test_smoke_1():
    assert delivery_cost_calculator(31, 1, False, 1) == 500

def test_smoke_2():
    assert delivery_cost_calculator(1, 0, True) == 450