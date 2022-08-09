"""
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
"""

with open("mailler_ve_kelimeler.txt","r",encoding="utf-8") as file:
    liste = file.readlines()
    liste2 = list()
    for i in liste:
        for x in i:
            if(x == "@"):
                liste2.append(i)
                with open("mailler.txt","w",encoding="utf-8") as file2:
                    for i in liste2:
                        file2.write(i)
