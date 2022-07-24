""""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""

print("Lütfen aşağıya hipotenüs uzunluğunun bulunmasını istediğiniz dik üçgenin iki kenarını giriniz")

birinci_kenar = int(input("Lütfen birinci kenarı giriniz:"))
ikinci_kenar = int(input("Lütfen ikinci kenarı giriniz:"))

formül = birinci_kenar ** 2 + ikinci_kenar ** 2
hipotenüs_uzunluğu = formül ** 0.5

print("Hipotenüs uzunluğu hesaplanıyor...")

print("Girdiğiniz değerlere göre dik üçgeninizin hipotenüs uzunluğu : {} ".format(hipotenüs_uzunluğu))