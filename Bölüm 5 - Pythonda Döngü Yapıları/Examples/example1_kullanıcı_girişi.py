sys_kullanıcı_adı = "Züleyha"
sys_parola = 1234
giriş_hakkı = 3

print("Sisteme hoş geldiniz. Lütfen aşağıya kullanıcı adınızı ve parolanızı giriniz.")


while True:
    kullanıcı_adı = input("Kullanıcı adınız: ")
    parola = int(input("Parolanız: "))
    if(sys_kullanıcı_adı != kullanıcı_adı and sys_parola == parola):
        print("Kullanıcı adını yanlış girdiniz. Lütfen tekrar deneyiniz..")
        giriş_hakkı -= 1
    elif(sys_kullanıcı_adı == kullanıcı_adı and sys_parola != parola):
        print("Parolanızı yanlış girdiniz. Lütfen tekrar deneyiniz..")
        giriş_hakkı -= 1
    elif (sys_kullanıcı_adı != kullanıcı_adı and sys_parola != parola):
        print("Kullanıcı adını ve parolanızı yanlış girdiniz. Lütfen tekrar deneyiniz..")
        giriş_hakkı -= 1
    else:
        print("Girilen bilgiler doğrudur. Sisteme hoş geldiniz.")
        break

    if(giriş_hakkı == 0):
        print("Giriş hakkınız bitmiştir.")
        break
