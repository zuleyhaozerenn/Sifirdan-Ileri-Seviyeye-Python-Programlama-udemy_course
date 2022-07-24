""""
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""

print("Lütfen aşağıya bilgilerinizi giriniz.")

ad = input("İsminiz:")
soyad = input("Soyadınız:")
numara = int(input("Numaranız:"))

print("Bilgiler kaydediliyor...\n \n \n")

print("Bilgiler kaydedildi. Bilgileriniz aşağıda bulunmaktadır.\n \n ")

print("KULLANICI BİLGİLERİ : \n AD: {} \n SOYAD: {} \n NUMARA: {} \n".format(ad,soyad,numara))
