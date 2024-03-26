import tkinter as tk
import webbrowser
from tkinter import ttk


def format_number_with_spaces(number):
    str_number = str(number)

    integer_part, decimal_part = (
        str_number.split(".") if "." in str_number else (str_number, "")
    )

    integer_part_with_spaces = " ".join(
        integer_part[::-1][i : i + 3] for i in range(0, len(integer_part), 3)
    )[::-1]

    formatted_number = integer_part_with_spaces + (
        "," + decimal_part if decimal_part else ""
    )

    return formatted_number


class PodilObceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulačka RUD pro rok 2023")

        # povolení pouze číselného vstupu
        self.validate_command = root.register(self.validate_input)

        self.primary_frame = tk.LabelFrame(
            root,
            text="Výpočet",
            font=("Helvetica", 12, "bold"),
        )
        self.primary_frame.pack(side="left", fill="y", expand=True)
        self.secondary_frame = tk.LabelFrame(
            root,
            text="Info",
            font=("Helvetica", 12, "bold"),
        )
        self.secondary_frame.pack(side="right", fill="y", expand=True)

        self.info_label = tk.Label(
            self.secondary_frame,
            text="Souhrnná data obcí ČR bez Prahy, Brna, Ostravy a Plzně pro rok 2023: \n* počet občanů (k 1.1.2023): 8 609 358,\n* katastrální výměra (k 1.1.2023): 7 569 130 ha,\n* počet žáků škol (k 30.9.2022): 1 071 167,\nvyužívána k výpočtu jsou zadána přímo v kódu aplikace.\nVstupní hodnotou pro výpočet koeficientu je počet občanů obce.Parametry vaší obce najdete v tabulce o procentím podílu obcí Ministerstva financí ČR.Použité vzorce vycházejí ze zákona č. 243/2000 Sb. o rozpočtovém určení výnosů a jsou také uvedeny v dokumentaci k aplikaci.\n\nKalkulačka RUD obcí pro rok 2023.\nParametry vaší obce najdete v tabulce o procentím podílu obcí Ministerstva financí ČR.",
            justify="left",
            wraplength=300,
        )
        self.info_label.pack(anchor="w")

        info_text = ""
        info_text += ""
        info_text += "Tyto tabulky naleznete na odkazu https://www.mfcr.cz/cs/kontrola-a-regulace/legislativa/legislativni-dokumenty s názvem Tabulka o procentím podílu obcí.\n"
        info_text += "Veškeré výpočty naleznete ve zdrojovém kódu této aplikace. Detailní vysvětlení výpočtů naleznete v dokumentaci k této apliakci. Výpočty obsahují data z roku 2023.\n"
        info_label = tk.Label(
            self.secondary_frame, text=info_text, wraplength=400, justify="left"
        )
        info_label.bind("<Button-1>", lambda e: self.open_link())
        info_label.pack(pady=(20, 0))

        #
        self.frame_vymery = tk.LabelFrame(
            self.primary_frame,
            text="Výměra obce v ha",
            font=("Helvetica", 10, "bold"),
        )
        self.frame_obcanu = tk.LabelFrame(
            self.primary_frame,
            text="Počet obyvatel obce",
            font=("Helvetica", 10, "bold"),
        )
        self.frame_skol = tk.LabelFrame(
            self.primary_frame,
            text="Počet žáků školy",
            font=("Helvetica", 10, "bold"),
        )
        self.frame_koeficient = tk.LabelFrame(
            self.primary_frame,
            text="Koeficient obce",
            font=("Helvetica", 10, "bold"),
        )
        self.frame_vymery.grid(row=0, column=0, padx=5)
        self.frame_obcanu.grid(row=1, column=0, padx=5)
        self.frame_skol.grid(row=2, column=0, padx=5)
        self.frame_koeficient.grid(row=3, column=0, padx=5)

        self.koeficient_label = tk.Label(
            self.frame_koeficient,
            text="",
            font=("Helvetica", 10, "bold"),
        )
        self.koeficient_label.grid(row=2, column=0, padx=10, columnspan=2)

        self.entry_vymery = ttk.Entry(
            self.frame_vymery,
            validate="key",
            validatecommand=(self.validate_command, "%P"),
        )
        self.entry_obcanu = ttk.Entry(
            self.frame_obcanu,
            validate="key",
            validatecommand=(self.validate_command, "%P"),
        )
        self.entry_skol = ttk.Entry(
            self.frame_skol,
            validate="key",
            validatecommand=(self.validate_command, "%P"),
        )
        self.entry_koeficient = ttk.Entry(
            self.frame_koeficient,
            validate="key",
            validatecommand=(self.validate_command, "%P"),
        )

        self.entry_vymery.grid(row=0, column=0, padx=10)
        self.entry_obcanu.grid(row=0, column=0, padx=10)
        self.entry_skol.grid(row=0, column=0, padx=10)
        self.entry_koeficient.grid(row=0, column=0, padx=10)

        # Výměry
        button_vymery = ttk.Button(
            self.frame_vymery, text="OK", command=self.vypocet_vymery
        )
        button_vymery.grid(row=0, column=1, padx=10, pady=(0, 10))

        # Obyvatelé
        button_obcanu = ttk.Button(
            self.frame_obcanu, text="OK", command=self.vypocet_obcanu
        )
        button_obcanu.grid(row=0, column=1, padx=10, pady=(0, 10))

        # Školy
        button_skol = ttk.Button(self.frame_skol, text="OK", command=self.vypocet_skol)
        button_skol.grid(row=0, column=1, padx=10, pady=(0, 10))

        # Koeficient
        # button_koeficient = ttk.Button(
        #     self.frame_koeficient, text="OK", command=self.vypocet_koeficient
        # )
        # button_koeficient.grid(row=0, column=1, padx=10, pady=(0, 10))

        button_soucet = ttk.Button(
            self.primary_frame, text="Provést výpočet", command=self.provest_soucet
        )
        button_soucet.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.vymery_ok = tk.Label(
            self.frame_vymery,
            text="",
            font=("Helvetica", 10, "bold"),
        )
        self.vymery_ok.grid(row=0, column=2, padx=10)

        self.obcani_ok = tk.Label(
            self.frame_obcanu,
            text="",
            font=("Helvetica", 10, "bold"),
        )
        self.obcani_ok.grid(row=0, column=2, padx=10)

        self.skoly_ok = tk.Label(
            self.frame_skol,
            text="",
            font=("Helvetica", 10, "bold"),
        )
        self.skoly_ok.grid(row=0, column=2, padx=10)

        self.koeficient_ok = tk.Label(
            self.frame_koeficient,
            text="",
            font=("Helvetica", 10, "bold"),
        )
        self.koeficient_ok.grid(row=0, column=2, padx=10)

        self.label_celkem = tk.Label(
            self.primary_frame,
            text="",
            font=("Helvetica", 16, "bold"),
            fg="green",
        )
        self.label_celkem.grid(
            row=5, column=0, columnspan=3, padx=10, pady=10, sticky="ew"
        )

        self.vysledek0 = 0
        self.vysledek1 = 0
        self.vysledek2 = 0
        self.novy_vysledek = 0

        # Propojení kláves Enter s funkcemi pro každé pole
        self.entry_vymery.bind("<Return>", lambda event: self.vypocet_vymery())
        self.entry_obcanu.bind("<Return>", lambda event: self.vypocet_obcanu())
        self.entry_skol.bind("<Return>", lambda event: self.vypocet_skol())
        self.entry_koeficient.bind("<Return>", lambda event: self.vypocet_koeficient())

    def validate_input(self, new_text):
        if new_text == "":
            return True
        try:
            float(new_text)
            return True
        except ValueError:
            return False

    def vypocet_vymery(self):
        try:
            zadana_hodnota = float(self.entry_vymery.get())
            self.vysledek0 = (zadana_hodnota / 7569130.6542) * 0.03 * 100
            if self.vysledek0 != 0:
                self.zobraz_vysledek(self.vymery_ok, "✔️", color="green")
            else:
                self.zobraz_vysledek(self.vymery_ok, "❌", color="red")
        except ValueError:
            self.zobraz_error("❌Zadejte platnou číselnou hodnotu výměry.")

    def vypocet_obcanu(self):
        try:
            zadana_hodnota = float(self.entry_obcanu.get())
            self.vysledek1 = (zadana_hodnota / 8609358) * 0.10 * 100
            if self.vysledek1 != 0:
                self.zobraz_vysledek(self.obcani_ok, "✔️", color="green")
            else:
                self.zobraz_vysledek(self.obcani_ok, "❌", color="red")

            self.entry_koeficient.delete(0, tk.END)
            self.entry_koeficient.insert(0, str(int(zadana_hodnota)))
            # Automatický výpočet koeficientu
            self.vypocet_koeficient()
        except ValueError:
            self.zobraz_error("❌Zadejte platnou číselnou hodnotu obyvatel.")

    def vypocet_skol(self):
        try:
            zadana_hodnota = float(self.entry_skol.get())
            self.vysledek2 = (zadana_hodnota / 1071167) * 0.09 * 100
            if self.vysledek2 != 0:
                self.zobraz_vysledek(self.skoly_ok, "✔️", color="green")
            else:
                self.zobraz_vysledek(self.skoly_ok, "❌", color="red")
        except ValueError:
            self.zobraz_error("❌Zadejte platnou číselnou hodnotu škol.")

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
                self.zobraz_error("❌Zadali jste neplatný počet občanů.")
                return

            self.novy_vysledek = (
                (vysledek / 9714289.9421) * 0.60948330 * 0.78 * 0.79 * 100
            )
            self.koeficient_label["text"] = str(round(self.novy_vysledek, 6)) + " %"
            if self.novy_vysledek != 0:
                self.zobraz_vysledek(self.koeficient_ok, "✔️", color="green")
            else:
                self.zobraz_vysledek(self.koeficient_ok, "❌", color="red")
        except ValueError:
            self.zobraz_error("❌Zadejte platnou celočíselnou hodnotu koeficientu.")

    def provest_soucet(self):
        soucet = self.vysledek0 + self.vysledek1 + self.vysledek2 + self.novy_vysledek
        vysledek_celkem = (soucet / 100) * 288111511594.68
        self.zobraz_vysledek(
            self.label_celkem,
            "Celkový výsledek je: {0} Kč".format(
                format_number_with_spaces(round(vysledek_celkem, 2))
            ),
            bold=True,
            color="green",
        )

    def open_link(self):
        webbrowser.open(
            "https://www.mfcr.cz/cs/kontrola-a-regulace/legislativa/legislativni-dokumenty"
        )

    def zobraz_vysledek(self, label, message, bold=False, color=None):
        label.config(text=message)
        if bold:
            label.config(font=("Helvetica", 16, "bold"))
        if color:
            label.config(fg=color)

    def zobraz_error(self, message):
        self.label_celkem.config(
            text="Chyba: " + message, fg="red", wraplength=self.root.winfo_width()
        )

    def ukoncit_program(self):
        self.root.destroy()


# Hlavní program
root = tk.Tk()
app = PodilObceGUI(root)
root.mainloop()
