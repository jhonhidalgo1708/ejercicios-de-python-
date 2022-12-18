#ejercicio12
import os
os.system("cls")
'''Dado un número que expresa el tiempo en segundos, desarrolle el 
programa que exprese dicho tiempo como la cantidad de días, horas,
 minutos y segundos contenidos en ese número'''

numero_segundos=int(input("expresa el tiempo  en segundos:"))


cantidad_dias=((numero_segundos//60)//60)//24

print("dias",cantidad_dias)
cantidad_horas=((numero_segundos//60)//60)%24
print("horas",cantidad_horas)
cantidad_minutos=(numero_segundos//60)%60
print("minutos",cantidad_minutos)
cantidad_segundos=numero_segundos%60
print("segundos",cantidad_segundos)


