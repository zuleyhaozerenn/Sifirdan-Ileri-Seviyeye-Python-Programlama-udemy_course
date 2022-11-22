import sqlite3
con = sqlite3.connect("kütüphane2.db")
cursor = con.cursor()

def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık2 (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT) ")
    con.commit()

def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık2 VALUES (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

print("Tabloya Eklemek İstediğiniz Kitapların Bilgilerini Giriniz...")
isim = input("İsim:")
yazar = input("Yazar:")
yayınevi = input("Yayınevi:")
sayfa_sayısı = int(input("Sayfa sayısı:"))


deger_ekle(isim,yazar,yayınevi,sayfa_sayısı)
con.close()

print("Kitap tabloya eklenmiştir..")