import random
sayi=random.randint(0,100)
print(sayi)
deneme=0
while True:
    tahmin=int(input("0 ile 100 arasinda bir sayi giriniz: "))
    deneme=deneme+1
    if sayi==tahmin:
        print("tebrikler!!! {}. denemede bildiniz".format(deneme))
        break
    if tahmin<sayi:
        print("tahmininizi artiriniz ")
        continue
    if tahmin>sayi:
        print("tahmininizi azaltiniz ")
        continue   
