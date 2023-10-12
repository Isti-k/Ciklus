## eljárások tesztelésére
import eljarasok

#1. teszteset
print("1. teszteset: Pozitív számok")
eljarasok.hanyados(3, 5)
print("2. testeset: Negatív számok")
eljarasok.hanyados(-5, -2)
print("3. teszteset: Tört számok - nem jó teszteset, mert egész szám")
eljarasok.hanyados(-5.2, -2.2)
print("4. teszteset: Nincs paraméter")
eljarasok.hanyados() # adtunk alapértelmezett értéket
print("5. teszteset: számláló 0, a=0")
eljarasok.hanyados(0, -5)
print("5. teszteset: neező b=0")
eljarasok.hanyados(-5, 0)