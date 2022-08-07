def not_hesaplama(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    ortalama = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)
    if(ortalama >= 90):
        harf = "AA"
    elif(ortalama >= 85):
        harf = "BA"
    elif (ortalama >= 80):
        harf = "BB"
    elif (ortalama >= 75):
        harf = "CB"
    elif (ortalama >= 70):
        harf = "CC"
    elif (ortalama >= 65):
        harf = "DC"
    elif (ortalama >= 60):
        harf = "DD"
    elif (ortalama >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + " " + "-------->" + " " + harf + "\n"

with open("dosya.txt","r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        eklenecekler_listesi.append(not_hesaplama(i))

        with open("notlar.txt","w",encoding="utf-8") as file2:
            for i in eklenecekler_listesi:
                file2.write(i)

