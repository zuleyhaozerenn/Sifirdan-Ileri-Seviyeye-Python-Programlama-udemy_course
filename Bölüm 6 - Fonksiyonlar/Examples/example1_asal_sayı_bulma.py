def asal(sayı):
    if (sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range (2, sayı):
            if(sayı % i == 0):
                return False
        return True

while True:
    sayı = input("Lütfen sayı giriniz. Programdan çıkış yapmak için 'q'ya tıklayınız.")
    if(sayı == "q"):
        print("Programdan çıkış yapılıyor...")
        break
    else:
        sayı = int(sayı)
        if(asal(sayı)):
            print("Girdiğiniz sayı asal sayıdır.")

        else:
            print("Girdiğiniz sayı asal bir sayı değildir.")
