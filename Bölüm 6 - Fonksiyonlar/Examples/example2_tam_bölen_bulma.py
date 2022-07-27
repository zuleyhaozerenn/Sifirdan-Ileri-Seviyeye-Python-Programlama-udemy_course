def tam_bölen(sayı):
    liste = []
    for i in range(2,sayı):
        if(sayı % i == 0):
            liste.append(i)
    return liste

while True:
    sayı = input("Lütfen tam bölenlerini bulmak istediğiniz sayıyı giriniz. Programdan çıkış yapmak istiyorsanız 'q'ya basınız.")
    if(sayı == "q"):
        print("Programdan çıkış yapılıyor..")
        break
    else:
        sayı = int(sayı)
        print("Sayınızın tam bölenleri: " ,tam_bölen(sayı))


