#ejercicio9
'''	Desarrolle el programa que lea un número
 entero y determine la suma de sus cifras. 
 Asumir que el número es positivo y de 4 cifras.'''

numero = int(input(" cuatro cifras propuestas : "))

suma_delasifras= 0
while numero > 0:
    suma_delasifras = suma_delasifras + (numero % 10)
    numero = numero // 10
#salida     
print("La suma total de los dígitos",suma_delasifras)