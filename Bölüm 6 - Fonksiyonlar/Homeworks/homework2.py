"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""


print("EBOB alma programına hoş geldiniz.")
print("Lütfen aşağıya iki adet sayı giriniz.")
a = int(input("Lütfen birinci sayınızı giriniz:"))
b = int(input("Lütfen ikinci sayınızı giriniz:"))

def ebob(a,b):
    def tam_bölen(sayı):
        liste = []
        for i in range(2, sayı):
            if (sayı % i == 0):
                liste.append(i)
        return liste
    liste1 = tam_bölen(a)
    liste2 = tam_bölen(b)
    liste3 = liste1 + liste2
    liste3.sort()
    while True:
        liste4 = []
        for i in liste3:
            if(liste3.count(i) == 2):
                liste4.append(i)
        break
    print("Girdiğiniz sayıların EBOB'u: ",max(liste4))

ebob(a,b)
