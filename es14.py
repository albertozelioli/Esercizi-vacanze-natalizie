#Crea un programma che scriva la differenza di due numeri "a" e "b" se il loro prodotto è maggiore di 10, oppure la loro somma se il loro prodotto è minore o uguale a 10.
#Esegui poi il programma con diverse coppie di valori per "a" e "b": (-5, 2), (5, -5), (10, 2), (-4, -5), (5, 4), (-3, 2).

print("Questo programma, data una coppia di numeri, restituisce la loro differenza se il loro prodotto è maggiore di 10, e la loro somma se il loro prodotto è minore o uguale a 10.")
a = int(input("Inserire il primo valore: "))
b = int(input("Inserire il secondo valore: "))

if (a * b) > 10:
    print("Essendo il prodotto di questi due numeri maggiore di 10, la differenza tra questi due numeri è: ", a - b)
elif (a * b) <= 10:
    print("Essendo il prodotto di questi due numeri minore o uguale di 10, la somma tra questi due numeri è: ", a + b)
