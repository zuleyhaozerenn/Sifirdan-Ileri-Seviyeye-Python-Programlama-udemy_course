"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""

print("Lütfen aşağıya sayılarınızı giriniz.")
sayı1 = float(input("Birinci sayı:"))
sayı2 = float(input("İkinci sayı:"))
sayı3 = float(input("Üçüncü sayı:"))

print("Girdiğiniz sayılar : {} , {} , {} ".format(sayı1,sayı2,sayı3))

print("Büyüklükler hesaplanıyor...")

if(sayı1 > sayı2 and sayı1 > sayı3):
    print("Girdiğiniz sayılar arasındaki en büyük sayı : {}".format(sayı1))

elif(sayı2 > sayı1 and sayı2 > sayı3):
    print("Girdiğiniz sayılar arasındaki en büyük sayı : {}".format(sayı2))

elif(sayı3 > sayı1 and sayı3 > sayı2):
    print("Girdiğiniz sayılar arasındaki en büyük sayı : {}".format(sayı3))

else:
    print("Hata.. Lütfen tekrar deneyiniz.")
