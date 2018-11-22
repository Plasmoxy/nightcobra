"""

(c) ShardBytes 2018
Palma Junior, tím shardbytes

Úloha 6

Vytvor funkciu kontrola s vhodnými parametrami, ktorá vráti informáciu, či zadané
percento môže byť pre danú triedu korektné alebo je chybné.
Svoje riešenie ulož do súboru falosne_percenta.py

parametre -> max pocet ziakov, percento na kontrolu

m -> pocet ziakov ktori maju dobry prospech
n -> pocet ziakov v triede
p -> percento ziakov ktori maju dobry prospech

p = 100% * m/n

m' = p*n / 100%

Dokaz -> Ak pocet ziakov vzhladom na vstupne percento je prirodzene cislo,
potom dany pocet ziakov existuje (nemozeme mat 1.5 ziaka).
( prirodzene cislo overim nezapornostou a nulovym modulom 1.0 )

"""

# vsetci<int> = pocet ziakov v triede
# percento<float> = pocet percent na overenie
# ak percento je nezaporne a je mozny pocet ziakov s danym percentom, vrat True,
# ak inak -> vrat False
def kontrola(vsetci, percento):
    return vsetci >=0 and percento >= 0 and ((percento*vsetci) / 100 ) % 1.0 == 0
