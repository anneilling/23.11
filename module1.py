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
    random.shuffle(ls) #segage väärtusi
#eraldame loendist 12 suvalist väärtust
    psword="".join([choice(ls) for x in range(12)])
#parool on valmis
    return psword

def koik_kasutajad(users,passwords):
    i=0
    for user in users:
        print(user,end="-")
        print(psword[i])
        i+=1
