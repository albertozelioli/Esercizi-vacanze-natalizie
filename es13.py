#Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è uguale a zero).

print("Questo programma verifica se il numero inserito è pari o dispari.")
numero = int(input("Inserire un numero a scelta: "))

if numero%2 == 0:
    print("Il numero",numero,"è pari.")
else: 
    print("Il numero",numero,"è dispari.")
