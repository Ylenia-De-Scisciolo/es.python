print("Benvenuti alla funzione Geometra!")
print("In fase di selezione a ciascun possibile calcolo corrisponde un valore numerico:")
print("- Area Quadrato: 1") 
print("- Area Rettangolo: 2")
print("- Area Triangolo: 3")
print("- Area Cerchio: 4")
print("Di quale figura geometrica desideri calcolare l'area?")
scelta = int(input(">>> "))
if scelta == 1:
    print("Hai scelto: Area Quadrato")
    lato = float(input("Inserisci il valore del lato del quadrato "))
    lato_per_lato = lato * lato
    print("L'area del quadrato e: " , lato_per_lato)
elif scelta == 2:
    print("Hai scelto: Area Rettangolo")
    base = float(input("Inserisci il valore della base "))
    altezza = float(input("Inserisci il valore dell'altezza "))
    base_per_altezza = base * altezza
    print("L'area del rettangolo e: " , base_per_altezza)
elif scelta == 3:
    print("Hai scelto: Area Triangolo")
    base = float(input('Inserisci il valore della base '))
    altezza = float(input("Inserisci il valore dell'altezza"))
    base_per_altezza2 = (base * altezza)/2
    print("L'area del triangolo e: " , base_per_altezza2)
elif scelta == 4:
    print("Hai scelto: Area Cerchio")
    r = float(input('Inserisci il valore del raggio '))
    area= (r * r) * 3.14
    print("L'area del cerchio e:" , area)
else:
    print ('Nessun calcolo disponibile per la scelta effettuata!')