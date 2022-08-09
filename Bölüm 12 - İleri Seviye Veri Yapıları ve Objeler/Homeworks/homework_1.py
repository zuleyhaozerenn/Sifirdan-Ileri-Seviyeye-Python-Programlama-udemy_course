"""
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""

s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frekans = dict()

for harf in s:
    if(harf in frekans):
        frekans[harf] += 1
    else:
        frekans[harf] = 1

for i, j in frekans.items():
    print(i , ":" , j)
