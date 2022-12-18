#ejercicio11

'''Dado dos números enteros de 3 cifras, desarrolle el programa que muestre la cifra primera y 
tercera cifras intercambiadas entre ambos números. Ejemplo 123 y 456  624 y 351.'''

#datos propuestos 

numero1=int(input("Ingrese el numero 1: "))


numero2=int(input("Ingrese el numero 2: "))

#solucion 

numero1_c1=numero1//100
numero1_c2=numero1%100//10
numero1_c3=numero1%10

num2_c1=numero2//100
num2_c2=numero2%100//10
num2_c3=numero2%10

print("---numeros intercambiados---")
print("numero 1",(num2_c3*100)+(numero1_c2*10)+(num2_c1))
print("numero 2",(numero1_c3*100)+(num2_c2*10)+(numero1_c1))