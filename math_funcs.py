def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def product(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('На ноль делить нельзя!')
    return a / b


def multiply(a, b):
    if not isinstance(b, int):
        raise ValueError('Степень должна быть целым числом!')
    return a ** b


if __name__ == '__main__':
    print(add(3, 5))
    print(subtract(5, 3))
    print(product(3, 5))
    print(divide(15, 3))
    print(multiply(2, 4))
