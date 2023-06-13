import random 
#0: Taş 1: kağıt, 2=Makas
def sonuc():
    return random.randint(0,2)

def oyun():
    a=sonuc()
    b=sonuc()
    
    if a==b:
        return 'T'
    elif a==0 and b==2:
        return 'A'
    elif a==2 and b==0:
        return 'B'
    elif a==0 and b==1:
        return 'B'
    elif a==1 and b==0:
        return 'A'
    elif a==1 and b==2:
        return 'B'
    else:
        return 'A'
    

    
def multi_game(n):
    a_win=0
    b_win=0
    for k in range(n):
        result=oyun()
        if result=='A':
            a_win=a_win+1
        elif result=='B':
            b_win=b_win+1
        else:
            print("beraberlik")
    print("A {} kez kazandı, B {} kez kazandı".format(a_win,b_win))

multi_game(10)

        
        
    
