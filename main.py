from utils import *
from data import *

def bin_to_dec(init_number) :
    target_number = 0
    poids_binaire = len(init_number) - 1
    for bit in init_number : 
        target_number += int(bit) * 2**int(poids_binaire)
        poids_binaire -= 1
    return target_number

def bin_to_hex(init_number) :
    target_number = 0
    pass
    return target_number


def dec_to_bin(init_number) :
    target_number = 1
    pass
    return target_number


def dec_to_hex(init_number) :
    target_number = 2
    pass
    return target_number


def hex_to_bin(init_number) :
    target_number = 3
    pass
    return target_number
    
    
def hex_to_dec(init_number) :
    target_number = 4
    pass
    return target_number
    
def sort_the_numbers_valid_chars_for_a_base(init_base) :
    
    match init_base :
        case init_base if init_base in bin_base_valid_chars :
            return bin_number_valid_chars
        case init_base if init_base in dec_base_valid_chars :
            return dec_number_valid_chars
        case init_base if init_base in hex_base_valid_chars :
            return hex_number_valid_chars
        

def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    
    target_number = None


    while init_base == target_base :
        print("Error la base de départ et la base visée sont les mêmes")
        target_number = None
        return 
    
    match init_base : 
            
            case init_base if init_base in bin_base_valid_chars :    
                
                    if target_base in dec_base_valid_chars : 
                        target_number = bin_to_dec(init_number)
                    else : 
                        target_number = bin_to_hex(init_number)
                
            case init_base if init_base in dec_base_valid_chars :
                
                    if target_base in bin_base_valid_chars :
                        target_number = dec_to_bin(init_number)
                    else :
                        target_number = dec_to_hex(init_number)

            case init_base if init_base in hex_base_valid_chars :
                
                    if target_base in bin_base_valid_chars :
                        target_number = hex_to_bin(init_number)
                    else :
                        target_number = hex_to_dec(init_number)

            case _:
                print("Base de départ non valide")

        
    return target_number



# assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

def do_the_job ():

    target_base = None
    init_number = ask_for_the_init_number (hex_number_valid_chars)
    init_base = ask_for_the_init_base (base_valid_chars)
    while target_base == None :
        init_base_valid_number_chars = sort_the_numbers_valid_chars_for_a_base(init_base)
        if is_a_valid_number(init_number, init_base_valid_number_chars) :
            target_base = ask_for_the_target_base (base_valid_chars)
        else :
            print(f"Le nombre de départ n'est valide en base {init_base}, veuillez changer de base de départ")
            init_base = ask_for_the_init_base(base_valid_chars)
    
    target_number = bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)
      
    
    return target_number





print(f"le nombre est cherché est : {str(do_the_job())}")
