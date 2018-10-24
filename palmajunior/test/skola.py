"""
Úloha o známkach v škole
Malý Jožko z Korytnačkova je ešte žiakom. Slovenčina nie je jeho obľúbeným
predmetom, a preto je veľmi nešťastný, že na slovenčine píšu na každej hodine
päťminútovku. Žiaci na konci polroku dostanú z päťminútoviek výslednú známku,
ktorú vypočítajú tak, že priemer známok z päťminútoviek zaokrúhlia.
Keďže Jožkovi nie je slovenčina ľahostajná, nerád by z nej prepadol. Vždy si
preto stanoví cieľ, akú výslednú známku chce so slovenčiny dostať. Ak Jožko už
nejaké známky dostal, aké najhoršie známky ešte môže dostať, aby svoj cieľ
dosiahol?
Vytvor program, ktorý Jožkovi zistí, aké najhoršie známky môže ešte
z päťminútoviek dostať. Keďže Jožko sa na slovenčinu pripravuje pravidelne, chce
aby medzi novými známkami boli rozdiely čo najmenšie. Na poradí nových známok
nezáleží.

Python
Vytvor funkciu nove_znamky s vhodnými parametrami, ktorá vráti, aké najhoršie
známky ešte môže Jožko dostať tak, aby na vysvedčení mal známku, ktorú si vopred
určil.
Svoje riešenie ulož do súboru skola.py.

"""

# -> NOPE ESTE RAZ

# arr -> array<int>
def average(arr):
    return (sum(arr)/len(arr))


# znamky = aktualne znamky
# ciel = zelana znamka
def nove_znamky(znamky, ciel):
    ziaduce = [] # ziaduce znamky

    for i in range(1, 5) :
        buduce = znamky.copy()
        buduce.append(i)

        # vezmi priemer buducich znamok a zaokruhli ich
        if round(average(buduce)) <= ciel:
            ziaduce.append(i)
    
    return ziaduce

# tu mozete pouzit algoritmus
def main():
    pass

def testDokaz():
    zn = [1, 2, 3]
    ciel = 1

    print("Znamky: " + str(zn) + " priemer= " + str(average(zn)))
    print("Ciel: " + str(ciel))
    print("Mozes dostat a si safe: " + str(nove_znamky(zn, ciel)))


if __name__ == "__main__":
    testDokaz()
