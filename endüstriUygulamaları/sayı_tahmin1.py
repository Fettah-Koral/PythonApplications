import random

sayı = random.randint(1, 10)
tahmin = None

while tahmin != sayı:
    tahmin = input("1 ve 10 arasında bir sayı tahmin ediniz: ")
    tahmin = int(tahmin)

    if tahmin == sayı:
        print("Tebrikler! Bildiniz!")
        break
    else:
        print("Üzgünüm, Tekrar deneyiniz!")
