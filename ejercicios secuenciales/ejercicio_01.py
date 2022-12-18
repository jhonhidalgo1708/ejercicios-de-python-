#inicio
import os
"1.	Desarrolle el programa que determine el porcentaje de varones y de mujeres que hay en un salón de clases."
os.system("cls")
#imprecion de los datos 
mujeres=int(input("dicte el porcentaje de mujeres:"))
varones=int(input("dicte el porcentaje de varones:"))

total=varones+mujeres
porcentaje_varones=int((varones*100)/total)
print("el porcentaje de varones es",porcentaje_varones,"%")
porcentaje_mujeres=int((mujeres*100)/total)
print("el porcentaje de mujeres es",porcentaje_mujeres,"%")
