

primeranota = int(input("digite la primer nota "))
segundanota = int(input("digite la segunda nota "))
terceranota= int(input("digite la tercera  nota "))
cuartanota=int(input("digite la tercera  nota "))
#solucion de los datos 

#operacion
if primeranota<segundanota:
   primeranota<terceranota
   primeranota<cuartanota
   elimine=primeranota
else:
    if segundanota<primeranota:
       segundanota<terceranota
       segundanota<cuartanota
       elimine=segundanota
    else:
        elimine=terceranota

total_de_promedio=(primeranota+segundanota+terceranota+cuartanota-elimine)/3
#salida
print("su premedio fue",total_de_promedio)
print("y la nota eliminada ",elimine)