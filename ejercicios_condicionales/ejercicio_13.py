#ejercicio13
#Inicio
   # Declaración de variables entero numero, u, d, c
   # Leer numero
numero=int(input("digite en numero"))

if numero >= 100 and numero <= 999:

       # Determina las cifras del número
       c = numero/100
       d = (numero%100)/10
       u = numero%10
       #Determina si las cifras del número son o no consecutivas
       if((d == c+1 and u == d+1) (d == c-1 and u == d-1)):
           resultado = "Las cifras del número son consecutivas"
       else:
           resultado = "Las cifras del número no son consecutivas"
       # Salida de resultados
    
print("El número debe ser positivo de tres cifras",resultado)
