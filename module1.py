#funktsioonide loomine
from random import *
def passcontrol(psword):
    ls=list(psword)
    for i in psword:
        if i.isdigit()== True:
            digit="True"
        if i.isalpha()== True:
            alpha="True"
        if i.isupper()==True:
            upper="True"
        if i.islower()==True:
            lower="True"
        if i in list('.','-','+','/','%'):
            symbol="True"
    if digit=="True" and upper=="True" and alpha=="True" and lower=="True" and symbol=="True":
        ans=True
    else:
        ans=False
    return ans
def passautomat()-> str:
 #parool genereeritakse masinaga
    str0=".,:;!_*-+()/#¤%&"
    str1="0123456789"
    str2="qwertyuiopasdfghjklzxcvbnm"
    str3=str2.upper() #QWERTYUIOPASDFGHJKLZXCVBNM
    str4=str0+str1+str2+str3
    ls=list(str4) #list
    shuffle(ls) #segage väärtusi
#eraldame loendist 12 suvalist väärtust
    psword="".join([choice(ls) for x in range(12)])
#parool on valmis
    return psword

def koik_kasutajad(users,psword):
    i=0
    for user in users:
        print(user,end="-")
        print(psword[i])
        i+=1

def autoris(users,psword):
    log=input("Login: ")
    if log not in users:
        print("Tunnus on mitte registeeritud")   
    else:
            pas=input("Parool: ")
            if pas not in psword:
                print("Vale parool")
            else:
                if users.index(log)==psword.index(pas):
                        print("Tere tulemast")

def register(users,psword):
    while 1:
        log=input("Kasutajatunnus:")
        if log not in users:
            print("Tunnus soobib")
            break
        else:
            print("See nimi juba on olemas listis")
            v=input("Arvuti-A või ise-I loob parool")
            if v.upper()=="A":
                pas=passautomat()
                print(f'See on sinu parool:{pas}')
            elif v.upper()=="I":
                    while 1:
                        pas=input("Sisesta oma parool")
                        tulemus=paskontroll(pas)
                        if tulemus==True:
                            users.append(log)
                            psword.append(pas)
                            break
                        return users,psword


