#ejercicio 25
'''	Una empresa ha decidido otorgar una
 bonificación por fiestas patrias a sus empleados.
  Si el empleado tiene más de un hijo, recibirá una
   bonificación igual al 12.5% de su sueldo bruto más 
   S/. 40 por cada hijo; en caso contrario, solo recibirá
    una bonificación del 10%. Elaborar el programa que muestre 
    la bonificación y el sueldo neto a pagar'''



montototal_vendido=int(input(" monto total vendido:"))
#solucion 
int
#si
if (montototal_vendido>500):
    sueldo=0.10*montototal_vendido+25*(montototal_vendido/500)
    #sino
else:
    sueldo=0.10*montototal_vendido
    print("el sueldo seria .",sueldo)  