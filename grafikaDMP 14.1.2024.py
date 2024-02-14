import tkinter as tk
from tkinter import ttk

class PodilObceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Výpočet Podílu Obce na Sdílených Daních")

        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(4, weight=1)

        
        self.entry_vymery = ttk.Entry(root)
        self.entry_obcanu = ttk.Entry(root)
        self.entry_skol = ttk.Entry(root)
        self.entry_koeficient = ttk.Entry(root)

        self.entry_vymery.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.entry_obcanu.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.entry_skol.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.entry_koeficient.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Výměry
        button_vymery = ttk.Button(root, text="Výměra", command=self.vypocet_vymery)
        button_vymery.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Obyvatelé
        button_obcanu = ttk.Button(root, text="Obyvatelé", command=self.vypocet_obcanu)
        button_obcanu.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Školy
        button_skol = ttk.Button(root, text="Školy", command=self.vypocet_skol)
        button_skol.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Koeficient
        button_koeficient = ttk.Button(root, text="Koeficient", command=self.vypocet_koeficient)
        button_koeficient.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        
        button_soucet = ttk.Button(root, text="Provést součet", command=self.provest_soucet)
        button_soucet.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        
        self.label_vymery = tk.Label(root, text="", font=("Helvetica", 10, "bold"), wraplength=root.winfo_width())
        self.label_obcanu = tk.Label(root, text="", font=("Helvetica", 10, "bold"), wraplength=root.winfo_width())
        self.label_skol = tk.Label(root, text="", font=("Helvetica", 10, "bold"), wraplength=root.winfo_width())
        self.label_koeficient = tk.Label(root, text="", font=("Helvetica", 10, "bold"), wraplength=root.winfo_width())
        self.label_celkem = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="green", wraplength=root.winfo_width())

        self.label_vymery.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.label_obcanu.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.label_skol.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.label_koeficient.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.label_celkem.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        
        self.vysledek0 = 0
        self.vysledek1 = 0
        self.vysledek2 = 0
        self.novy_vysledek = 0

    def vypocet_vymery(self):
        try:
            zadana_hodnota = float(self.entry_vymery.get())
            self.vysledek0 = (zadana_hodnota / 7560277.4525) * 0.03 * 100
            self.zobraz_vysledek(self.label_vymery, "Výměru obce tvoří {:.9f}% podílu sdílených daní.".format(self.vysledek0))
        except ValueError:
            self.zobraz_error("Zadejte platnou číselnou hodnotu výměry.")

    def vypocet_obcanu(self):
        try:
            zadana_hodnota = float(self.entry_obcanu.get())
            self.vysledek1 = (zadana_hodnota / 8413311) * 0.10 * 100
            self.zobraz_vysledek(self.label_obcanu, "Počet občanů obce tvoří {:.9f}% podílu sdílených daní.".format(self.vysledek1))
        except ValueError:
            self.zobraz_error("Zadejte platnou číselnou hodnotu obyvatel.")

    def vypocet_skol(self):
        try:
            zadana_hodnota = float(self.entry_skol.get())
            self.vysledek2 = (zadana_hodnota / 1036513) * 0.09 * 100
            self.zobraz_vysledek(self.label_skol, "Počet dětí a žáků navštěvující obcí zřizovanou školu nebo školku tvoří {:.9f}% podílu sdílených daní.".format(self.vysledek2))
        except ValueError:
            self.zobraz_error("Zadejte platnou číselnou hodnotu škol.")

    def vypocet_koeficient(self):
        try:
            pocet_obcanu = int(self.entry_koeficient.get())
            if 51 <= pocet_obcanu <= 2000:
                vysledek = 50 + 1.0700 * (pocet_obcanu - 50)
            elif 2001 <= pocet_obcanu <= 30000:
                vysledek = 2136.5 + 1.1523 * (pocet_obcanu - 2000)
            elif 30001 <= pocet_obcanu <= 300000:
                vysledek = 34400.9 + 1.3663 * (pocet_obcanu - 30000)
            elif 0 <= pocet_obcanu <= 50:
                vysledek = 1.0000 * pocet_obcanu
            else:
                self.zobraz_error("Zadali jste neplatný počet občanů.")
                return

            self.novy_vysledek = (vysledek / 9484053.2589) * 0.61877832 * 0.78 * 0.79 * 100
            self.zobraz_vysledek(self.label_koeficient, "Výsledek výpočtu koeficientu je: {:.6f}%".format(self.novy_vysledek))
        except ValueError:
            self.zobraz_error("Zadejte platnou celočíselnou hodnotu koeficientu.")

    def provest_soucet(self):
        soucet = self.vysledek0 + self.vysledek1 + self.vysledek2 + self.novy_vysledek
        vysledek_celkem = (soucet / 100) * 247642301996.12
        self.zobraz_vysledek(self.label_celkem, "Celkový výsledek je: {:.2f} Kč".format(vysledek_celkem), bold=True, color="green")

    def zobraz_vysledek(self, label, message, bold=False, color=None):
        label.config(text=message)
        if bold:
            label.config(font=("Helvetica", 16, "bold"))
        if color:
            label.config(fg=color)
        label.config(wraplength=self.root.winfo_width())

    def zobraz_error(self, message):
        self.label_celkem.config(text="Chyba: " + message, fg="red", wraplength=self.root.winfo_width())

# Hlavní program
root = tk.Tk()
app = PodilObceGUI(root)
root.mainloop()
