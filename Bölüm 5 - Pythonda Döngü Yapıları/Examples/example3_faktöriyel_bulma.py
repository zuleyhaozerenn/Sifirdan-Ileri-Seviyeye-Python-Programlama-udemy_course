"""
Bir sayının faktöriyelini bulma
"""

print("Faktöriyel bulma programına hoş geldiniz. ")
print("Programdan çıkmak için 'q'ya basabilirsiniz.")

while True:
    sayı = input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz:")

    if(sayı == "q"):
        print("Programdan çıkış yapılıyor...")
        break

    else:
        sayı = int(sayı)
        faktöriyel = 1
        for i in range(2,sayı+1):
            faktöriyel *= i
        print("Girdiğiniz sayının faktöriyeli: ",faktöriyel)
    