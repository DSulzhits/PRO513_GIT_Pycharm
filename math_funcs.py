def add(a, b):
    return a + b


def divide(a, b):
    if a != 0:
        return a / b
    raise ZeroDivisionError('На ноль делить нельзя.')


def multiply(a, b):
    return a * b


if __name__ == '__main__':
    print(add(3, 5))
    print(multiply(3, 5))
