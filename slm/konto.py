class Konto():
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo

    def wyplata(self,kwota):
        if kwota <= self.saldo:
            self.saldo = self.saldo - kwota
            return self.saldo
        else:
            return "no money"
    
    def wplata(self, kwota):
        self.saldo = self.saldo + kwota
        return self.saldo 
    
# konto1 = Konto(10000)

# konto1.wyplata(11000)
# print(konto1.saldo)

# konto1.wyplata(1000)
# print(konto1.saldo)

# konto1.wplata(10000)
# print(konto1.saldo)

