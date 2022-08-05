class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller

    def bilgileri_göster(self):
        print("""
        Çalışan Bilgileri:
        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))

    def maasa_zam(self,zam_miktarı):
        print("Maaş yükseltiliyor...")
        self.maaş += zam_miktarı
        print("Maaşın son durumu:",self.maaş)

    def dil_ekleme(self,yeni_dil):
        print("Yeni dil ekleniyor...")
        self.diller.append(yeni_dil)
        print("Diller:",self.diller)


yazılımcı1 = Yazılımcı("Züleyha","Özeren",12345,3000,["C","Python","PHP","Java"])
yazılımcı1.bilgileri_göster()
yazılımcı1.maasa_zam(500)
yazılımcı1.dil_ekleme("C++")
yazılımcı1.bilgileri_göster()
