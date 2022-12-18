#ejercicio 18

'''18.	En una tienda han puesto en oferta la venta de todos sus
 artículos por cambio de estación ofreciendo un 15% + 15% de descuento. 
 El primer 15% se aplica al importe de la compra, mientras que el segundo 
 15% se aplica al importe que resulta de restar el importe de la compra menos el primer descuento.
Dada la cantidad de unidades adquiridas de un mismo tipo de artículo
 por parte de un cliente y el precio unitario del artículo. 
Desarrolle el programa que determine el importe de la compra, el descuento y el importe a pagar.'''

#datos propuestos

cantidad_de_propruductos=float(input("cantidad de unidades adqueridas"))
precio_unitario=float(input("ingresar el precio del articulo"))

#solucion 
importe_compra=precio_unitario*cantidad_de_propruductos
print ('el importe de la compra: ',importe_compra,"S/")
primer_descuento=importe_compra*0.15
print ('el importe del primer descuento : ',primer_descuento,"S/")
segundo_descuento=(importe_compra-primer_descuento)+0.15
print ('el importe del primer segundo descuento : ',segundo_descuento,"S/")
importe_a_pagar= importe_compra-primer_descuento -segundo_descuento
print ('el importe a pagar  : ',importe_a_pagar,"S/")