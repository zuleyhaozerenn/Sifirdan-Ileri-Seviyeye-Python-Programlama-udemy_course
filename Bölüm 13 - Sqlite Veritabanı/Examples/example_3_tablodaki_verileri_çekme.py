import sqlite3
con = sqlite3.connect("kütüphane3.db")
cursor = con.cursor()

def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık3 (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT) ")
    con.commit()

tablo()

def değer_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık3 VALUES (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

print("Tabloya eklemek istediğiniz kitapların bilgilerini giriniz:")
isim = input("İsim:")
yazar = input("Yazar:")
yayınevi = input("Yayınevi:")
sayfa_sayısı = int(input("Sayfa Sayısı:"))

değer_ekle(isim,yazar,yayınevi,sayfa_sayısı)
print("Kitap, tabloya eklenmiştir..")


def değerleri_gösterme():
    cursor.execute("Select * From kitaplık3")
    data = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri:")
    for i in data:
        print(i)

print("Tabloya eklediğiniz veriler aşağıda yer almaktadır:")
değerleri_gösterme()
con.close()