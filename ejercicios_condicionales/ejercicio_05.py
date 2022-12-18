#Ejercicio 5 
'''Desarrolle el programa que dado un número de 4 cifras, 
forme el mayor número posible de dos cifras usando 
la mayor y menor cifra del número ingresado.'''



#datos obtenidos
numero = input("Ingrese el numero de 4 cifras: ")



# solucion 
#si
if len(numero) !=4:
    print("El numero debe ser de 4 cifras")
#sino
else:
    cifra_men = 10;
    cifra_may = 0;

    for cifra in numero:
        if (int(cifra) < cifra_men):
            cifra_men = int(cifra);

        elif (int(cifra) > cifra_may):
            cifra_may = int(cifra);



    
    print(f"El mayor número posible es: {str(cifra_may)}{str(cifra_men)}");