"""
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""

def pisagor():
    liste = range(1,101)
    liste1 = []
    for i in liste:
        for j in liste:
            c = (i**2 + j**2) ** 0.5
            if( c == int(c )):
                liste1.append((i,j,int(c)))

    return liste1
for i in pisagor():
    print(i)