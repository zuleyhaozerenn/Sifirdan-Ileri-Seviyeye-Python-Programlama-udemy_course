"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi

"""

rakam = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onluk = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def sayının_okunuşu(sayı):
    sayı = int(sayı)
    birinci = sayı % 10
    ikinci = sayı // 10
    return onluk[ikinci] + " " + rakam[birinci]

sayı = input("Lütfen sayı giriniz:")
print(sayının_okunuşu(sayı))