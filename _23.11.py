from module1 import *
users=loe_failist_listisse("users.txt")
psword=loe_failist_listisse("passwords.txt")

while True:
    print("Näita kõike-0,\nReg-1,\nAvt-2,\nVälja-3")
    v=int(input())
    if v==0:
        koik_kasutajad(users,psword)
    elif v==1:
        print("Registreerimine ")
        users,passwords=register(users,psword)
    elif v==2:
        print("Avtoriseerimine")
        log(users,psword)
    elif v==3:
           print("Välja")
           faili_sisu_umberkirjutamine("users.txt",users)
           faili_sisu_umberkirjutamine("passwords.txt",passwords)
           quit()
    else:
        print("On vaja valida 1,2 või 3") #kõik on olemas




        