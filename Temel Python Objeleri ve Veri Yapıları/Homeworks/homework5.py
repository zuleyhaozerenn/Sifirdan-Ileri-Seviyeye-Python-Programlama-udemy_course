"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

print("Lütfen iki sayı giriniz.")

a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))

print("SAYILARINIZ: \n BİRİNCİ SAYI :{} \n İKİNCİ SAYI:{} \n".format(a,b))

print("Sayılar değiştiriliyor...")

a,b = b,a

print("Sayılarınızın son hali aşağıda bulunmaktadır.")

print("BİRİNCİ SAYI :{} \n İKİNCİ SAYI :{} \n".format(a,b))