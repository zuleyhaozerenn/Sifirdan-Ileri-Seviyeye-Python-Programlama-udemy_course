"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı
bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""

print("Aracınızın gittiğiniz süre boyunca ne kadar yaktığını öğrenmek istiyorsanız lütfen aşağıdaki bilgileri doldurun.")

yakılan_yakıt = int(input("Aracınız kilometrede ne kadar yakmaktadır:"))
yol_km = int(input("Kaç kilometre yol gittiniz:"))

para = yakılan_yakıt * yol_km

print("Girdiğiniz değerlere göre toplam ödemeniz gereken tutar: {}". format(para))
