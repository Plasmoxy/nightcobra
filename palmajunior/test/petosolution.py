# Python 3.7
# (c) Sebastián Petrík

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


## Vrati najhorsie mozne znamky, berie aktualne znamky, cielovu znamku, pocet pisomiek
# znamky:array<int>, ciel:int, pocet:int
# return:array<int>
def nove_znamky(znamky, cielova_znamka, pocet):
    dalsie = [] # najhorsie znamky, ktore moze dostat

    ### Pomocne funkcie ###

    # arr -> array<int>
    def average(arr):
        return (sum(arr)/len(arr))
    
    def aktualna_znamka():
        spolu = znamky.copy()
        spolu.extend(dalsie)
        return round(average(spolu))
    
    ### algoritmus ###

    for i in range(0, pocet):
        dalsie.append(5)

    while (aktualna_znamka() > cielova_znamka):
        for i in range(0, pocet):
            if (aktualna_znamka() > cielova_znamka):
                #print(f"Vypocitavam : {dalsie} : {aktualna_znamka()}") # debug
                dalsie[i] = dalsie[i] - 1
            
            if dalsie[i] <= 0:
                return [] # uz nemoze nic urobit, iteracia sa uchylila k prvku <=0, co znamena ze uz sa neda dostat k cielu

    return dalsie

def main():
    zn = [3, 1, 3, 2, 4]
    c = 2
    p = 4

    vysledok = nove_znamky(zn, c, p)
    print("--- Výsledok ---")
    print(f"tvoje známky = {zn}")
    print(f"tvoja cieľová známka = {c}")
    
    if vysledok:
        print(f"\nV nasledujúcich {p} písomkách musíč dostať najhoršie :")
        print(f"{vysledok}")
    else:
        print(f"Bohužiaľ sa ti v nasledujúcich {p} písomkách už nepodarí dosiahnuť známku {c} :(")


if __name__ == "__main__":
    main()