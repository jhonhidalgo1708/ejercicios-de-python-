#ejercicio7
'''Desarrolle el programa que lea tres números enteros y determine el 
número intermedio. No use operadores lógicos en la solución'''

primer_numero=input("dicte el primer numero")
segundo_numero=input("dicte el segundo  numero")
tercer_numero=input("dicte  el tercer numero")

#solucion
#si
if primer_numero>segundo_numero:
   medio =primer_numero
   xtem = segundo_numero
   #sino
else:
   medio = segundo_numero
   xtem = primer_numero
if medio > tercer_numero :
   medio = tercer_numero
if medio < xtem :
   medio = xtem

print("El número Medio es : ",medio)