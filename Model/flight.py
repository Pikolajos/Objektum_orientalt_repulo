from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_info(self):
        pass

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar * 0.8)  # Olcsóbb jegyár

    def jarat_info(self):
        return f"Belföldi Járat - Szám: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar}"

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar * 1.5)  # Magasabb jegyár

    def jarat_info(self):
        return f"Nemzetközi Járat - Szám: {self.jaratszam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar}"
