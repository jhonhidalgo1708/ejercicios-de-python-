#ejercicio16
'''	El cálculo del pago mensual de un empleado de una empresa se efectúa de la 
siguiente manera: el sueldo básico se calcula sobre la base del número total de
 horas trabajadas basado en una tarifa horaria, al sueldo básico, se le aplica una 
 bonificación del 20% obteniéndose el sueldo bruto; al sueldo bruto, se le aplica 
 un descuento del 10% obteniéndose el sueldo neto. Desarrolle el programa que
  muestre el sueldo básico, 
bruto y neto de un trabajador.'''

horasTrab=float(input("Ingrese horas de trabajo: "))
tarifaHor=float(input("Ingrese la tarifa de horas: "))

sueldoBas = horasTrab*tarifaHor
montoBoni = 0.20*sueldoBas
print("sueldo basico ",sueldoBas)
sueldoBru = sueldoBas+montoBoni
print("sueldo bruto ",sueldoBru)
montoDesc = 0.10*sueldoBru
sueldoNet = sueldoBru-montoDesc
print("sueldo neto" ,sueldoNet)