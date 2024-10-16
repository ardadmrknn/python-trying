mail = "demirkanarda9@gmail.com"
parola = "1234567"

a = input("mail gir: ")
b = input("parola gir: ")

z2 = (a==mail) and (b==parola)

if z2:
    print("--giriş başarılı--")

elif (a!=mail):
    print("mail adresini kontrol et, giriş başarısız")
elif (b!=parola):
    print("şifre yanlış, giriş başarısız")
else:
    print("--giriş başarısız--")