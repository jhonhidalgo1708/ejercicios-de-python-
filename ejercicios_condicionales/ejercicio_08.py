#ejercicio 8 
'''Un estudiante recibe una propina mensual S/. 20. El 
estudiante rinde mensualmente tres exámenes. Su papá ha 
decidido incentivarlo dándole una propina adicional 
de S/. 5 por cada examen aprobado. Desarrolle el programa que
 determine el monto total de la propina'''
#datos propuestoss
primer_exsamen=float(input("dicte  el primer numero:"))

segundo_examen=float(input("dicte el segundo  numero:"))

tercer_examen=float(input("dicte el tercer numero:"))
#solucion 

propina=20
#si 
if (primer_exsamen>13):propina+5
if (segundo_examen>13):propina+5
if (tercer_examen>13):propina+5


print("Valor de la propina",propina)