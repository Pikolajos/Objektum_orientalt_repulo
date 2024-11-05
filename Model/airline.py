class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def jarat_lista(self):
        return [jarat.jarat_info() for jarat in self.jaratok]