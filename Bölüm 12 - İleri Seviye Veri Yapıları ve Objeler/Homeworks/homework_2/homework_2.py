"""
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

                    Memlekete sis çökmüş bir gece
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu

Bu dosyanın herbir satırını okuyun.
Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.
"""

class Dosya():

    def __init__(self,dosya_içeriği):
        with open("şiir.txt","r", encoding="utf-8") as file:
            self.dosya_içeriği = file.readlines()
            ilk_harf =  ""
            for i in self.dosya_içeriği:
                ilk_harf += i[0]

            print(ilk_harf)


dosya = Dosya("şiir.txt")