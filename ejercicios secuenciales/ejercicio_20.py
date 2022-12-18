#ejercicio20 
import os
'''20.	Dada una cantidad de dinero en soles, desarrolle el programa 
que descomponga dicha cantidad en billetes de 200, 100, 50, 20, 10 y 
monedas de 5, 2, 1 nuevos soles.'''

cantidad_de_soles = int (input ('Ingresa el valor de cantidad en soles: '))

monedas_de_1=cantidad_de_soles
billetes_de_500=(monedas_de_1-monedas_de_1%500)//500
print ('Valor de billetes de 500: ' + repr (billetes_de_500))
monedas_de_1=monedas_de_1%500
billetes_de_200=(monedas_de_1-monedas_de_1%200)//200
print ('Valor de billetes de 200: ' + repr (billetes_de_200))
monedas_de_1=monedas_de_1%200
billetes_de_100=(monedas_de_1-monedas_de_1%100)//100
print ('Valor de billetes de 100: ' + repr (billetes_de_100))
monedas_de_1=monedas_de_1%100
billetes_de_50=(monedas_de_1-monedas_de_1%50)//50

print ('Valor de billetes de 50: ' + repr (billetes_de_50))
monedas_de_1=monedas_de_1%50
billetes_de_20=(monedas_de_1-monedas_de_1%20)//20
print ('Valor de billetes de 20: ' + repr (billetes_de_20))
monedas_de_1=monedas_de_1%20
billetes_de_10=(monedas_de_1-monedas_de_1%10)//10
print ('Valor de billetes de 10: ' + repr (billetes_de_10))
monedas_de_1=monedas_de_1%10
billetes_de_5=(monedas_de_1-monedas_de_1%5)//5
print ('Valor de billetes de 5: ' + repr (billetes_de_5))
monedas_de_1=monedas_de_1%5

print ('Valor de monedas de 1: ' + repr (monedas_de_1))
monedas_de_2=(monedas_de_1-monedas_de_1%2)//2
print ('Valor de monedas de 2: ' + repr (monedas_de_2))
monedas_de_1=monedas_de_1%2
