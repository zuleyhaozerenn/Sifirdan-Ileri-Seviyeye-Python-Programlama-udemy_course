"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""

print("Harf notu hesaplama programına hoş geldiniz...")

print("Lütfen aşağıya sınav sonuçlarınızı giriniz.")

vize1 = int(input("Lütfen 1. vize sonucunuzu giriniz:"))
vize2 = int(input("Lütfen 2. vize sonucunuzu giriniz:"))
final = int(input("Lütfen final sonucunuzu giriniz:"))

print("Ortalamanız hesaplanıyor...")

ortalama = (vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40)

print("Sınav sonuçlarınıza göre ortalamanız: {} ".format(ortalama))

print("Harf notunuz hesaplanıyor...")

if(ortalama >= 90 ):
    print("Harf notunuz: AA")

elif(ortalama >= 85 ):
    print("Harf notunuz: BA")

elif(ortalama >= 80 ):
    print("Harf notunuz: BB")

elif(ortalama >= 75 ):
    print("Harf notunuz: CB")

elif(ortalama >= 70 ):
    print("Harf notunuz: CC")

elif(ortalama >= 65 ):
    print("Harf notunuz: DC")

elif(ortalama >= 60 ):
    print("Harf notunuz: DD")

elif(ortalama >= 55 ):
    print("Harf notunuz: FD")

elif(ortalama >= 55 ):
    print("Harf notunuz: FF")

else :
    print("Dersten kaldınız..")

