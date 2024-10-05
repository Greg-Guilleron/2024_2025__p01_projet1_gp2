from utils import *
from data import *

def bin_to_dec(init_number) :
    
    target_number = 0
    
    if is_a_valid_number(init_number, bin_number_valid_chars) :
        poids_binaire = len(init_number) - 1
        for bit in init_number : 
            target_number += int(bit) * 2**int(poids_binaire)
            poids_binaire -= 1
        return target_number
    
    else :
        print("Le nombre de départ n'est valide en base binaire")

def bin_to_hex(init_number) :
    pass
    return target_number


def dec_to_bin(init_number) :
    pass
    return target_number


def dec_to_hex(init_number) :
    pass
    return target_number


def hex_to_bin(init_number) :
    pass
    return target_number
    
    
def hex_to_dec(init_number) :
    pass
    return target_number
    


def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    
    if init_base == target_base :
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
    
    init_number = ask_for_the_init_number (hex_number_valid_chars)
    init_base = ask_for_the_init_base (base_valid_chars)
    target_base = ask_for_the_target_base (base_valid_chars)
    
    target_number = bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)
      
    
    return target_number





print(f"le nombre est cherché est : {str(do_the_job())}")
