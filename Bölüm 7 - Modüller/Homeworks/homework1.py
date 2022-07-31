"""
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.
"""

print("Hesap makinesi programına hoş geldiniz..")
import math

print("Hesaplamalar:\n"
      "1 - arccos hesaplama\n"
      "2 - arcsin hesaplama\n"
      "3 - arctan hesaplama\n"
      "4 - tan hesaplama\n"
      "5 - ondalık sayıyı kendinden bir önceki tam sayıya çevirme\n"
      "6 - kombinasyon hesaplama\n"
      "7 - cos hesaplama\n"
      "8 - faktöriyel hesaplama\n"
      "9 - ondalık sayıyı kendinden bir sonraki tam sayıya çevirme\n"
      "10 - logaritma hesaplama\n"
      "11 - 10 tabanındaki logaritmayı hesaplama\n"
      "12 - 2 tabanındaki logaritmayı hesaplama\n"
      "13 - permütasyon hesaplama\n"
      "14 - üs hesaplama\n"
      "15 - sin hesaplama\n"
      "16 - karekök hesaplama\n")

print("Programdan çıkmak için 'q'ya basınız...")

print("Lütfen hesaplama yapmak istediğiniz işlemi seçiniz.")

while True:
    islem = input("İşlem:")
    if(islem == "q"):
        print("Programdan çıkış yapılıyor...")
        break
    if (islem == "1"):
        sayı = int(input("Lütfen arccosunu almak istediğiniz açıyı giriniz:"))
        arccos = math.acos(sayı)
        print("İşleminizin sonucu:", arccos)
    elif (islem == "2"):
        sayı = int(input("Lütfen arcsini almak istediğiniz açıyı giriniz:"))
        arcsin = math.asin(sayı)
        print("İşleminizin sonucu:", arcsin)
    elif (islem == "3"):
        sayı = int(input("Lütfen arctanı almak istediğiniz açıyı giriniz:"))
        arctan = math.atan(sayı)
        print("İşleminizin sonucu:", arctan)
    elif (islem == "4"):
        sayı = int(input("Lütfen bir önceki tan almak istediğiniz açıyı giriniz:"))
        tan = math.tan(sayı)
        print("İşleminizin sonucu:", tan)
    elif (islem == "5"):
        sayı = float(input("Lütfen bir önceki tam sayıya çevirmek istediğiniz ondalık sayıyı giriniz:"))
        tam_sayı = math.ceil(sayı)
        print("İşleminizin sonucu:", tam_sayı)
    elif (islem == "6"):
        sayı = int(input("Lütfen eleman sayısı giriniz:"))
        sayı2 = int(input("Lütfen seçim sayısını giriniz:"))
        kombinasyon = math.comb(sayı, sayı2)
        print("İşleminizin sonucu:", kombinasyon)
    elif (islem == "7"):
        sayı = int(input("Lütfen cos almak istediğiniz açıyı giriniz:"))
        cos = math.cos(sayı)
        print("İşleminizin sonucu:", cos)
    elif (islem == "8"):
        sayı = int(input("Lütfen faktöriyelini hesaplamak istediğiniz sayıyı giriniz:"))
        faktöriyel = math.factorial(sayı)
        print("İşleminizin sonucu:", faktöriyel)
    elif (islem == "9"):
        sayı = float(input("Lütfen bir sonraki tam sayıya çevirmek istediğiniz ondalık sayıyı giriniz:"))
        tam_sayı2 = math.floor(sayı)
        print("İşleminizin sonucu:", tam_sayı2)
    elif (islem == "10"):
        sayı = int(input("Lütfen logaritmasını hesaplamak istediğiniz sayıyı giriniz:"))
        taban = int(input("Lütfen logaritmanızın tabanını giriniz:"))
        logaritma = math.log(sayı,taban)
        print("İşleminizin sonucu:", logaritma)
    elif (islem == "11"):
        sayı = int(input("Lütfen 10 tabanında olan logaritmanızı giriniz:"))
        logaritma2 = math.log10(sayı)
        print("İşleminizin sonucu:", logaritma2)
    elif (islem == "12"):
        sayı = int(input("Lütfen 2 tabanında olan logaritmanızı giriniz:"))
        logaritma3 = math.log2(sayı)
        print("İşleminizin sonucu:", logaritma3)
    elif (islem == "13"):
        sayı = int(input("Lütfen n değerinizi giriniz:"))
        sayı2 = int(input("Lütfen k değerinizi giriniz:"))
        permütasyon = math.perm(sayı,sayı2)
        print("İşleminizin sonucu:", permütasyon)
    elif (islem == "14"):
        sayı = int(input("Lütfen üssünü hesaplama istediğiniz sayıyı giriniz:"))
        sayı2=int(input("Lütfen üs değerinizi giriniz:"))
        üs = math.pow(sayı,sayı2)
        print("İşleminizin sonucu:", üs)
    elif (islem == "15"):
        sayı = int(input("Lütfen hesaplamak istediğiniz sin açısını giriniz:"))
        sin = math.sin(sayı)
        print("İşleminizin sonucu:", sin)
    elif (islem == "16"):
        sayı = int(input("Lütfen karekökünü bulmak istediğiniz sayıyı giriniz:"))
        karekök = math.sqrt(sayı)
        print("İşleminizin sonucu:", karekök)
    else:
        print("Geçersiz işlem girdiniz. Lütfen tekrar deneyiniz...")























