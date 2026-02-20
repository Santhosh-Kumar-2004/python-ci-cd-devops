def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    if a < 0:
        raise ValueError("Negative numbers are not allowed")
    if b < 0:
        raise ValueError("Negative numbers are not allowed")
    return a - b


# second run test caching
def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
