def add(x,y):
    """Add Function"""
    return x + y

def subtract(x,y):
    """Subtract Function"""
    return x - y

def multiply(x,y):
    """Multiply Function"""
    return x * y

def divide(x,y):
    """Devide Function"""
    if y == 0:
        raise ValueError("Can't divide by zero!")
    return x / y

# print(divide(10,5))