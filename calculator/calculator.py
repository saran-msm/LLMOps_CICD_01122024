import math
from typing import Union

class Calculator:
    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x + y
    
    def subtract(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x - y
    
    def multiply(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x * y
    
    def divide(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y
    
    def logarithm(self, x: Union[int, float]) -> float:
        if x <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        return math.log10(x)
    
    def square(self, x: Union[int, float]) -> Union[int, float]:
        return x ** 2
    
    def square_root(self, x: Union[int, float]) -> float:
        if x < 0:
            raise ValueError("Square root is not defined for negative numbers")
        return math.sqrt(x) 