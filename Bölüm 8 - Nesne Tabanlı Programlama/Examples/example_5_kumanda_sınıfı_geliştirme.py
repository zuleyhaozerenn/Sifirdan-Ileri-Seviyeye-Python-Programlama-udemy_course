import random
import time

class Kumanda():
    def __init__(self,tv_durumu = "Kapalı",tv_ses = 0,kanal_listesi = ["TRT"],kanal = "TRT"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_aç(self):
        if(self.tv_durumu == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durumu = "Açık"

    def tv_kapat(self):
        if(self.tv_durumu == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durumu = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi arrtırmak için: '>', Sesi azaltmak için: '<', Çıkış yapmak için: 'çıkış' yazınız.")
            if(cevap == ">"):
                if(self.tv_ses != 31):
                    print("Ses arttırılıyor...")
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            elif(cevap == "<"):
                if(self.tv_ses != 0):
                    print("Ses düşürülüyor...")
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif(cevap == "çıkış"):
                print("Çıkış Yaplıyor...")
                print("Güncel ses:",self.tv_ses)
                break
            else:
                print("Geçersiz işlem...")

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")

        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal başarıyla eklendi...")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Televizyonun güncel durumu:\nTelevizyon Durumu: {}\nSes Durumu: {}\nKanal Listesi: {}\nŞu anki Kanal: {}\n".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print("""
KUMANDA PROGRAMINA HOŞ GELDİNİZ...

İŞLEMLER:
1 - Televizyonu Açma
2 - Televizyonu Kapama
3 - Ses Ayarları
4 - Kanal Ekleme
5 - Kanal Sayısını Öğrenme
6 - Rastgele Kanala Geçme
7 - Televizyonun Güncel Bilgileri
q - Programdan çıkış

""")

while True:
    işlem = input("Lütfen yapmak istediğiniz işlemi giriniz:")
    if(işlem == "q"):
        print("Programdan çıkış yapılıyor...\nİyi günler dileriz...\n")
        break

    elif(işlem == "1"):
        kumanda.tv_aç()

    elif(işlem == "2"):
        kumanda.tv_kapat()

    elif(işlem == "3"):
        kumanda.ses_ayarları()

    elif(işlem == "4"):
        kanal_isimleri = input("Lütfen kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
        print("Güncel kanal listesi:",kanal_listesi)

    elif(işlem == "5"):
        print("Kanal Sayısı:",len(kumanda))

    elif(işlem == "6"):
        kumanda.rastgele_kanal()

    elif(işlem == "7"):
        print(kumanda)

    else:
        print("Geçersiz işlem girdiniz. Lütfen tekrar deneyiniz.")