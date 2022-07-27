print(""""
ATM Programına hoş geldiniz..

Lütfen yapmak istediğiniz işlemi seçiniz:

1 - Bakiye Sorgulama
2 - Para Yatırma
3 - Para Çekme

Programdan çıkış yapmak için "q"ya tıklayınız.
""")

bakiye = 1000


while True:
    islem = input("İşleminiz:")
    if(islem == "q"):
        print("Programdan çıkış yapılıyor. İyi günler dileriz...")
        break
    elif(islem == "1"):
        print("Güncel bakiyeniz : {} ".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Lütfen yatırmak istediğiniz para miktarını giriniz:"))
        bakiye += miktar
        print("Güncel bakiyeniz : {} ".format(bakiye))
    elif(islem == "3"):
        çekilen = int(input("Çekmek istediğiniz para miktarını giriniz:"))
        if(bakiye - çekilen < 0 ):
            print("Bakiyeniz yetersizdir. Lütfen tekrar deneyiniz.")
            continue
        bakiye -= çekilen
        print("Güncel bakiyeniz: {} ".format(bakiye))
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyiniz...")


