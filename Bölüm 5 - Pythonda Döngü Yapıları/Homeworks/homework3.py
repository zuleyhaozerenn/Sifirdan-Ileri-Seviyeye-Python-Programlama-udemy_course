"""
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
Bu işlemi continue ile yapmaya çalışın.
"""

liste = list(range(1,101))

for i in liste:
    if(i % 3 == 0):
        print(i)
        continue
