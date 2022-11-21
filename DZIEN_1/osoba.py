class Osoba:
    #opis stanu -> konstruktor klasy
    def __init__(self,imie,wiek,waga,wzrost):
        self.wzrost = wzrost
        self.waga = waga
        self.imie = imie
        self.wiek = wiek
        self.kolor_oczu = "brązowe"
        self.info()

    #zachowanie -> funkcje klasy -> metody
    def info(self):
        print("została utworzona nowa osoba.....")

    def dane_osoby(self):
        print(f"osoba -> imię: {self.imie}, kolor oczu: {self.kolor_oczu}")

    def wiekzaxlat(self,x):
        return self.wiek + x


os1 = Osoba("Jan",32,87,180)
os1.kolor_oczu = "niebieskie"
os1.dane_osoby()
dt = 7
print(f"wiek osoby za {dt} wynosi: {os1.wiekzaxlat(dt)} lat")

print("***************************")

os2 = Osoba("Olga",40,56,170)
os2.dane_osoby()
dt = 3
print(f"wiek osoby za {dt} wynosi: {os2.wiekzaxlat(dt)} lat")


class Pacjent(Osoba):
    def __init__(self,imie,wiek,waga,wzrost,nr_pacjenta,placowka,rodzaj_wizyty):
        super().__init__(imie,wiek,waga,wzrost)
        self.rodzaj_wizyty = rodzaj_wizyty
        self.placowka = placowka
        self.nr_pacjenta = nr_pacjenta


print("***************************")

pc1 = Pacjent("Cyryl",23,88,173,54545,"NZOZ Badacz","wizyta kontrolna")
pc1.dane_osoby()
wk = 20
print(f"wiek osoby za {wk} wynosi: {os2.wiekzaxlat(wk)} lat")






