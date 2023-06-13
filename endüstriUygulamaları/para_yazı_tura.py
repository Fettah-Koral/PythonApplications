import random

def flip_coin():
    if random.random()>=0.5:
        return 'T'
    else:
        return 'Y'
    

def multiple_coin(n):
    t=0
    y=0

    for k in range(n):
        sonuc=flip_coin()
        if sonuc=='T':
            t=t+1
        else:
            y=y+1
    print("toplam Tura sayısı: {}, yazı sayısı: {}".format(t,y))
    
multiple_coin(10000)