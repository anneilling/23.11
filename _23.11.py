from module1 import *
users=["Anne"]
psword=["12345"]

while True:
    print("Näita kõike-0,\nReg-1,\nAvt-2,\nVälja-3")
    v=int(input())
    if v==0:
        koik_kasutajad(users,psword)
    elif v==1:
        print("Registreerimine ")
        while 1:
            log=input("Login ")
            if log not in users:
                print("Login soobib")
                break
            else:
                 print("See nimi juba on olemas listis")
        v=input("Arvuti-A või ise-I loob parool ")
        if v.upper()=="A":
            pas=passautomat()
        elif v.upper()=="I":
            while 1:
                pas=input("Sisesta oma parool ")
                tulemus=passcontrol(pas)
                if tulemus==True:
                    users.append(log)
                    psword.append(pas)
                    break
        elif v==2:
           print("Avtoriseerimine")
           log(users,psword)
        elif v==3:
            print("Välja")
            break #valmis
        else:
            print("On vaja valida 1,2 või 3")#kõik on olemas




        