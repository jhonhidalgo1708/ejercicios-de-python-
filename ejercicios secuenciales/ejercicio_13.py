#ejercicicio 11
import os
os.system("cls")
'''11.	Dado dos números enteros de 3 cifras,
desarrolle el programa que muestre la cifra
 primera y tercera cifras intercambiadas entre 
 ambos números. Ejemplo 123 y 456  624 y 351'''

#datos que se veran
numero_1=int(input("Ingrese el numero 1 "))
numero_2=int(input("Ingreseel  numero 2 "))

numero1_c1=numero_1//100
numero1_c2=numero_1%100//10
numero1_c3=numero_1%10

numero2_c1=numero_2//100
numero2_c2=numero_2%100//10
numero2_c3=numero_2%10

print("---numeros intercambiados---")
print("numero 1",(numero2_c3*100)+(numero1_c2*10)+(numero2_c1))
print("numero 2",(numero1_c3*100)+(numero2_c2*10)+(numero1_c1))
