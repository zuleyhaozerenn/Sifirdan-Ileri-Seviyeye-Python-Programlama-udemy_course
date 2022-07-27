"""
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik.
Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan
sadece çift sayıları bir listeye atmayı yapmayı çalışın.
"""

liste = list(range(1,101))
liste2 = list()

for i in liste:
    if(i % 2 == 0):
        liste2.append(i)
        continue
print(liste2)

liste2 = [ x for x in liste if x %2== 0]
print(liste2)