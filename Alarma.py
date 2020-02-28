import time
from tkinter import *
from datetime import datetime


class alarma:
    def __init__(self):
        pass
    
    def alarma(self,op,hora,minutos):
        if(op ==  1):
            print("La alarma esta programada para las 6:30")
            h=6
            ho = 24 -hora + h
            print("tiempo faltante: ",ho,"horas")

        if (op == 2):
            print("La alarma esta programada para las 8:30")
            h = 8
            ho = 24 - hora + h
            print("tiempo faltante aprox: ", ho, "horas")

        if (op == 3):
            print("La alarma esta programada para las 9:30")
            h = 9
            ho = 24 - hora + h
            print("tiempo faltanteaprox: ", ho, "horas")

        if (op == 4):
            print("La alarma esta programada para las 10:30")
            h = 10
            ho = 24 - hora + h
            print("tiempo faltante aprox: ", ho, "horas")


ahora = datetime.now()
hora = ahora.hour
print("La hora es: ", hora)
minutos = ahora.minute
print("Los minutos son: ", minutos)

O1 = alarma()
op2 = int(input("Teclee algun numero del 0 al 9 para acceder a la alarma: "))
time.sleep(2)
O1.alarma(op2, hora, minutos)


