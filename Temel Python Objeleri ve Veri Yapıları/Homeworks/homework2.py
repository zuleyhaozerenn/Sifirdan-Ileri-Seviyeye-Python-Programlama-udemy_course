"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

print("Beden Kitle İndeksi Hesaplama programına hoş geldiniz. Lütfen aşağıya kilonuzu ve boyunuzu giriniz.")

kilo = int(input("Kilonuz:"))
boy = int(input("Boyunuz:"))

Beden_kitle_indeksi = kilo / (boy * boy)

print("Girdiğiniz değerlere göre beden kitle indeksiniz: {}".format(Beden_kitle_indeksi))
