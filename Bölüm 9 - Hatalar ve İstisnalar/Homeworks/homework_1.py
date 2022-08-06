"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
Bunu yaparken try,except bloklarını kullanmayı unutmayın.
"""

liste = ["345","sadas","324a","14","kemal"]


try:
    liste1 = []
    for i in liste:
        for x in i:
            if (x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9"):
                liste1.append(i)
                break

            else:
                continue
except:
    pass

finally:
    print(liste1)