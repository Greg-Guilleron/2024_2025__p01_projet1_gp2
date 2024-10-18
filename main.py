from utils import *
from data import *
        

def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base) :
    
    # vérification que les bases de départ et visée sont différentes (si les caracteres valides des 2 bases sont les memes alors init_number == target_number)
    if sort_the_numbers_valid_chars_for_a_base(init_base) == sort_the_numbers_valid_chars_for_a_base(target_base) :
        target_number = init_number
        return target_number
    
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



def do_the_job ():

    init_number = ask_for_the_init_number (hex_number_valid_chars, ask_for_init_number_text)
    init_base = ask_for_the_init_base (base_valid_chars, ask_for_the_init_base_text)
    target_base = None
    # vérification de la validité du nombre de départ dans la base de départ
    while target_base == None :
        init_base_valid_number_chars = sort_the_numbers_valid_chars_for_a_base(init_base)
        if is_a_valid_number(init_number, init_base_valid_number_chars) : 
            target_base = ask_for_the_target_base (base_valid_chars, ask_for_the_target_base_text)
        else :
            init_base = ask_for_the_init_base(base_valid_chars, f"Le nombre de départ n'est valide en base {init_base}, veuillez changer de base de départ : ")
    
    # transformation du nombre choisi
    target_number = bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)
      
    
    return target_number


choice_to_close = choose_yes_or_no("Bonjour Jim Pioche, voulez vous convertir un nombre ? : ")

while choice_to_close == True :
    print(f"le nombre est cherché est : {str(do_the_job())}")
    choice_to_close = choose_yes_or_no("Voulez vous convertir un autre nombre ?")

print("A bientôt !!")



