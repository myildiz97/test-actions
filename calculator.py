def add(x, y):
    if x is None or y is None:
        raise ValueError(f'Invalid parameters: x={x}, y={y}')
    return x + y


def subtract(x, y):
    if x is None or y is None:
        raise ValueError(f'Invalid parameters: x={x}, y={y}')
    return x - y


def multiply(x, y):
    if x is None or y is None:
        raise ValueError(f'Invalid parameters: x={x}, y={y}')
    return x * y


def divide(x, y):
    if x is None or y is None:
        raise ValueError(f'Invalid parameters: x={x}, y={y}')
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y