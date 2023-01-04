from logg import logging
# деление
def div(a, b):
    try:
        return a / b
    except:
        print("скорей всего деление на ноль")
        logging.warning("delenie na 0")

# умножение
def mult(a, b):
    return a * b

# извлечение квадратного корня
def spq(a):
    return a ** 0.5

# разность
def sub(a, b):
    return a - b

# сумма
def sum(a, b):
    return a + b
