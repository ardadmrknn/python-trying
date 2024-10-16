ad = str(input("isim gir: "))
soyad = str(input("soyisim gir: "))
kilo = float(input("kilo gir: "))
boy = float(input("boy(m) gir: "))

fr = (kilo / (boy**2))
print(fr)

a = 0<fr<18.4
b = 18.5<=fr<24.9
c = 25<=fr<29.9
d = 30<=fr

if a:
    print(f"sayın {ad} {soyad}, indeksiniz: Zayıf")
elif b:
    print(f"sayın {ad} {soyad}, indeksiniz: Normal")
elif c:
    print(f"sayın {ad} {soyad}, indeksiniz: Kilolu")
elif d:
    print(f"sayın {ad} {soyad}, indeksiniz: Obez")
else:
    print("bilgi kontrol")