import random

def feladat_kiiras(jatekvege):
    print("Barátod bent ragadt a házban, mentsd meg, ha tudod.")
    print("Figyelmeztetés: Magán terület\nElérkeztél a titkos házhoz, ahol az a feladatod, hogy végig juss a különböző szobákon!\nVigyázz, hogy ne kerülj börtönbe.\n")
    kezdes = input("Felkészültél? (igen/nem)")
    if kezdes == "nem":
        print("Game Over!")
        jatekvege=2
    else:
        print("Akkor kezdjük.\n")
    return jatekvege


def terkep(lista,jatekvege):
    if jatekvege==0:
        print("-"*200)
        print(f"Kerités {"Postaláda":>10} {"Bejárat":>10} {"Konyha":>10} {"Lépcső alja":>15} {"Lépcső teteje":>20} {"Dolgozószoba":>15} {"Nappali":>10} {"Labor":>10} {"Erkély":>10} {"Titkos folyosó":>20}")
        print(f"Tábla {"Levél":>10} {"Kulcs":>11} {"Húsi":>23} {"Zseblámpa":>38} {"Gipsz gyümi":>15} {"Kötél":>18} {"Kincs":>15}")
        print(f"Leltár: {lista}")

def postalada(lista = []):
    level = input("Elviszed a levelet amit találtál? (igen/nem)")
    if level == "igen":
        lista.append("levél")
    print("Mehetünk a bejárathoz!\n")

def bejarat():
    print("Zárva van az ajtó!")
    kulcs = input("Szerinted hol van a kulcs az ajtóhoz?")
    while kulcs != "lábtörlő alatt":
        print("Próbáld más hol!\nHint! Nézd a padlón!")
        kulcs = input("Na, hol van a kulcs az ajtóhoz?")
    print("Gratulálók az ajtó nyitva van! Mehetünk tovább!\n")

def konyha(lista, jatekvege):
    print("Találkoztál a házvezető nővel!\nAdd neki a levelet, ha van!")
    level = input("Oda adod a levelet neki? (igen/nem)")
    if level == "igen":
        if "levél" in lista:
            print("Neki adtad a levelet. Mehetsz tovább!\n")
            lista.remove("levél")
        else:
            print("Nincs nálad, ezért börtön be zárt!")
            jatekvege=2
    else:
        print("Nem adtad a levelet neki, ezért ki rakott a házból!")
        jatekvege = 2
    return jatekvege



def lepcsoalja(lista, jatekvege):
    if jatekvege == 0:    
        print("Lépcső alján találtál egy húsit!")
        husi = input("Elviszed? (igen/nem)")
        if husi == "igen":
            lista.append("husi")
        print("Menj fel a lépcsőn!\n")

def lepcsoteteje(lista, jatekvege):
    if jatekvege == 0:
        szorny_lista = ["zöld csápi", "vörös csápi"]
        szorny = random.choice(szorny_lista)
        print(f"Össze talákoztál a {szorny}-val!")
        if szorny == "vörös csápi":
            if "husi" not in lista:
                jatekvege = 2
                print("Sajnos megevett, mert nem volt nálada húsi!")
            else:
                print("Nálad van húsi, amivel megetetted a szörnyet!\n")
                lista.remove("husi")
        if szorny == "zöld csápi":
            if "husi" not in lista:
                print("Nincs nálad a húsi, de kedves a szörny, úgyhogy tovább enged!")
            else:
                print("Nálad van húsi, amivel megetetted a szörnyet!\n")
                lista.remove("husi")
    return jatekvege

def dolgozo(lista, jatekvege):
    if jatekvege == 0:
        print("Be értél a dolgozó szobába!\nFényt látsz az asztalon!")
        lampa = input("Zseblámpa van az asztalon, felveszed? (igen/nem)\n")
        if lampa == "igen":
            lista.append("zseblámpa")
        
def nappali(lista, jatekvege):
    if jatekvege == 0:
        print("Beléptél az Ikeás nappaliba!")
        targy = input("Elkel vinned valamit a 3 térgy közül! De jól gondold meg!\nTitkos könyv, Gipsz gyümölcs, Don Bosco szoborra. Melyik legyen?")
        if targy == "Titkos könyv" or targy=="titkos könyv":
            lista.append(targy)
        elif targy == "Gipsz gyümölcs" or targy=="gipsz gyümölcs":
            lista.append("gipsz gyümölcs")
        else:
            lista.append(targy)
        print(f"Felvetted a {targy}\n")

        
def labor(lista, jatekvege):
    if jatekvege==0:
        print("Beléptél a laborba, ahol vár a Zöld csápi!\n Add a gipsz gyümölcsöt a Zöld csápinak, ha nálad van.")
        targy = input("Neki adod titkos információkért? (igen/nem)")
        if targy == "igen":
            if "gipsz gyümölcs" in lista:
                print("A titkos folyosót a térkép mögött találod\n")
                lista.remove("gipsz gyümölcs")
            else:
                print("Sajnos nincs nálad a gipsz gyümölcs\n")
        else:
            print("Úgy döntöttél,hogy nem adod neki. Nagy hiba!\n")

def tikosfolyoso(lista, jatekvege):
    if jatekvege==0:
        print("Keresd meg a titkos folyosót")
        folyoso = input("Szerinted hol van a folyosó?")
        while folyoso != "térkép mögött":
            print("Rossz helyen keresed.\nHint! Keresd a térképnél.")
            folyoso = input("Mostmár tudod, hogy hol van a folyosó?")
        print("Sötét van a folyosón.")
        zseblampa = input("Van-e nálad zseblámpa? (igen/nem)")
        if zseblampa == "igen":
            if "zseblámpa" in lista:
                print("Kikerülted a gödröt és meg találtad a barátodat")
                jatekvege = 1
            else:
                print("Nincs nálad zseblámpa, bele estél a gödörbe.")
                kezdes=input("Szeretnéd újra kezdeni a játékot? (igen/nem)")
                if kezdes=="igen":
                    jatekvege=0
                else:
                    jatekvege=2
        else:
            print("Nincs nálad zseblámpa, bele estél a gödörbe.")
            kezdes=input("Szeretnéd újra kezdeni a játékot? (igen/nem)")
            if kezdes=="igen":
                jatekvege=0
            else:
                jatekvege=2
        return jatekvege
    
def ellenorzes(jatekvege):
    if jatekvege==1:
        print("Gratulálok kijutotattok a házból!")
    elif jatekvege == 2:
        print("Game Over!")