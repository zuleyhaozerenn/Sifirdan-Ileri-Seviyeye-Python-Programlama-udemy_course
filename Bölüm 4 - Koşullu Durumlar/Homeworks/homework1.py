"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

print("Beden kitle indeksi hesaplama programına hoş geldiniz.")

boy = float(input("Lütfen boyunuzu metre cinsinden giriniz:"))
kilo = int(input("Lütfen kilonuzu giriniz:"))

sonuç = kilo / (boy * boy)

print("Beden kitle indeksiniz : {}".format(sonuç))

if(sonuç < 18.5 ):
    print("Beden kitle indeksinize göre zayıfsınız.")

elif(sonuç > 18.5 and sonuç < 25):
    print("Beden kitle indeksinize göre normal kilonuzdasınız.")

elif(sonuç > 25 and sonuç < 30 ):
    print("Beden kitle indeksinize göre fazla kilolusunuz.")

elif(sonuç > 30 ):
    print("Beden kitle indeksinize göre obezsiniz.")

else:
    print("Hata... Lütfen boyunuzu ve kilonuzu tekrardan giriniz..")

print("Beden kitle indeksiniz ne olursa olsun lütfen spor yapmayı ihmal etmeyin.")
