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


