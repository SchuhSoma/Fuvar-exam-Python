print("\n\tOKJ vizsgafeladat: Fuvar")
print("\n-----------------------------------------------------\n")
print("2.Feladat adatok beolvasása:")
FuvarAdatok_Lista=[]
beolvasottDB=0
fajl=open("fuvar.csv",encoding="utf-8")
for egySor in fajl:
    egySor=egySor.strip()
    dbok=egySor.split(";")
    Fuvar={
        "taxiId":int(dbok[0]),
        "indulas":dbok[1],
        "idotartam":int(dbok[2]),
        "tavolsag":float(dbok[3]),
        "viteldij":float(dbok[4]),
        "borravalo":float(dbok[5]),
        "fizetesmod":dbok[6]
         }
    FuvarAdatok_Lista.append(Fuvar)
    beolvasottDB+=1
fajl.close()
if(beolvasottDB>0):
    print("\tSikeres beolvasás, beolvasott sorok száma: ",beolvasottDB)
else:
    print("\tSikertelen beolvasás próbáld újra")
print("\n-----------------------------------------------------\n")
print("3.Feladat: bejegyzések száma")
print("\tbejegyzések száma: ", len(FuvarAdatok_Lista))
print("\n-----------------------------------------------------\n")
print("4.Feladat: 6185-ös taxis össz bevétele mennyi volt")
Bevetel=0
for Fuvar in FuvarAdatok_Lista:
    if(Fuvar["taxiId"]==6185):
        Bevetel+=Fuvar["viteldij"]+Fuvar["borravalo"]
print("\tA 6185-ös taxi bevétele: ", Bevetel," $")
print("\n-----------------------------------------------------\n")
print("5.Feladat: fizetési mód statisztika")
FizetesMod_List=[]
for Fuvar in FuvarAdatok_Lista:
    if not FizetesMod_List.__contains__(Fuvar["fizetesmod"]):
        FizetesMod_List.append(Fuvar["fizetesmod"])
#for i in range(len(FizetesMod_List)):
#    #print(FizetesMod_List[i])
statisztika_List=[]
for i in range(len(FizetesMod_List)):
    db = 0
    for Fuvar in FuvarAdatok_Lista:
        if(Fuvar["fizetesmod"]==FizetesMod_List[i]):
            db+=1
    statisztika={
        "mod":FizetesMod_List[i],
        "db":db
    }
    statisztika_List.append(statisztika)
    print(FizetesMod_List[i], ": ", db)
print("----------------------------------------")
for i in range(len(statisztika_List)):
    print(statisztika_List[i])
print("\n-----------------------------------------------------\n")
print("6.Feladat: összes mérföld hossza km-ben")
OsszMerfold=0
OsszKm=0
for Fuvar in FuvarAdatok_Lista:
    OsszMerfold+=Fuvar["tavolsag"]
    OsszKm=OsszMerfold*1.6
print("\tA megtett összes kilóméter hossza: ",OsszKm)
print("\n-----------------------------------------------------\n")
print("7.Feladat: leghosszabb fuvar")
leghosszabb=0
leghosszabbID=0
leghosszabbViteldij=0
leghosszabTav=0
for Fuvar in FuvarAdatok_Lista:
    if(leghosszabb<Fuvar["idotartam"]):
        leghosszabb=Fuvar["idotartam"]
        leghosszabbID=Fuvar["taxiId"]
        leghosszabbViteldij=Fuvar["viteldij"]
        leghosszabTav=Fuvar["tavolsag"]
print("\tA leghosszabb fuvar időtartalma: ",leghosszabb,"\n\ttaxi azonosító: ",leghosszabbID,"\n\tviteldíj: ",leghosszabbViteldij,"távolság: ", leghosszabTav)