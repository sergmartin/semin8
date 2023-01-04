# запрос переменных и проверка на число

def ent_a():
    a = ""
    while (not a.isdigit()):
        a = input("Ведите первое целое число: ")
        if (not a.isdigit()):
            print("Прочитайте еще раз, что необходимо ввести!")
    a = int(a)  
    return a

def ent_b():
    b = ""
    while (not b.isdigit()):
        b = input("Ведите второе целое число: ")
        if (not b.isdigit()):
            print("Прочитайте еще раз, что необходимо ввести!")
    b = int(b)  
    return b
    
#print(ent_a())
#print(ent_b())
