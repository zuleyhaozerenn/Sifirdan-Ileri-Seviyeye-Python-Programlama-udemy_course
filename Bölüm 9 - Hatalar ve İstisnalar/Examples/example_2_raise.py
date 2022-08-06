def ters_çevir(kelime):
    if(type(kelime) != str):
        raise ValueError("Lütfen string bir değer giriniz..")
    else:
        return kelime[: : -1]

print(ters_çevir("python"))
print(ters_çevir(12))