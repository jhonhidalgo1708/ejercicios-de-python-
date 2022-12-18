#ejercicio 19 
'''19.	Una empresa paga a sus vendedores un sueldo 
básico mensual de S/. 500. El sueldo bruto es igual al 
sueldo básico más una comisión, que es igual al 9% del
 monto total vendido. Por ley, todo vendedor se somete a
  un descuento del 11%. Desarrolle el 
programa que calcule la comisión, el sueldo bruto, 
el descuento y el sueldo neto de un vendedor de la empresa.'''



monVendido=float(input("monto vendido"))


#solucion 



comisión = monVendido*0.09
sbruto = 300 + comisión
descuento = sbruto * 0.11
sneto = sbruto - descuento




print("comision ",comisión)
print("sueldo bruto",sbruto,)
print("descuento ",descuento)
print("sueldo neto ",sneto)