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
  

valid_response = [
    "oui",      # Français
    "yes",      # Anglais
    "sí",       # Espagnol
    "Ja",       # Allemand
    "Sì",       # Italien
    "はい" ,       # Japonais
    "네" ,         # Coréen
    "Да" ,        # Russe
    "sim",      # Portugais
    "да" ,         # Bulgare
    "taip",     # Malais
    "evet",     # Turc
    "شاهد" ,  # Arabe
    "už" ,         # Lituanien
    "ya",       # Indonésien
    "tак" ,       # Ukrainien
    "aye",      # Écossais
    "o",        # Grec
    "haan",     # Hindi
    "si",       # Filipino
    "ja",       # Néerlandais 
    ]
    
unvalid_response = [
    "non",      # Français
    "no",       # Anglais
    "No",       # Espagnol
    "nein",     # Allemand
    "Noo",       # Italien
    "いいえ" ,    # Japonais
    "아니요" ,  # Coréen
    "hет" ,       # Russe
    "não",      # Portugais
    "не" ,          # Bulgare
    "tidak",    # Malais
    "hayır",     # Turc
    "لا" ,         # Arabe
    "ne" ,         # Lituanien
    "tidak",    # Indonésien
    "hі" ,        # Ukrainien
    "na",       # Écossais
    "Όχι" ,      # Grec
    "नहीं" ,     # Hindi
    "hindi",    # Filipino
    "nee",      # Néerlandais
    ]

  
bin_base_valid_chars = [
    "2", "binaire", "binary", "base2", "base-2", "bin", "b2", "02", "binario", "binaryy",
    "binn", "01", "two", "deux", "1-0", "bi2", "second", "deuce", "bit", "binary2",
    "deuxx", "deaux", "d'eux", "d'euxs", "d'euxx", "deu", "deuxe", "dos", "zwei", "due",
    "twee", "два", "iki", "dwa", "dva", "hai", "binairee", "binnair", "binere", "binarre",
    "binairey", "dEUX"
]

dec_base_valid_chars = [
    "10", "dix", "ten", "décimal", "decimal", "base10", "base-10", "b10", "010", "décimale",
    "décimaux", "tendecimal", "decimalt", "10d", "10dec", "dixème", "tennth", "d10", "dezimal", "10base"
]

hex_base_valid_chars = [
    "16", "hexadécimal", "hexadecimal", "base16", "base-16", "hex", "h16", "0x10", "016", "seize",
    "sixteen", "hexadec", "hexa", "hdecimal", "x16", "seizeième", "sixteenn", "0x", "hex16", "16base",
    "hexa", "h", "he", "0x1A", "hexadezimal", "esadecimale", "hexadecimal", "hexadecimaal", "шестнадцатеричный", "十六进制",
    "16進数", "16진수", "ستة عشر ", "onaltılık", "hexadecimalt", "hexadecimalt", "heksadesimal", "heksadesimaali",
    "hexadecimális", "szesnastkowy", "hexadecimální", "šesnajsti", "hexadecimálny", "heksadecimalni", "хексадецимални",
    "хексадесетичен", "hexazecimal", "šešioliktainis", "sešpadsmitais", "kuusteistkümnes", "sextán", "esadeċimali",
    "hexadezimala", "hexadecimal", "hexadecimal", "hexadécimale", "hexadesimal", "luxembourgeois", "хексадецимален",
    "heksadecimal", "hệ mười sáu", "ฐานสิบหก", "ষোলবেস", "பதினாறு அடிப்படை", "سولہ گن ", "شانزده ", "שש עשרה",
    "षोडश ", "شانزده ", "ܫܬܐ ܥܣܪܐ ", "მეათექვსმეტიანა", "hexadesimali"
]
  
  
base_valid_chars = bin_base_valid_chars \
    + dec_base_valid_chars \
    + hex_base_valid_chars
