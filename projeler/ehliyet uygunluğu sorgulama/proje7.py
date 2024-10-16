a = input("isim: ")
b = int(input("yaş: "))

if b>=18:
    c = input("eğitim düzeyi: ")

    if (c=="lise" or c=="üniversite"):
        print(f"sayın {a} EHLİYET ALABİLİRSİNİZ")

    else:
        print("oku da gel")

else:
    print("nah sana EHLİYET, büyü de gel")