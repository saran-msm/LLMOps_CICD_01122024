import pytest
import os
import sys

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from calculator.calculator import Calculator
import math

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        return Calculator()
    
    # Basic Operations Tests
    @pytest.mark.parametrize("x, y, expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
        # ... more test cases
    ])
    def test_add(self, calculator, x, y, expected):
        assert calculator.add(x, y) == expected
    
    @pytest.mark.parametrize("x, y, expected", [
        (5, 3, 2),
        (1, 1, 0),
        (0, -1, 1),
        (3.5, 2.0, 1.5),
        # ... more test cases
    ])
    def test_subtract(self, calculator, x, y, expected):
        assert calculator.subtract(x, y) == expected
    
    # Edge Cases
    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.divide(1, 0)
    
    def test_negative_square_root(self, calculator):
        with pytest.raises(ValueError):
            calculator.square_root(-1)
    
    def test_negative_logarithm(self, calculator):
        with pytest.raises(ValueError):
            calculator.logarithm(-1)
    
    # Advanced Operations Tests
    @pytest.mark.parametrize("x, expected", [
        (1, 0),
        (10, 1),
        (100, 2),
        # ... more test cases
    ])
    def test_logarithm(self, calculator, x, expected):
        assert math.isclose(calculator.logarithm(x), expected, rel_tol=1e-9) 