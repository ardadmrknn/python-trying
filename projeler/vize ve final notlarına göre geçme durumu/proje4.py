vize1 = int(input("1. vize: "))
vize2 = int(input("2. vize: "))
final = int(input("final: "))

ort = (((vize1+vize2)/2)*0.6) + (final * 0.4)

if ort>50 and final>=50:
    print("GEÇTİN!")

if final>=70:
    print("final notunuzdan dolayı geçtiniz!")

else: 
    print("KALDIN")