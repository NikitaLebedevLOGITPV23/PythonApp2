         #7 inimese pikkus ja sugu
sugu=input("Kas sa oled mees või naine?"). lower()
if sugu=="naine" or sugu=="n":
    l1=155
    l2=170
    l3=255
elif sugu=="mees" or sugu=="m":
    l1=160
    l2=180
    l3=255
else:
    l1=0
    print("Viga")
if l1:=0:
    try:
        pikkus=int(input("Sisesta oma pikkus: "))
        if pikkus>29 and pikkus<155:
           vastus="lühike"
        elif pikkus>=155 and pikkus<170:
           vastus="keskmine"
        elif pikkus>170 and pikkus<=255:
           vastus="pikk"
        else:
           vastus="tundmatu"
        print("Sinu pikkus on (0)" .format(vastus))
    except:
        print("Vale andmete format:")

        #8 poos
from random import *
from datetime import *
arve_nr=datetime.now() # date.today()
print(arve_nr)
tsekk="Arve:"+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

toode="Piim"
hind=randint(50,150) /100
v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas ta osta?"). lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk=toode+ " "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+ "\n"
    summa+=mitu*hind
toode="Sai"
hind=randint(80,180) /100
v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas ta osta?"). lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk=toode+ " "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+ "\n"
    summa+=mitu*hind
toode="Leib"
hind=randint(50,150) /100
v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas ta osta?"). lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk=toode+ " "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+ "\n"
    summa+=mitu*hind
tsekk="Kokku maksta: " +str(summa)
print(tsekk)