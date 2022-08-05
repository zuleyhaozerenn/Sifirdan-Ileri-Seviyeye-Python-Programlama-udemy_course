"""super metodu"""


class Çalışan():
    def __init__(self, isim, soyisim, maaş, departman):
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.departman = departman

    def bilgileri_göster(self):
        print("Çalışanın bilgileri:")
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim, self.soyisim, self.maaş,
                                                                        self.departman))

    def departman_değiştir(self, yeni_departman):
        print("Departman değiştiriliyor...")
        self.departman = yeni_departman
        print("Çalışanın yeni departmanı: ", self.departman)


class Yönetici(Çalışan):
    def __init__(self, isim, soyisim, maaş, departman, sorumlu_olduğu_kişi_sayısı):
        super().__init__(isim,soyisim,maaş,departman)
        self.sorumlu_olduğu_kişi_sayısı = sorumlu_olduğu_kişi_sayısı

    def bilgileri_göster(self):
        print("Yöneticinin bilgileri:")
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\nDepartman: {}\nSorumlu olduğu kişi sayısı: {}\n".format(self.isim,self.soyisim,self.maaş,self.departman,self.sorumlu_olduğu_kişi_sayısı))

yönetici = Yönetici("a","b",3000,"c",50)
yönetici.bilgileri_göster()