# ciklus bizonyos műveletek ismétésére való
# ciklusváltó - számlálja, hogy hányszor futott már le a ciklus
#ciklus - ismétendő utasítások
# ciklusfeltétel - itt adjuk meg, hogy meddig fusson a ciklus
def szamlalos_ciklus1():
    cv: int = 1
    while (cv <= 10):
        print("Többé nem kések, mert lemaradok fontos információkról!")
        cv += 1

    print(cv, "A ciklus után")

def elotesztelos_ciklus():
## kérjünk be egy 10-nél nayobb számot a felhasználótól
    szam: int = int(input("Adjon meg egy 10-nél nagyobb számot!"))
    if szam <= 10 :
        print("10-nél nagyobb számot!")
        szam: int = int(input("Adjon 10-nél nagyobb számot!"))

    print("Hurrrá, végre sikerült 10-nél nagyobbat!", szam)

# készíts külön eljárást
# 1. írd ki a számokat 1 és 10 között a képernyőre egymás mellé
# 2. írd ki a számokat 20 és 30 között a képernyőre
# 3. Írd ki a 15 és 25 közötti páros számokat
# 4. írd ki a számokat egyessével 12 és 30 között fordított sorrendben

#1. feladat
def feladat1():
    cv: int = 1
    while(cv <= 10):
        print(f"{cv}", end=" ")
        cv += 1
#2. feladat
def feladat2():
    cv: int = 20
    while(cv <= 30):
        print(f"{cv}", end=" ")
        cv += 1
 
#3. feladat
def feladat3():
    cv: int = 15 
    while(cv <= 25):
        if cv % 2 == 0:
            print(f"{cv}", end=" ")
        cv += 1 

# 4. feladat
def feladat4():
    cv: int = 30 
    while(cv >= 12):
            print(f"{cv}", end=" ")
            cv -= 1 


