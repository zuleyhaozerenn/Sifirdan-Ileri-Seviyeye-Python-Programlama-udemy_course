try:
    a = int(input("Lütfen bir sayı giriniz:"))
    b = int(input("Lütfen ikinci bir sayı giriniz:"))
    print(a/b)

except ValueError:
    print("Value Error!")
    print("Lütfen girdiğiniz değerin sayı olduğundan emin olunuz...")

except ZeroDivisionError:
    print("Zero Division Error!")
    print("İkinci girdiğiniz sayının değeri 0 olamaz. Lütfen farklı bir değer giriniz.")

finally:
    print("İyi günler...")