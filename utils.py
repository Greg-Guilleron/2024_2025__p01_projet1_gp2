from data import *

bin_number_valid_chars = ["0", "1"]

base_valid_chars = ["2" ; "Deuxx" ; "Deaux" ; "D'eux" ; "D'euxs" ; "D'euxx" ; "Deu" ; "Deu" ; "Deuxs" ; "D'euxse" ; "Deuxe" ;   "⠙⠑⠥⠭" ;  "two" ; "dos" ; "zwei" ; "due" ; "dois" ; "twee" ; "два"  ; "二" ;"二" ; "عشرة "; "iki" ; "två" ; "to" ; "kaksi" ; "to" ; "dwa"; "kettő" ; "dva" ;"이" ; "hai" ; "Binaire" ; "Binairee" ; "Binnair" ; "Binere" ; "Binarre" ; "Binare" ; "Binnaire" ; "Binairey" ; "Bynaire" ; "Binairé" ; "deux" ;"Deux" ; "DEUX" ; "10" ; "ten";"diez" ;zehn ;dieci ;dez ;tien ; десять ;十 ;十 ;on ;tio ;ti ;kymmenen ;ti ;dziesięć ;tíz ;deset ;십 ; mười ; Dixx D'ix  Dixxe ;Diks ;Dics ;Diix ;D'i ;D'ixs ;D'x ; Dixz ; ⠙⠊⠭ ; dix Dix DIX ;16 ; ⠎⠑⠊⠵⠑ ; seize ; Seize ; SEIZE ; •  sixteen ; Dieciséis ;Sechzehn ;sedici ;dezesseis ;zestien ;十六 ; 十六 ; •  : ستة عشر ; on altı sextonseksten ;kuusitoista ;seksten ;szesnaście ;tizenhat ;šestnáct ;열여섯 ;
mười sáu ;  Seiz  Seise ;  Sez ;  Seizee ;  Seizez ;  Seizz ; Seizze ;  Saisze ;  Seyze ; Sise
]

dec_number_valid_chars = \
    bin_number_valid_chars \
  + ["2", "3", "4", "5", "6", "7", "8", "9"]

hex_number_valid_chars = \
    dec_number_valid_chars \
  + ["A", "B", "C", "D", "E", "F"] \
  + ["a", "b", "c", "d", "e", "f"]

def check_char_number_validity (char):
    return char in hex_number_valid_chars

def is_a_valid_number (number):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def ask_for_the_init_number ():
    init_number = input (ask_for_init_number_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_the_init_number_text)
    return init_number

def ask_for_the_init_base ():
    init_number = input (ask_for_the_init_base_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_the_init_base_text)
    return init_number

def ask_for_the_target_base ():
    init_number = input (ask_again_for_the_target_base_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_the_target_base_text)
    return init_number
        
ask_for_the_init_number ()
ask_for_the_init_base ()
