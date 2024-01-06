class Obiekt:
    def __init__(self, co_to, mina, znak, status):
        self.co_to = co_to
        self.mina = mina
        self.znak = znak
        self.status = status

    def info1(self):
        print(f"{self.co_to} z {self.mina} i {self.znak} jest {self.status}")

ob1 = Obiekt("Postać", "uśmiechem", "koroną", "królem")
ob1.info1()

class Maszyna:
    def __init__(self,pojazd, koła, armata, wielkość):
        self.pojazd = pojazd
        self.koła = koła
        self.armata = armata
        self.wielkość = wielkość

    def info2(self):
        print(f"{self.pojazd} z {self.koła} koła i {self.armata} armata jest {self.wielkość}")

ob2 = Maszyna('Czołg', "3", "1", "mały")
ob2.info2()

class Technologia:
    def __init__(self,sprzęt, ekran, obudowa, myszka):
        self.sprzęt = sprzęt
        self.ekran = ekran
        self.obudowa = obudowa
        self.myszka = myszka

    def info3(self):
        print(f"{self.sprzęt} ma {self.ekran} ekran, {self.obudowa} obudowe i {self.myszka} myszka")

ob3 = Technologia("Laptop", "mały", "grubą", "brak")
ob3.info3()