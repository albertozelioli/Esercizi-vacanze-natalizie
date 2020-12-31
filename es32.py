#Implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo grado: a x + b = 0.
#Il processo risolutivo dipende dai valori assunti dai coefficienti a e b secondo la tabella che segue: se a = 0 e b = 0 è indeterminata; se a != 0 e b = 0 allora x = 0; se a = 0 e b != 0 è impossibile; se a != 0 e b != 0 allora x = -b/a.

print("Questo programma calcola la soluzione di un equazione di primo grado: a x + b = 0")
a = int(input("Inserire il valore di a: "))
b = int(input("Inserire il valore di b: "))

if a == 0 and b == 0:
    print("L'equazione è indeterminata.")
elif a != 0 and b == 0:
    print("x = 0")
elif a == 0 and b != 0:
    print("L'equazione è impossibile.")
elif a != 0 and b != 0:
    print("x =",-b/a)
