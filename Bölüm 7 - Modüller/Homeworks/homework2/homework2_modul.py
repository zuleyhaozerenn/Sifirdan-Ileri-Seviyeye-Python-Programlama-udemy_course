"""
Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın.
Bu yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.
"""

def karekok(sayı):
    """
    Bu fonksiyon girdiğiniz sayının karekökünü alır.
    """
    if(sayı == 0):
        print("Sonuç:", 0 )
    else:
        print("Sonuç:", sayı ** 0.5)

def üs(sayı,üs):
    """
    Bu fonksiyon girdiğiniz sayının istediğiniz değerdeki üssünü alır.
    """

    if(üs == 0):
        print("Sonuç:", 1)
    elif(üs == 1):
        print("Sonuç:",sayı)
    else:
        print("Sonuç:", sayı ** üs)

def faktöriyel(sayı):
    """
    Bu fonksiyon girdiğiniz sayının faktöriyelini hesaplar.
    """
    faktoriyel = 1
    if(sayı == 0 or sayı == 1):
        return 1
    else:
        while(sayı >= 1):
            faktoriyel *= sayı
            sayı -= 1
        return faktoriyel


def kombinasyon(eleman,seçim):
    """
    Bu fonksiyon kombinasyon hesaplar. 2 adet değer alır.
    """
    def faktöriyel(sayı):
        faktoriyel = 1
        if (sayı == 0 or sayı == 1):
            return 1
        else:
            while (sayı >= 1):
                faktoriyel *= sayı
                sayı -= 1
            return faktoriyel
    kombinasyon = (faktöriyel(eleman)) / (faktöriyel(seçim) * faktöriyel(eleman - seçim))
    print("Sonuç:", kombinasyon)

def permütasyon(eleman,seçim):
    """
    Bu fonksiyon permütasyon hesaplar. 2 adet değer alır.
    """
    def faktöriyel(sayı):
        faktoriyel = 1
        if (sayı == 0 or sayı == 1):
            return 1
        else:
            while (sayı >= 1):
                faktoriyel *= sayı
                sayı -= 1
            return faktoriyel
    permutasyon = (faktöriyel(eleman)) / (faktöriyel(eleman - seçim))
    print("Sonuç: ",permutasyon)

