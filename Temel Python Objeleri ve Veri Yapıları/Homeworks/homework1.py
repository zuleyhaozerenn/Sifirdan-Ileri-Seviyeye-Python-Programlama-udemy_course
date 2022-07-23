"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
"""
print("Lütfen çarpılmasını istediğiniz 3 sayıyı aşağıya giriniz.")

sayı1= int(input("Lütfen sayı giriniz:"))
sayı2= int(input("Lütfen sayı giriniz:"))
sayı3= int(input("Lütfen sayı giriniz:"))

print("Girdiğiniz sayıların çarpımı aşağıda bulunmaktadır.\n Sonuç:{}".format(sayı1*sayı2*sayı3))
