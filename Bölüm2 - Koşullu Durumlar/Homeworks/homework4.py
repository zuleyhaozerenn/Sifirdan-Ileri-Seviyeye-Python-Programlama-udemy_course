"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""

şekil = input("Lütfen tipini bulmak istediğiniz şekli yazınız (Dikdörtgen / Üçgen):")

if(şekil == "Dikdörtgen"):
    print("Lütfen şeklinizin kenar uzunluklarını giriniz.")
    kenar1 = int(input("Birinci kenar uzunluğunuz:"))
    kenar2 = int(input("İkinci kenar uzunluğunuz:"))
    kenar3 = int(input("Üçüncü kenar uzunluğunuz:"))
    kenar4 = int(input("Dördüncü kenar uzunluğunuz:"))
    if(kenar1 == kenar2 == kenar3 == kenar4):
        print("Şekliniz karedir.")
    elif((kenar1 == kenar3 and kenar2 == kenar4) or (kenar2 == kenar1 and kenar3 == kenar4) or (kenar4 == kenar1 and kenar2 == kenar3)):
        print("Şekliniz dikdörtgendir.")
    else:
        print("Şekliniz dörtgendir.")

elif(şekil == "Üçgen"):
    print("Lütfen şeklinizin kenar uzunluklarını giriniz.")
    kenar1 = int(input("Birinci kenar uzunluğunuz:"))
    kenar2 = int(input("İkinci kenar uzunluğunuz:"))
    kenar3 = int(input("Üçüncü kenar uzunluğunuz:"))
    print("Girdiğiniz değerlere göre şeklinizin üçgen olup olmadığı kontrol ediliyor...")
    if((abs(kenar1 + kenar2) > kenar3) and (abs(kenar2+kenar3) > kenar1) and (abs(kenar1 + kenar3) > kenar2)):
        print("Şekliniz üçgendir.")
        if(kenar1 == kenar2 == kenar3):
            print("Şekliniz eşkenar üçgendir.")
        elif(kenar1 == kenar2 != kenar3 or kenar2 == kenar3 != kenar1 or kenar1 == kenar3 != kenar2):
            print("Şekliniz ikizkenar üçgendir.")
        else:
            print("Şekliniz normal bir üçgendir.")
    else:
        print("Şekliniz üçgen olmak için geçerli değerlere sahip değildir.")

else:
    print("Hata... Lütfen tekrar deneyiniz.")