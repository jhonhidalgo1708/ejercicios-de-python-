#ejercicio 5
import os
os.system("cls")

'''Desarrolle el programa que dada la capacidad de un disco duro
 en gigabytes, lo convierta amegabytes, kilobytes y bytes.
  1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB'''

#impresion de los datos 

capacidad_en_GB = float (input ('Ingresa el valor de capacidad en GB: '))
capacidad_en_MB=capacidad_en_GB*1024

print ('Valor de capacidad en MB: ' + repr (capacidad_en_MB))
capacidad_en_KB=capacidad_en_MB*1024
print ('Valor de capacidad en KB: ' + repr (capacidad_en_KB))
capacidad_en_B=capacidad_en_KB*1024
print ('Valor de capacidad en B: ' + repr (capacidad_en_B))
print ('Valor de capacidad en KB: ' + repr (capacidad_en_KB))
