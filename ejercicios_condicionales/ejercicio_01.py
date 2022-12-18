#Ejercicio 1
'''Una tienda vende un producto a precios unitarios que dependen de la 
cantidad de unidades adquiridas. Adicionalmente, si el cliente adquiere
 más de 50 unidades la tienda le descuenta el 15% del importe de la compra; 
 en caso contrario, sólo le descuenta el 5%. Desarrolle el programa que determine el
 importe de la compra, el descuento y el total a pagar por la compra de cierta cantidad de unidades del producto. '''

unidades = int(input("unidades"))
#solucion de los datos 
precio = 25
if unidades <= 25 : precio = 27
elif unidades >= 51 : precio = 23
print (f"precio = {precio}\n")

compra = unidades * precio
print (f"compra = {compra}\n")
descuento = (0.15 if unidades > 50 else 0.05) * compra
print (f"descuento = {precio}\n")
print (f"total = {compra - descuento}\n")