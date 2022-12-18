#ejercicio15
import os
os.system("cls")
'''Juan, Rosa y Daniel aportan cantidades de dinero para formar un capital.
Juan y Rosa aportan en dólares y Daniel, en soles. Desarrolle el programa
que determine el capital total en dólares y que porcentaje de dicho capital
aporta cada uno. Dólar = S/. 3.00 nuevos soles.'''

dinero_juan=float(input("dinero de juan"))
dinero_rosa=float(input(" dinero de rosa"))
dinero_daniel=float(input("dinero de daniel "))

dolares_daniel=dinero_daniel/3
capital_total=dinero_juan+dinero_rosa+dolares_daniel
print("el capital total: $",format(capital_total,".2f"))
porcentaje_juan=(dinero_juan*100)/capital_total
print("juan aporto",format(porcentaje_juan,".2f"),"%")
porcentaje_rosa=(dinero_rosa*100)/capital_total
print("rosa aporto",format(porcentaje_rosa,".2f"),"%")
porcentaje_danie=(dolares_daniel*100)/capital_total
print("daniel aporto",format(porcentaje_danie,".2f"),"%")