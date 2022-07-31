"""
random ve time modülüyle sayı tahmin oyunu
"""

import random
import time

print("Sayı tahmin oyunu programına hoş geldiniz...")
print("Lütfen 1 ile 40 arasında bir sayı giriniz..")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    sayı_tahmini = int(input("Lütfen sayı giriniz:"))

    if(sayı_tahmini < rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Lütfen daha yüksek bir sayı giriniz...")
        tahmin_hakkı -= 1

    elif(sayı_tahmini > rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Lütfen daha düşük bir sayı giriniz...")
        tahmin_hakkı -=1

    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Sayıyı doğru tahmin ettiniz. Sayı:",rastgele_sayı)
        break

    if(tahmin_hakkı == 0):
        print("Tahmin hakkınız bitmiştir.. Sayı:",rastgele_sayı)
        break