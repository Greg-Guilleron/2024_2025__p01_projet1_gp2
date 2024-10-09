from data import *

bin_number_valid_chars = ["0", "1"]

dec_number_valid_chars = \
    bin_number_valid_chars \
  + ["2", "3", "4", "5", "6", "7", "8", "9"]

hex_number_valid_chars = \
    dec_number_valid_chars \
  + ["A", "B", "C", "D", "E", "F"] \
  + ["a", "b", "c", "d", "e", "f"]
  
  
bin_base_valid_chars = [
    "2",         # Numérique standard
    "binaire",   # En français
    "binary",    # En anglais
    "base2",     # Forme explicite
    "base-2",    # Variante avec tiret
    "bin",       # Version abrégée
    "b2",        # Abrégé avec "b"
    "02",        # Numérique avec zéro initial
    "binario",   # En espagnol/italien
    "binaryy",   # Variante stylisée
    "binn",      # Variante stylisée
    "01",        # Représentation binaire
    "two",       # En anglais pour deux
    "deux",      # En français pour deux
    "1-0",       # Variante explicite (1 et 0)
    "bi2",       # Combinaison abrégée
    "second",    # En anglais (deuxième)
    "deuce",     # Variante anglaise informelle
    "bit",       # Terme lié à l'informatique
    "binary2",   # Combinaison explicite  
]

dec_base_valid_chars = [
    "10",         # Numérique standard
    "dix",        # En français
    "ten",        # En anglais
    "décimal",    # En français (explicite)
    "decimal",    # En anglais (explicite)
    "base10",     # Forme explicite
    "base-10",    # Variante avec tiret
    "b10",        # Version abrégée
    "010",        # Numérique avec zéro initial
    "décimale",   # Variante française
    "décimaux",   # Variante pluriel en français
    "tendecimal", # Version combinée anglaise
    "decimalt",   # Variante stylisée en anglais
    "10d",        # Numérique abrégé avec "d"
    "10dec",      # Numérique abrégé avec "dec"
    "dixème",     # Variante française (dixième)
    "tennth",     # Variante stylisée anglaise
    "d10",        # Numérique abrégé
    "dezimal",    # En allemand
    "10base"      # Variante numérique explicite
]

hex_base_valid_chars = [
    "16",          # Numérique standard
    "hexadécimal", # En français
    "hexadecimal", # En anglais
    "base16",      # Forme explicite
    "base-16",     # Variante avec tiret
    "hex",         # Version abrégée
    "h16",         # Abrégé avec "h"
    "0x10",        # Notation hexadécimale avec préfixe
    "016",         # Numérique avec zéro initial
    "seize",       # En français pour 16
    "sixteen",     # En anglais pour 16
    "hexadec",     # Variante abrégée
    "hexa",        # Variante abrégée
    "hdecimal",    # Variante stylisée
    "x16",         # Variante avec "x"
    "seizeième",   # Variante française (seizième)
    "sixteenn",    # Variante stylisée
    "0x",          # Préfixe hexadécimal
    "hex16",       # Combinaison explicite
    "16base",      # Variante numérique explicite
]
  
  
base_valid_chars = bin_base_valid_chars \
    + dec_base_valid_chars \
    + hex_base_valid_chars


# base_valid_chars = \
#         [ "2" , "deuxx" , "deaux" , "d'eux" , "d'euxs" , "d'euxx" , "deu" , "deu" , "deuxs" , "d'euxse" , "deuxe" ,   "⠙⠑⠥⠭" ,  "two" , "dos" , "zwei", \
#         "due" , "dois" , "twee" , "два"  , "二" ,"二" , "عشرة", "iki" , "två" , "to" , "kaksi" , "to" , "dwa", "kettő" , "dva" ,"이" , "hai" , "binaire",\
#         "binairee" , "binnair" , "binere" , "binarre" , "binare" , "binnaire" , "binairey" , "bynaire" , "binairé" , "deux" ,"deux" , "dEUX" , "10",  \
#         "ten","diez" ,"zehn" ,"dieci" ,"dez" ,"tien" , "десять" ,"十" ,"十" ,"on" ,"tio" ,"ti" ,"kymmenen" ,"ti" ,"dziesięć" ,"tíz" ,"deset" ,"십",  \
#         "mười" , "dixx", "d'ix" , "dixxe" ,"diks" ,"dics" ,"diix" ,"d'i" ,"d'ixs" ,"d'x" , "dixz" , "⠙⠊⠭" ,"dix" ,"dix" ,"dIX" ,"16" , "⠎⠑⠊⠵⠑",  \
#         "seize" , "seize" , "sEIZE" ,"sixteen" , "dieciséis" ,"sechzehn" ,"sedici" ,"dezesseis" ,"zestien" ,"十六" ,"十六","ستة عشر","on altı", \
#         "sextonseksten","kuusitoista" ,"seksten" ,"szesnaście" ,"tizenhat" ,"šestnáct" ,"열여섯" ,"mười sáu" , " seiz",  "seise" , "sez" ,  "seizee", \
#         "seizez" ,  "seizz" , "seizze" ,  "saisze" ,  "seyze" , "sise"]

def check_char_number_validity (char, valid_char):
    return char in valid_char


def is_a_valid_number (number, valid_char) :
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i], valid_char)
        i = i + 1
    return is_a_valid_char
    
    
def ask_for_the_init_number (valid_char, question) :
    init_number = input (question)    
    while not (is_a_valid_number (init_number, valid_char)) == True:
        init_number = input (ask_again_for_the_init_number_text)
    return init_number

def ask_for_the_init_base (valid_char, question) :
    init_base = input (question)
    while not (check_char_number_validity (init_base, valid_char)) == True:
        init_base = input (ask_again_for_the_init_base_text)
    return init_base

def ask_for_the_target_base (valid_char, question) :
    target_base = input (question)
    while not (check_char_number_validity (target_base, valid_char)) == True:
        target_base = input (ask_again_for_the_target_base_text)
    return target_base


def sort_the_numbers_valid_chars_for_a_base(base) :
    
    match base :
        case base if base in bin_base_valid_chars :
            return bin_number_valid_chars
        case base if base in dec_base_valid_chars :
            return dec_number_valid_chars
        case base if base in hex_base_valid_chars :
            return hex_number_valid_chars
        

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
