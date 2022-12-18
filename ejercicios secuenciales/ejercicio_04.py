#inicio
import os
os.system("cls")

'''En países de habla inglesa, es común dar la estatura de una persona como la suma de una
cantidad de pies, más una cantidad de pulgadas, por ejemplo 3’ 2”. Desarrolle el programa que
determine la estatura en metros dada su estatura en el formato inglés'''

pies = float (input("Escriba la cantidad en pies:" ))
pulgadas = float (input("Escriba la cantidad en pulgadas:" ))
tpies=pies*30.48
tpulgadas=pulgadas*2.54
total_en_cm=tpies+tpulgadas
total_en_m=total_en_cm/100
print("total de tallas en metros",total_en_m,"m" ) 