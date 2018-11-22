
hodnoty = {
    'S': 0,
    'V': 90,
    'J': 180,
    'Z': 270
}

def rekurzivny_uhol(s, i=None, u=None):

    print(f"s={s}, i={i}, u={u}")

    # initializujem index ako posledny index stringu
    if (i==None):
        i = len(s) - 1
    
    # podmienka rekurzie
    if (i == 0):
        return u # ak sme uz na konci stringu
    else:
        
        u = u + (hodnoty[s[i]] - u) / 2.0

        # rekurzia, znizim index o 1, pouzijem novy uhol ako holder
        return rekurzivny_uhol(s, i-1, u)

# sekvencia = text s postupnostou
def vypocitaj_uhol(postupnost):
    
    # over
    pocetJedinecnych = ('S' in postupnost) + ('V' in postupnost) + ('J' in postupnost) + ('Z' in postupnost)

    if pocetJedinecnych > 2:
        raise ValueError("Chyba: Neplatné zadanie.")

    

    return rekurzivny_uhol(postupnost)


print(vypocitaj_uhol("J"))