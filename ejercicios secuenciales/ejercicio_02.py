#inicio
import os

os.system("cls")

'''Desarrolle el programa que permite convertir una cantidad dada en metros a su 
equivalente en centímetros, pulgadas, pies y yardas. Considere los siguientes factores de conversión : 
1 metro = 100 cm, 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 cm'''

metros=int(input("Digite una cantidad en metros:"))
 # rasolucion del problema 
centimetros=metros*100
print("centimetros:",format(centimetros,".2f"),"cm")
pulgadas=centimetros/2.54134
print("pulgadas:",format(pulgadas,".2f"),"in")
pies=pulgadas/12
print("pies:",format(pies,".2f"),"ft")
yardas=pies/3
print("yardas:",format(yardas,".2f"),"yd")

