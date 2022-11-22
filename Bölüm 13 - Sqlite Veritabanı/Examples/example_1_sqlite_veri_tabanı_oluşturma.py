import sqlite3
con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT) ")
    con.commit()

def deger_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES ('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', 561) ")
    con.commit()

deger_ekle()
con.close()