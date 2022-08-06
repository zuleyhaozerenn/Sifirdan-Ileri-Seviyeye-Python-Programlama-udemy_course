"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın.
Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün.
Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın.
Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın.
Liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""


def çift_mi(sayı):
    if(sayı % 2 == 0):
        return sayı
    else:
        raise ValueError

liste = (12,13,14,15,21,20,34,56)
liste_çift = list()

for i in liste:
    try:
        if(çift_mi(i)):
            liste_çift.append(i)
    except ValueError:
        pass


print(liste_çift)
