#funktsioonide loomine
from random import *
def loe_failist_listisse(file:str)->list: #loeme tekst failist ja salvestame listisse
    f=open(file,"r")
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_

def passcontrol(psword: str)->bool:
    ls=list(psword)
    for e in ls:
        if e.isdigit(): d=True
        if e.isalpha(): a=True
        if e.isupper(): u=True
        if e.islower(): l=True
        if e in list(".,:;!_*-+()/#¤%&"): s=True
    if d==True and a==True and u==True and l==True and s==True:
           t=True
    else:
           t=False
    return t

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
                print(f"See on sinu parool:{pas}")
            elif v.upper()=="I":
                    while 1:
                        pas=input("Sisesta oma parool")
                        tulemus=paskontroll(pas)
                        if tulemus==True:
                            users.append(log)
                            psword.append(pas)
                            break
                        return users,psword


