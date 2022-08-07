"""
"futbolcular.txt" şeklinde bir dosya oluşturun.
İçine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin.
Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //
"""
def takım_bulma(satır):
    global takım
    satır = satır[:-1]
    liste = satır.split(",")
    takım = liste[1]
    return takım
with open("Futbolcular.txt","r",encoding="utf-8") as file:
    Fenerbahçe = []
    Galatasaray = []
    Beşiktaş = []
    for i in file:
        takım_bulma(i)
        if(takım == " Fenerbahçe"):
            Fenerbahçe.append(i)
        elif (takım == " Galatasaray"):
            Galatasaray.append(i)
        elif (takım == " Beşiktaş"):
            Beşiktaş.append(i)

    with open("Fenerbahçe.txt","w",encoding="utf-8") as file2:
        for i in Fenerbahçe:
            file2.write(i)

    with open("Galatasaray.txt","w",encoding="utf-8") as file3:
        for i in Galatasaray:
            file3.write(i)

    with open("Beşiktaş.txt","w",encoding="utf-8") as file4:
        for i in Beşiktaş:
            file4.write(i)