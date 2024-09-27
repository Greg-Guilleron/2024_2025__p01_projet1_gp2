def ask_for_the_init_number() :

    pass


def ask_for_a_base(which_base) :

    base = 0

    while base != 2 and base != 10 and base != 16 :

        base = input(f"Quel est la base {which_base} ? 2 ; 10 ; 16 : ")

    return base



def ask_for_the_init_base() :

    return ask_for_a_base("de début")



def ask_for_the_target_base() :

    return ask_for_a_base("visée")