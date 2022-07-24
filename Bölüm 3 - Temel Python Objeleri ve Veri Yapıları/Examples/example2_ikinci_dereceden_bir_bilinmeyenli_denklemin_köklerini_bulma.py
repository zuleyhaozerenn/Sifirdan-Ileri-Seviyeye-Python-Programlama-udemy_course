"""
İkinci dereceden bir bilinmeyenli denklemin köklerini bulma

denklem: ax^2+bx+c

deltayı hesaplama: b**2-4ac

birinci kök: (-b-delta**0.5) / 2*a
ikinci kök : (-b+delta**0.5) / 2*a
"""

print("Lütfen aşağıya çözülmesini istediğiniz ax^2+bx+c formatındaki ikinci dereceden bir bilinmeyenli denklemin a,b ve c değerlerini yazınız.")

a= int(input("Lütfen a değerini yazınız:"))
b= int(input("Lütfen b değerini yazınız:"))
c= int(input("Lütfen c değerini yazınız:"))

print("Verdiğiniz değerlere göre denklemin deltası hesaplanmaktadır...")

delta = b ** 2 - 4 * a * c

print(delta)

print("Verdiğiniz değerlere göre denklemin kökleri hesaplanmaktadır...")

kök1 = (- b - delta ** 0.5) / 2 * a
kök2 = (- b + delta ** 0.5) / 2 * a

print("Denklemin kökleri aşağıda bulunmaktadır.")

print("Birinci kök: {}\n İkinci kök: {}\n".format(kök1,kök2))
