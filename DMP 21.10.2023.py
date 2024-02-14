#Výměra
def vypocet(hodnota):
    vysledek = (hodnota / 7569130.6545) * 0.03 * 100 
    return vysledek


zadana_hodnota = float(input("Zadejte výměru obce v ha: "))


vysledek0 = vypocet(zadana_hodnota)

print("Výměru obce tvoří {:.9f}% podílu sdílených daní.".format(vysledek0))

#Obyvatelé
def vypocet(hodnota1):
    vysledek = (hodnota1 / 8649358) * 0.10 * 100
    return vysledek


zadana_hodnota = float(input("Zadejte počet občanů obce: "))


vysledek1 = vypocet(zadana_hodnota)

print("Počet občanů obce tvoří {:.9f}% podílu sdílených daní.".format(vysledek1))

#školy
def vypocet(hodnota2):
    vysledek = (hodnota2 / 1071167) * 0.09 * 100
    return vysledek


zadana_hodnota = float(input("Zadejte počet dětí a žáku školy/školky v dané obci: "))


vysledek2 = vypocet(zadana_hodnota)

print("Počet dětí a žáků navštěvující obcí zřizovanou školu nebo školku tvoří {:.9f}% podílu sdílených daní.".format(vysledek2))

#0,03% výměra
#0,10% občani značí váhu daného segmentu v procentech přičemž koeficient postupných přechodů má nejvyšší váhu 78%. Celkově dávají váhu 100%
#0,09% školy

#koeficient

def vypocet(pocet_obcanu):
    if 51 <= pocet_obcanu <= 2000:
        # Výpočet pro rozmezí 51-2000
        vysledek = 50 + 1.0700 * (pocet_obcanu - 50)
    elif 2001 <= pocet_obcanu <= 30000:
        # Výpočet pro rozmezí 2001-30000
        vysledek = 2136.5 + 1.1523 * (pocet_obcanu - 2000)
    elif 30001 <= pocet_obcanu <= 300000:
        # Výpočet pro rozmezí 2001-30000
        vysledek = 34400.9 + 1.3663 * (pocet_obcanu - 30000)
    else:
        # Chybová zpráva pro neplatné zadání
        return "Zadali jste neplatný počet občanů."

    return vysledek

# Získání vstupu od uživatele
pocet_obcanu = int(input("Zadejte počet občanů: "))

# Volání funkce a tisk výsledku
vysledek = vypocet(pocet_obcanu)

# Násobení výsledku
novy_vysledek = vysledek / 9714289.9421 * 0.610590 * 0.78 * 0.79 * 100

# Výpis výsledku
print("Výsledek výpočtu je:", novy_vysledek)

a=vysledek0
b=vysledek1
c=vysledek2
d=novy_vysledek
soucet=(a+b+c+d)
print("Celkové procento, kterým se obec podílí obec je {:.6f}%".format(soucet))