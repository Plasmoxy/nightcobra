
# postupnost = text!! s postupnostou
# napriklad vypocitaj_uhol("SSSZ")
def vypocitaj_uhol(postupnost):

    hodnoty = {
        'S': 0,
        'V': 90,
        'J': 180,
        'Z': 270
    }
    
    # vypocet

    # v pripade ze sa orientujeme podla zapadu ako hlavneho smeru,
    # dochadza k vypoctom so zapornymi hodnotami, takze si modifikujeme sever ako 360 stupnov
    if 'Z' in postupnost:
        hodnoty['S'] = 360
    else:
        hodnoty['S'] = 0

    # koncovy index
    koniec = len(postupnost)-1 

    # aktualny uhol
    u = hodnoty[postupnost[koniec]]

    # iteracia od konca, vypocitanie diferencie a pridanie k danemu uhlu
    for i in range(koniec, -1, -1):
        # print(f"u={u}, i={i}")

        # diferencia medzi aktualnym a nasledujucim uhlom
        # diferencia v sebe uklada informaciu o smere posunu !
        d = hodnoty[postupnost[i]] - u

        # ak je |diferencia| > 90 stupnov, uhol nema zmysel lebo sa posuvame krizom cez zaklad
        if abs(d) > 90:
            print(d)
            raise ValueError("Chyba: Chybny smer!")

        # pripocitame polovicnu diferenciu
        u = u + d/2.0

    return u
