"""
Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın.
Bu yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.
"""
import homework2_modul
import time

print("Lütfen hesaplamak istediğiniz hesaplama çeşidini seçiniz.")
print("İşlemler:\n"
      "1 - Karekök alma\n"
      "2 - Üs alma\n"
      "3 - Faktöriyel hesaplama\n"
      "4 - Kombinasyon hesaplama\n"
      "5 - Permütasyon hesaplama\n"
      " q - Çıkış\n")


while True:
      islem = input("İşleminiz:")
      if(islem == "q"):
            print("Programdan çıkış yapılıyor... ")
            time.sleep(1)
            print("İyi günler dileriz..")
            break
      elif(islem == "1"):
            sayı = int(input("Lütfen karekökünü almak istediğiniz sayıyı giriniz:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            homework2_modul.karekok(sayı)
      elif (islem == "2"):
            sayı = int(input("Lütfen üs almak istediğiniz sayıyı giriniz:"))
            üs = int(input("Lütfen üs değerini giriniz:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            homework2_modul.üs(sayı,üs)
      elif (islem == "3"):
            sayı = int(input("Lütfen faktöriyelini hesaplamak istediğiniz sayıyı giriniz:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print("Sonuç:", homework2_modul.faktöriyel(sayı))
      elif (islem == "4"):
            sayı = int(input("Lütfen kombinasyon için eleman sayınızı giriniz:"))
            seçim = int(input("Lütfen kombinasyon için seçim sayınızı giriniz:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            homework2_modul.kombinasyon(sayı,seçim)
      elif (islem == "5"):
            sayı = int(input("Lütfen permütasyon için eleman sayınızı giriniz:"))
            seçim2 = int(input("Lütfen permütasyon için seçim sayınızı giriniz:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            homework2_modul.permütasyon(sayı,seçim2)
      else:
            print("Geçersiz işlem yaptınız.. Lütfen tekrar deneyiniz..")
            time.sleep(2)