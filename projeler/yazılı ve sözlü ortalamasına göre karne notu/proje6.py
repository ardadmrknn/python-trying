yaz1 = int(input("1. yazılı notu: "))
yaz2 = int(input("2. yazılı notu: "))
söz = int(input("sözlü notu: "))

a = (yaz1 + yaz2 + söz)/3

if a>=0:
    if a<25:
        print("0")
    if 25<=a<45:
        print("1")
    if 45<=a<55:
        print("2")
    if 55<=a<70:
        print("3")
    if 70<=a<84:
        print("4")
    if 85<=a<100:
        print("5")

else:
    print("kaldın")