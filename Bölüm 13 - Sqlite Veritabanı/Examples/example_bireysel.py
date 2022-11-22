import sqlite3
import time
con = sqlite3.connect("kütüphane_bireysel.db")
cursor = con.cursor()

def tablo_oluşturma():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık_bireysel (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()

tablo_oluşturma()



def kitaplığa_kitap_ekleme(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık_bireysel VALUES (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def kütüphane_bilgileri():
    cursor.execute("Select * From kitaplık_bireysel")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def kitap_ismi_güncelleme(eski_isim,yeni_isim):
    cursor.execute("UPDATE kitaplık_bireysel set İsim = ? where İsim = ?",(yeni_isim,eski_isim))
    con.commit()

def yazar_ismi_güncelleme(eski_yazar,yeni_yazar):
    cursor.execute("UPDATE kitaplık_bireysel set Yazar = ? where Yazar = ?",(yeni_yazar,eski_yazar))
    con.commit()

def yayınevi_ismi_güncelleme(eski_yayınevi,yeni_yayınevi):
    cursor.execute("UPDATE kitaplık_bireysel set Yayınevi = ? where Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

def sayfa_sayısı_güncelleme(eski_sayfa_sayısı,yeni_sayfa_sayısı):
    cursor.execute("UPDATE kitaplık_bireysel set Sayfa_Sayısı = ? where Sayfa_Sayısı = ?",(yeni_sayfa_sayısı,eski_sayfa_sayısı))
    con.commit()

def kitap_silme(kitap):
    cursor.execute("DELETE FROM kitaplık_bireysel where İsim = ?",(kitap,))
    con.commit()



print("""
**************************

KÜTÜPHANE PROGRAMINA HOŞ GELDİNİZ...
Lütfen SQL programını hazırda bekletiniz..

Yapabileceğiniz işlemler:
1 - Kütüphaneye kitap ekleme
2 - Kütüphanedeki kitapları ve bilgilerini görme
3 - Bulunan kitabın ismini değiştirme
4 - Bulunan kitabın yazarını değiştirme
5 - Bulunan kitabın yayınevini değiştirme
6 - Bulunan kitabın sayfa sayısını değiştirme
7 - Kütüphaneden kitap silme
q - Programdan çıkış

********************************************
""")

while True:
    islem = input("Lütfen yapmak istediğiniz işlemin numarasını giriniz:")




    if (islem == '1'):

        print("Lütfen kütüphaneye eklemek istediğiniz kitabın bilgilerini giriniz:")
        isim = input("Kitabınızın ismi:")
        yazar = input("Kitabınızın yazarı:")
        yayınevi = input("Kitabınızın yayınevi:")
        sayfa_sayısı = int(input("Kitabınızın sayfa sayısı:"))
        kitaplığa_kitap_ekleme(isim, yazar, yayınevi, sayfa_sayısı)
        time.sleep(2)
        print("Kitabınız kütüphaneye eklenmiştir..")

    elif (islem == '2'):
        print("Kütüphanenizdeki kitaplar ve bilgileri:")
        kütüphane_bilgileri()

    elif(islem == '3'):
        eski_isim = input("Lütfen değiştirmek istediğiniz kitabın ismini giriniz:")
        yeni_isim = input("Lütfen kitabın yeni ismini giriniz:")
        print("Kitabın ismi güncelleniyor...")
        time.sleep(1)
        kitap_ismi_güncelleme(eski_isim,yeni_isim)
        print("Kitabınızın ismi güncellenmiştir. 2. seçeneği seçerek güncel kütüphanenizi görebilirsiniz.")

    elif (islem == '4'):
        eski_yazar = input("Lütfen değiştirmek istediğiniz kitabın yazarını giriniz:")
        yeni_yazar = input("Lütfen kitabın yeni yazarını giriniz:")
        print("Kitabın yazarı güncelleniyor...")
        time.sleep(1)
        yazar_ismi_güncelleme(eski_yazar, yeni_yazar)
        print("Kitabınızın yazarı güncellenmiştir. 2. seçeneği seçerek güncel kütüphanenizi görebilirsiniz.")

    elif (islem == '5'):
        eski_yayınevi = input("Lütfen değiştirmek istediğiniz kitabın yayınevini giriniz:")
        yeni_yayınevi = input("Lütfen kitabın yeni yayınevini giriniz:")
        print("Kitabın yayınevi güncelleniyor...")
        time.sleep(1)
        yayınevi_ismi_güncelleme(eski_yayınevi, yeni_yayınevi)
        print("Kitabınızın yayınevi güncellenmiştir. 2. seçeneği seçerek güncel kütüphanenizi görebilirsiniz.")

    elif (islem == '6'):
        eski_sayfa_sayısı = input("Lütfen değiştirmek istediğiniz kitabın sayfa sayısını giriniz:")
        yeni_sayfa_sayısı = input("Lütfen kitabın yeni sayfa sayısını giriniz:")
        print("Kitabın sayfa sayısı güncelleniyor...")
        time.sleep(1)
        sayfa_sayısı_güncelleme(eski_sayfa_sayısı, yeni_sayfa_sayısı)
        print("Kitabınızın sayfa sayısı güncellenmiştir. 2. seçeneği seçerek güncel kütüphanenizi görebilirsiniz.")

    elif ( islem == '7'):
        kitap = input("Lütfen silmek istediğiniz kitabın ismini giriniz:")
        print("Kitap, kütüphaneden kaldırılıyor..")
        time.sleep(1)
        kitap_silme(kitap)
        print("Kitap, kütüphaneden kaldırılmıştır. Kütüphanenizin güncel durumunu görmek için 2. seçeneği seçiniz.")

    elif (islem == '8'):
        ilk_kitabın_ismi = input("Değiştirmek istediğiniz kitabın ismini giriniz:")
        ikinci_kitabın_ismi = input("Hangi kitapla yer değiştirilmesini istiyorsunuz:")



    elif (islem == 'q'):
        print("Programdan çıkış yapılıyor...")
        time.sleep(1)
        print("İyi günler dileriz...")
        break

con.close()