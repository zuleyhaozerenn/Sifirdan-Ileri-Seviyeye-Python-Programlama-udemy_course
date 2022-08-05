print("init metodu")
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        print("Kitap objesi oluşturuluyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür

kitap = Kitap("Budala","Dostoyevski",779,"Klasik")

print("")
print("str metodu")
class Kitap2(Kitap):
    def __init__(self, isim, yazar, sayfa_sayısı, tür):
        super().__init__(isim,yazar,sayfa_sayısı,tür)
    def __str__(self):
        return "İsim:{} \nYazar: {}\nSayfa Sayısı: {}\nTür: {}\n".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)

kitap2 = Kitap2("a","b",5,"c")
print(kitap2)

print("")
print("len metodu")

class Kitap3(Kitap2):
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        super().__init__(isim,yazar,sayfa_sayısı,tür)

    def __str__(self):
        super().__str__()

    def __len__(self):
        return self.sayfa_sayısı

kitap3 = Kitap3("e","f",10,"g")
print(len(kitap3))

print("")
print("del metodu")

class Kitap4(Kitap3):
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        super().__init__(isim,yazar,sayfa_sayısı,tür)

    def __str__(self):
        super().__str__()

    def __len__(self):
        return self.sayfa_sayısı

    def __del__(self):
        print("Kitap objesi siliniyor...")

kitap4 = Kitap4("k","l",50,"m")
del kitap4