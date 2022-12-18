#Ejercicio 3
'''3.	Los ángulos se clasifican de la siguiente manera: nulo (0°),
 Agudo (0°< x < 90°), Recto (90°), Obtuso (90° < x <180°), Llano (180°), Cóncavo (180°< x < 360°), 
Completo (360°). Desarrolle el programa que determine la clasificación
 de un ángulo dado en grados.'''

#datos obtenidos 

angulo =  int(input("digite el ángulo: "))

#operacion 

if angulo == 0:
    print("El ángulo es nulo")

if angulo == 90:
    print("El angulo es recto")

if angulo == 360:
    print("El angulo es completo")

if angulo == 180:
    print("El angulo es llano")

if 0 < angulo < 90:
    print("El angulo es agudo")

if 90 < angulo < 180:
    print("El angulo es obtuso")

if 180 < angulo < 360:
    print("El angulo es cóncavo")