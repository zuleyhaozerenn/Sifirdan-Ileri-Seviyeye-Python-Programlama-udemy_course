"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""

print("Mükemmel sayı bulma programına hoş geldiniz. ")
print("Lütfen aşağıya mükemmel sayı olup olmadığını kontrol etmek istediğiniz sayıyı giriniz.")

i = 1
toplam = 0
sayı = int(input("Sayınız:"))

while (i<sayı):
    if(sayı % i == 0):
        toplam += i
    i += 1

if(sayı == toplam):
    print("Sayınız mükemmel sayıdır.")
else:
    print("Sayınız mükemmel sayı değildir.")


