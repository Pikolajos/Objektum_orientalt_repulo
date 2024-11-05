from Model.flight import Jarat


class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def foglalas_hozzaadasa(self, jarat, utas_nev):
        # Ellenőrizzük, hogy a járat elérhető-e
        if isinstance(jarat, Jarat):
            foglalas_ar = jarat.jegyar
            self.foglalasok.append({"utas_nev": utas_nev, "jarat": jarat.jarat_info(), "ar": foglalas_ar})
            return foglalas_ar  # Visszaadjuk a foglalás árát
        else:
            return "Ez a járat nem elérhető!"

    def foglalas_lemondasa(self, utas_nev, jarat_szam):
        # Keresünk létező foglalást az utasnév és járatszám alapján
        for i, foglalas in enumerate(self.foglalasok):
            if foglalas["utas_nev"] == utas_nev and jarat_szam in foglalas["jarat"]:
                del self.foglalasok[i]
                return "Foglalás sikeresen törölve."
        return "Foglalás nem található."

    def foglalas_lista(self):
        return self.foglalasok if self.foglalasok else "Nincs elérhető foglalás."
