import tkinter as tk

def vypocet_vymery():
    hodnota = float(entry_vymery.get())
    vysledek = (hodnota / 7560277.4525) * 0.03 * 100
    label_vymery.config(text="Výměru obce tvoří {:.9f}% podílu sdílených daní.".format(vysledek))

def vypocet_obcanu():
    hodnota = float(entry_obcanu.get())
    vysledek = (hodnota / 8413311) * 0.10 * 100
    label_obcanu.config(text="Počet občanů obce tvoří {:.9f}% podílu sdílených daní.".format(vysledek))

def vypocet_skol():
    hodnota = float(entry_skol.get())
    vysledek = (hodnota / 1036513) * 0.09 * 100
    label_skol.config(text="Počet dětí a žáků navštěvující obcí zřizovanou školu nebo školku tvoří {:.9f}% podílu sdílených daní.".format(vysledek))

def vypocet_celkoveho_podilu():
    pocet_obcanu = int(entry_celkem_obcanu.get())
    vysledek_koeficientu = vypocet_koeficientu(pocet_obcanu)
    novy_vysledek = (vysledek_koeficientu / 9484053.2589) * 0.61877832 * 0.78 * 0.79 * 100
    label_celkoveho_podilu.config(text="Celkové procento, kterým se obec podílí, je {:.6f}%".format(novy_vysledek))

def vypocet_koeficientu(pocet_obcanu):
    if 51 <= pocet_obcanu <= 2000:
        return 50 + 1.0700 * (pocet_obcanu - 50)
    elif 2001 <= pocet_obcanu <= 30000:
        return 2136.5 + 1.1523 * (pocet_obcanu - 2000)
    elif 30001 <= pocet_obcanu <= 300000:
        return 34400.9 + 1.3663 * (pocet_obcanu - 30000)
    elif 0 <= pocet_obcanu <= 50:
        return 1.0000 * pocet_obcanu
    else:
        return "Zadali jste neplatný počet občanů."


root = tk.Tk()
root.title("Výpočet podílu obce na sdílených daních")


entry_vymery = tk.Entry(root)
entry_obcanu = tk.Entry(root)
entry_skol = tk.Entry(root)
entry_celkem_obcanu = tk.Entry(root)

button_vymery = tk.Button(root, text="Výpočet výměry", command=vypocet_vymery)
button_obcanu = tk.Button(root, text="Výpočet občanů", command=vypocet_obcanu)
button_skol = tk.Button(root, text="Výpočet škol", command=vypocet_skol)
button_celkem_obcanu = tk.Button(root, text="Výpočet celkového podílu", command=vypocet_celkoveho_podilu)


label_vymery = tk.Label(root, text="")
label_obcanu = tk.Label(root, text="")
label_skol = tk.Label(root, text="")
label_celkoveho_podilu = tk.Label(root, text="")


entry_vymery.grid(row=0, column=1)
entry_obcanu.grid(row=1, column=1)
entry_skol.grid(row=2, column=1)
entry_celkem_obcanu.grid(row=3, column=1)

button_vymery.grid(row=0, column=2)
button_obcanu.grid(row=1, column=2)
button_skol.grid(row=2, column=2)
button_celkem_obcanu.grid(row=3, column=2)

label_vymery.grid(row=4, column=1)
label_obcanu.grid(row=5, column=1)
label_skol.grid(row=6, column=1)
label_celkoveho_podilu.grid(row=7, column=1)


root.mainloop()
