import excep
import model
import user_interface
from logg import logging

def wopr():
    n = True
    while n == True:
        m = input("посчитаем что-нибудь? ")
    
        if m.lower() == "да":
            f = input("будем извлекать квадратный корень?  ")
            logging.info("1 vopros")
            if f.lower() == "да":
                
                print(model.spq(excep.ent_a()))
                logging.info("koren")
            elif f.lower() == "нет":
                user_interface.deist(excep.ent_a(), excep.ent_b() )    
                logging.info("perehod k deistvijam")
        elif m.lower() == "нет":
            print("нет так нет((((")
            n = False
            logging.info("vihog pri otricatelnon otvete")
logging.info("Start program")
wopr()