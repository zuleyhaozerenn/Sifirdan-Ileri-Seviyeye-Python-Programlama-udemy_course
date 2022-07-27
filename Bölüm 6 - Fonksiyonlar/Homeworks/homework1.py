"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""

def mükemmel_sayı(sayı):
    liste = []
    toplam = 0
    i = 1
    while (i<sayı):
        if(sayı%i == 0):
            toplam += i
        i += 1
    if(toplam == sayı):
        liste.append(toplam)
        return True
    else:
        return False

for i in range(1,1001):
    if(mükemmel_sayı(i)):
        print("mükemmel sayı:",i)



