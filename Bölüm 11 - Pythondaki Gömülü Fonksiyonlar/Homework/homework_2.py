"""
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın,
Sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]
"""


def üçgen(demet):
    kenar1 = demet[0]
    kenar2 = demet[1]
    kenar3 = demet[2]
    for i in liste:
        if((abs(kenar1 + kenar2) > kenar3) and (abs(kenar2+kenar3) > kenar1) and (abs(kenar1 + kenar3) > kenar2)):
            return True
        return False

liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(üçgen,liste)))
