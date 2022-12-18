# CONDICIONALES

'''Una tienda vende un producto a un precio unitario igual a S/. 20. 
Como oferta la tienda ofrece un porcentaje de 
descuento sobre el importe de la compra. Adicionalmente la tienda
 regala caramelos en base al número de unidades 
adquiridas del producto. Desarrolle el programa que determine el 
importe de la compra, el descuento, total a pagar 
y el número de caramelos del obsequio que se da al
 cliente por la compra realizada. '''

#presentacion de los datos obtenidos 
numero_unidades = float(input("ingrese la cantidad de productos: "))

#solucion de los datos 

if numero_unidades>= 1 and numero_unidades <= 50:
    print(" vamsos a regalo de 5 caramelos")
elif numero_unidades >= 51 and numero_unidades <= 100:
    print("vamos a regalo de 10 caramelos")

else: 
    print("vamos a regalo de 15 caramelos")
importe = numero_unidades * 20



if importe> 700:
    descuento = importe * 0.16
    totalidad_a_pagar = importe - descuento  
    print(f"el descuento es  {totalidad_a_pagar: 2f}")

elif importe< 700 and importe> 501:
    descuento= importe * 0.14
    totalidad_a_pagar= importe - descuento  
    print(f"el descuento es {totalidad_a_pagar: 2f}")

else :
    descuento= importe * 0.12
    totalidad_a_pagar = importe - descuento  
    print(f"el descuento es {totalidad_a_pagar: 2f}")