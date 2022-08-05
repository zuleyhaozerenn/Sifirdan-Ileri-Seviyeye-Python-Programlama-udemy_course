class Araba():
    def __init__(self, model = "Bilgi Yok", renk = "Bilgi Yok", beygir_gücü = "Bilgi Yok"):
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü

araba1 = Araba(model = "Renault Megane",beygir_gücü = 110)
araba2 = Araba(renk = "Gümüş", beygir_gücü = 90)
araba3 = Araba (model = "Peugeot 301",renk = "Siyah")


print("Birinci arabanın özellikleri:\n"
      "Model: {}\n"
      "Renk: {}\n"
      "Beygir gücü: {}\n".format(araba1.model,araba1.renk,araba1.beygir_gücü))

print("İkinci arabanın özellikleri:\n"
      "Model: {}\n"
      "Renk: {}\n"
      "Beygir gücü: {}\n".format(araba2.model,araba2.renk,araba2.beygir_gücü))

print("Üçüncü arabanın özellikleri:\n"
      "Model: {}\n"
      "Renk: {}\n"
      "Beygir gücü: {}\n".format(araba3.model,araba3.renk,araba3.beygir_gücü))
