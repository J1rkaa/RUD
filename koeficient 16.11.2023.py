"""

def vypocet(pocet_obcanu):
    if 51 <= pocet_obcanu <= 2000:
        # Výpočet pro rozmezí 51-2000
        vysledek = (pocet_obcanu - 50) * 1.0700 + 50 * 1.0000
    elif 2001 <= pocet_obcanu <= 30000:
        # Výpočet pro rozmezí 2001-30000
        vysledek = 50 * 1.0000 + (2000 - 50) * 1.0700 + (pocet_obcanu - 2000) * 1.1523
    else:
        # Chybová zpráva pro neplatné zadání
        return "Zadali jste neplatný počet občanů."

    return vysledek


pocet_obcanu = int(input("Zadejte počet občanů: "))


vysledek = vypocet(pocet_obcanu)
print(f"Výsledek výpočtu je: {vysledek}")
"""


# Předchozí program pro výpočet občanů
def vypocet(populace):
    if 0 <= populace <= 50:
        vysledek = 1.0000 * populace
    elif 51 <= populace <= 2000:
        vysledek = 50 + 1.0700 * populace
    elif 2001 <= populace <= 30000:
        vysledek = 2136.5 + 1.1523 * populace
    else:
        vysledek = 34400.9 + 1.3663 * populace
    return vysledek

# Získání vstupu od uživatele
populace_input = int(input("Zadejte počet obyvatel: "))


vysledek_vypoctu = vypocet(populace_input)

# Násobení 
novy_vysledek = (vysledek_vypoctu / 9714289.9421) * 0.610590 * 0.78 * 0.79 * 100


print("Výsledek výpočtu je:", novy_vysledek)

