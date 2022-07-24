print("Lütfen oyuncu bilgilerini giriniz.")

ad = input("Oyuncunun adı:")
soyad = input("Oyuncunun soyadı:")
takım = input("Oyuncunun bulunduğu takım:")

bilgi = [ad,soyad,takım]

print("Bilgiler kaydediliyor...")

print("Ad:{}\n Soyad:{}\n Takım:{}\n".format(bilgi[0],bilgi[1],bilgi[2]))

print("Bilgiler kaydedildi.")