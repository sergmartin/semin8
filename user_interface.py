from model import *

from logg import logging
#a = int(input("Введите символ 1: "))
#b = int(input("Введите символ 2: "))

# меню калькулятора

def deist(a, b):
    
    
    s = ["*", "/", "+", "-"]
    print("* - умножение\n", "/ - деление\n", "+ - сложение\n", "- : разность\n")
    
    n = ""
    
    while n not in s:
        n = input("Введите символ действия из списка: ")
        if n == "*":
           print(f" ответ: { mult(a, b)}")
           logging.info("mult")
        elif n == "/":
            print(f" ответ: {div(a, b)}")
            logging.info("div")
        elif n == "+":
            print(f" ответ: {sum(a, b)}")
            logging.info("sum")
        elif n == "-":
            print(f" ответ: {sub(a, b)}")
            logging.info("sub")
       

#deist(a, b)
