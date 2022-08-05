class Çalışan():
    def __init__(self,isim,soyisim,maaş,departman):
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_göster(self):
        print("Çalışanın bilgileri:")
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim,self.soyisim,self.maaş,self.departman))

    def departman_değiştir(self,yeni_departman):
        print("Departman değiştiriliyor...")
        self.departman = yeni_departman
        print("Çalışanın yeni departmanı: ",self.departman)

class Yönetici(Çalışan):
    def zam_yap(self,zam_miktarı):
        print("Zam yapılıyor...")
        self.maaş += zam_miktarı
        print("Çalışanın yeni maaşı: ",self.maaş)

class Yönetici2(Çalışan):
    pass

yönetici1 = Yönetici("a","b",3000,"c")
yönetici1.bilgileri_göster()
yönetici1.zam_yap(500)
yönetici1.bilgileri_göster()
