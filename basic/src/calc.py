def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        raise ValueError('Denominator cannot be 0')
        # return float('inf')
    return a / b