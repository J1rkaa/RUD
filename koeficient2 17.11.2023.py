
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
    elif 0 <= pocet_obcanu <= 50:
        # Výpočet pro rozmezí 2001-30000
        vysledek = 1.0000 * pocet_obcanu
    else:
        # Chybová zpráva 
        return "Zadali jste neplatný počet občanů."

    return vysledek


pocet_obcanu = int(input("Zadejte počet občanů: "))


vysledek = vypocet(pocet_obcanu)

novy_vysledek = (vysledek / 9484053.2589) * 0.61877832 * 0.78 * 0.79 * 100


print(f"Výsledek výpočtu je: {novy_vysledek}")

0.61877832