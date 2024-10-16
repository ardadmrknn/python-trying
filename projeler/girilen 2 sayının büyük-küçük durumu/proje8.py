x = float(input("1 sayı gir: "))
y = float(input("2. sayı gir: "))

if x > y:
    print (f"{x} büyüktür {y}'den/dan")
elif x==y:
    print("iki sayı birbirine eşit")
else:
    print(f"{x} küçüktür {y}'den/dan")