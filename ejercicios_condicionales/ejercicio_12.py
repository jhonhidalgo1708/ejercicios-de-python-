#ejrcicio12
'''Dado un número que expresa el tiempo en segundos, desarrolle 
l programa que exprese dicho tiempo como la cantidad de días,
 horas, minutos y segundos contenidos en ese número.'''
#datos asignados

num_segundos=int(input("digite en numero expresados en segundos:"))


#solucion 

dias=((num_segundos//60)//60)//24
print("dias",dias)
horas=((num_segundos//60)//60)%24
print("horas",horas)
minutos=(num_segundos//60)%60
print("minutos",minutos)
segundos=num_segundos%60
print("segundos",segundos)
