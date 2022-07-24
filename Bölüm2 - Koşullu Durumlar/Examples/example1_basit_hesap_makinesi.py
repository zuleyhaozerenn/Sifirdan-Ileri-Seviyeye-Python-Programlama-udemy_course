print("Hesap makinesi programına hoş geldiniz...")
print("Lütfen yapmak istediğiniz işlemin numarasını giriniz. İşlemler ve numaraları:"
      "\n 1 - Toplama İşlemi"
      "\n 2 - Çıkarma İşlemi"
      "\n 3 - Çarpma İşlemi"
      "\n 4 - Bölme İşlemi")

işlem = int(input("İşlem numaranız:"))

if(işlem == 1):
    print("Seçtiğiniz işlem Toplama işlemidir.")
    print("Lütfen işlem yapmak istediğiniz sayıları giriniz.")
    sayı1 = int(input("Birinci sayınız:"))
    sayı2 = int(input("İkinci sayınız:"))
    sonuç = sayı1 + sayı2
    print("İşleminizin sonucu : {}".format(sonuç))

elif(işlem == 2):
    print("Seçtiğiniz işlem Çıkarma işlemidir.")
    print("Lütfen işlem yapmak istediğiniz sayıları giriniz.")
    sayı1 = int(input("Birinci sayınız:"))
    sayı2 = int(input("İkinci sayınız:"))
    sonuç = sayı1 - sayı2
    print("İşleminizin sonucu : {}".format(sonuç))

elif(işlem == 3):
    print("Seçtiğiniz işlem Çarpma işlemidir.")
    print("Lütfen işlem yapmak istediğiniz sayıları giriniz.")
    sayı1 = int(input("Birinci sayınız:"))
    sayı2 = int(input("İkinci sayınız:"))
    sonuç = sayı1 * sayı2
    print("İşleminizin sonucu : {}".format(sonuç))


elif(işlem == 4):
    print("Seçtiğiniz işlem Bölme işlemidir.")
    print("Lütfen işlem yapmak istediğiniz sayıları giriniz.")
    sayı1 = int(input("Birinci sayınız:"))
    sayı2 = int(input("İkinci sayınız:"))
    sonuç = sayı1 / sayı2
    print("İşleminizin sonucu : {}".format(sonuç))

else:
    print("Geçersiz işlem numarası girdiniz. Lütfen tekrar deneyiniz.")