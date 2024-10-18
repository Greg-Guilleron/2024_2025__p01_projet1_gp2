ask_for_init_number_text = "Le nombre ? : "

ask_again_for_the_init_number_text = "Le nombre put***! : "

ask_for_the_init_base_text = "Quelle est la base de départ du nombre ? : "

ask_again_for_the_init_base_text = "Quelle est la base du nombre, choisissez un caractere valable ? : "

ask_for_the_target_base_text = "Quelle est la base ciblée du nombre ? : "

ask_again_for_the_target_base_text = "Quelle est la base ciblée stpp ?? : "


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
    "deuxx",
    "deaux",
    "d'eux",
    "d'euxs",
    "d'euxx",
    "deu",
    "deuxe",
    "dos",
    "zwei",
    "due",
    "twee",
    "два",
    "iki",
    "dwa",
    "dva",
    "hai",
    "binairee",
    "binnair",
    "binere",
    "binarre",
    "binairey",
    "dEUX",
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
    "hexa",
    "h",
    "he",
    "0x1A",
    "hexadezimal",  # Allemand
    "esadecimale",  # Italien
    "hexadecimal",  # Portugais
    "hexadecimaal",  # Néerlandais
    "шестнадцатеричный (shestnadtsatyerichny)",  # Russe
    "十六进制 (shíliù jìnzhì)",  # Chinois (simplifié)
    "16進数 (じゅうろくしんすう, jūroku shinsū)",  # Japonais
    "16진수 (십육진수, sip-yuk jinsu)",  # Coréen
    "ستة عشر (sittat ʿashar)",  # Arabe
    "onaltılık",  # Turc
    "hexadecimalt",  # Suédois
    "hexadecimalt",  # Danois
    "heksadesimal",  # Norvégien
    "heksadesimaali",  # Finnois
    "hexadecimális",  # Hongrois
    "szesnastkowy",  # Polonais
    "hexadecimální",  # Tchèque
    "šesnajsti",  # Slovène
    "hexadecimálny",  # Slovaque
    "heksadecimalni",  # Croate
    "хексадецимални (heksadecimalni)",  # Serbe
    "хексадесетичен (heksadesetichen)",  # Bulgare
    "hexazecimal",  # Roumain
    "šešioliktainis",  # Lituanien
    "sešpadsmitais",  # Letton
    "kuusteistkümnes",  # Estonien
    "sextán",  # Islandais
    "esadeċimali",  # Maltais
    "hexadezimala",  # Basque
    "hexadecimal",  # Catalan
    "hexadecimal",  # Galicien
    "hexadécimale",  # Walon
    "hexadesimal",  # Luxembourgeois
    "хексадецимален (heksadecimalen)",  # Macédonien
    "heksadecimal",  # Albanais
    "hệ mười sáu",  # Vietnamien
    "ฐานสิบหก (thān sìp hòk)",  # Thaï
    "ষোলবেস (shôlobes)",  # Bengali
    "பதினாறு அடிப்படை (patiṉāṟu aṭippaṭai)",  # Tamoul
    "سولہ گن (solah gan)",  # Ourdou
    "شانزده (shānzdah)",  # Persan
    "שש עשרה (shesh esreh)",  # Hébreu
    "षोडश (ṣoḍaśa)",  # Sanskrit
    "شانزده (shānzdah)",  # Farsi
    "ܫܬܐ ܥܣܪܐ (shṭā ʿasrā)",  # Syriaque
    "მეათექვსმეტიანა (meat’ek’vsmet’iana)",  # Géorgien
    "hexadesimali"  # Swahili
]
  
  
base_valid_chars = bin_base_valid_chars \
    + dec_base_valid_chars \
    + hex_base_valid_chars
