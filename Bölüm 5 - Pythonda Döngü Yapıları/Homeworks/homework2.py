"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
"""
print("Girdiğiniz sayıları toplama programnına hoş geldiniz.")
print("Programdan çıkmak istiyorsanız 'q'ya basınız")

toplam = 0

while True:
    sayı = input("Lütfen sayı giriniz:")
    if(sayı == "q"):
        print("Programdan çıkış yapılıyor...")
        break

    sayı = int(sayı)
    toplam += sayı
    print("Girdiğiniz sayı : {} Girdiğiniz sayıların toplamı: {}".format(sayı,toplam))