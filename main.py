import maniac_feladatok



jatekvege = 0

while jatekvege==0:
    leltar_lista = []
    jatekvege=maniac_feladatok.feladat_kiiras(jatekvege)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    maniac_feladatok.postalada(leltar_lista)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    maniac_feladatok.bejarat()
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    jatekvege = maniac_feladatok.konyha(leltar_lista,jatekvege)
    maniac_feladatok.ellenorzes(jatekvege)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    maniac_feladatok.lepcsoalja(leltar_lista, jatekvege)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    jatekvege = maniac_feladatok.lepcsoteteje(leltar_lista, jatekvege)
    maniac_feladatok.ellenorzes(jatekvege)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    maniac_feladatok.dolgozo(leltar_lista, jatekvege)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    maniac_feladatok.nappali(leltar_lista, jatekvege)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    maniac_feladatok.labor(leltar_lista, jatekvege)
    maniac_feladatok.terkep(leltar_lista, jatekvege)
    jatekvege = maniac_feladatok.tikosfolyoso(leltar_lista, jatekvege)
    maniac_feladatok.ellenorzes(jatekvege)
