#ejercicio17
'''17.	Una institución social recibe anualmente una 
donación que reparte de la siguiente forma: 25% para el
 centro de salud, 35% en el comedor infantil, 25% para la escuela infantil y 
el resto para el asilo de ancianos.  Desarrolle el programa 
que muestre los montos asignados.'''

import os
os.system("cls")
#datos 
donacion=float(input(" monto de la donacion"))
# resolucion de los datos 
centro_de_salud=donacion*0.25
comedor_infantil=donacion*0.35
escuela_infantil=donacion*0.25
asilo_ancianos=donacion*0.15

print("el centro de salud recibe S/.",format(centro_de_salud,"2f"))
print("el comedor infantil recibe S/.",format(comedor_infantil,"2f"))
print("la escuela infantil recibe S/.",format(escuela_infantil,"2f"))
print("el asilo de ancianos recibe S/.",format(asilo_ancianos,"2f"))