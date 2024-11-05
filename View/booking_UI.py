import tkinter as tk
from tkinter import messagebox

from Model.airline import LegiTarsasag
from Model.flight import BelfoldiJarat, NemzetkoziJarat
from Controller.ticket_booking import JegyFoglalas


class FoglalasiRendszerUI:
    def __init__(self, root, legitarsasag, foglalas_rendszer):
        self.legitarsasag = legitarsasag
        self.foglalas_rendszer = foglalas_rendszer
        self.root = root
        self.root.title("Repülőjegy Foglalási Rendszer")

        tk.Label(root, text="Járatok").grid(row=0, column=0, padx=10, pady=10)
        self.jaratok_lista = tk.Listbox(root, width=50, height=6)
        self.jaratok_lista.grid(row=1, column=0, padx=10, pady=10)
        self.update_jaratok()

        tk.Label(root, text="Utas neve").grid(row=2, column=0, padx=10, pady=5)
        self.utas_nev_entry = tk.Entry(root)
        self.utas_nev_entry.grid(row=3, column=0, padx=10, pady=5)

        tk.Button(root, text="Jegy foglalása", command=self.jegy_foglalasa).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(root, text="Foglalás lemondása", command=self.foglalas_lemondasa).grid(row=5, column=0, padx=10, pady=5)
        tk.Button(root, text="Foglalások listázása", command=self.foglalasok_listazasa).grid(row=6, column=0, padx=10, pady=5)

    def update_jaratok(self):
        self.jaratok_lista.delete(0, tk.END)
        for jarat in self.legitarsasag.jarat_lista():
            self.jaratok_lista.insert(tk.END, jarat)

    def jegy_foglalasa(self):
        utas_nev = self.utas_nev_entry.get()
        if not utas_nev:
            messagebox.showwarning("Hiba", "Adjon meg egy utas nevet!")
            return

        selected_index = self.jaratok_lista.curselection()
        if not selected_index:
            messagebox.showwarning("Hiba", "Válasszon ki egy járatot!")
            return

        jarat = self.legitarsasag.jaratok[selected_index[0]]
        ar = self.foglalas_rendszer.foglalas_hozzaadasa(jarat, utas_nev)
        messagebox.showinfo("Siker", f"Foglalás sikeres! Jegy ára: {ar} Ft")

    def foglalas_lemondasa(self):
        utas_nev = self.utas_nev_entry.get()
        selected_index = self.jaratok_lista.curselection()

        if not utas_nev or not selected_index:
            messagebox.showwarning("Hiba", "Adjon meg egy utas nevet és válasszon járatot!")
            return

        jarat_szam = self.legitarsasag.jaratok[selected_index[0]].jaratszam
        eredmeny = self.foglalas_rendszer.foglalas_lemondasa(utas_nev, jarat_szam)
        messagebox.showinfo("Foglalás Lemondása", eredmeny)

    def foglalasok_listazasa(self):
        foglalasok = self.foglalas_rendszer.foglalas_lista()
        if not foglalasok:
            messagebox.showinfo("Foglalások", "Nincsenek foglalások.")
        else:
            foglalasok_ablak = tk.Toplevel(self.root)
            foglalasok_ablak.title("Aktuális Foglalások")
            for foglalas in foglalasok:
                tk.Label(foglalasok_ablak, text=f"{foglalas['utas_nev']} - {foglalas['jarat']} - Ár: {foglalas['ar']} Ft").pack()

if __name__ == "__main__":
    root = tk.Tk()

    legitarsasag = LegiTarsasag("SkyTravel")
    legitarsasag.jarat_hozzaadasa(BelfoldiJarat("B123", "Budapest", 10000))
    legitarsasag.jarat_hozzaadasa(NemzetkoziJarat("N456", "London", 30000))
    legitarsasag.jarat_hozzaadasa(BelfoldiJarat("B789", "Debrecen", 8000))

    foglalas_rendszer = JegyFoglalas()
    foglalas_rendszer.foglalas_hozzaadasa(legitarsasag.jaratok[0], "Nagy István")
    foglalas_rendszer.foglalas_hozzaadasa(legitarsasag.jaratok[1], "Kis Béla")
    foglalas_rendszer.foglalas_hozzaadasa(legitarsasag.jaratok[2], "Nagy István")

    app = FoglalasiRendszerUI(root, legitarsasag, foglalas_rendszer)
    root.mainloop()
