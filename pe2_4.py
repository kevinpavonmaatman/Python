#Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt
#heeft en dat daarna het salaris uitprint.
#Voorbeelduitvoer:
#Wat verdien je per uur: 3.80
#Hoeveel uur heb je gewerkt: 20
#20 uur werken levert 76.0 Euro op

verdienste = int(input ('Wat verdien je per uur: '))
uuren = int(input ('Hoeveel uur heb je gewerkt? '))
totalen = uuren * verdienste

print(uuren, 'uur werken levert', totalen, 'Euro op')
