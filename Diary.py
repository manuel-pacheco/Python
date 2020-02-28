import time
from datetime import datetime
#sino tienen instalado la libreria tkinter instalarla
from tkinter import *



#Creación de ventana principal
ventana = Tk()
miFrame=Frame(ventana, width=1200, height=600)
miFrame.pack()

def reloj():
    ahora = datetime.now()
    #Diccionarios de días y meses
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    dias = {
        0: "Domingo",
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
    }

    ahora = datetime.now()
    numero_mes = ahora.month
    # A entero para quitar los ceros a la izquierda en caso de que existan
    numero_dia = int(ahora.strftime("%w"))
    # Leer diccionario
    dia = dias.get(numero_dia)
    mes = meses.get(numero_mes)
    # Formatear
    fecha = "{}, {} de {} del {}".format(dia, ahora.day, mes, ahora.year)
    hora = ahora.strftime(fecha + "\t %H:%M:%S")
    etiqueta.configure(text=hora)
    etiqueta.after(1000,reloj)

etiqueta = Label(miFrame, font="arial 20 bold", bg="blue violet", fg="lime green")
etiqueta.grid(columnspan =10,row=0)

if __name__ == "__main__":
    reloj()
    
#img = Image.open("C:\LogoItc.png")
#new_img = img.resize((256,256))
#widget = Label(miFrame,image= new_img)
#widget.grid(row=0, column=6)


######## Creación de Label para días #########
direccionLabel=Label(miFrame, text="lunes")
direccionLabel.grid(row=3, column=1, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Martes")
direccionLabel.grid(row=3, column=2, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Miercoles")
direccionLabel.grid(row=3, column=3, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Jueves")
direccionLabel.grid(row=3, column=4, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Viernes")
direccionLabel.grid(row=3, column=5, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Sabado")
direccionLabel.grid(row=3, column=6, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Domingo")
direccionLabel.grid(row=3, column=7, sticky="e", padx=10, pady=10)

######## Creación de Label para Horas #########
direccionLabel=Label(miFrame, text="00:00  02:00")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="02:00  04:00")
direccionLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="04:00  06:00")
direccionLabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="06:00  08:00")
direccionLabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="08:00  10:00")
direccionLabel.grid(row=8, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="10:00  12:00")
direccionLabel.grid(row=9, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="12:00  14:00")
direccionLabel.grid(row=10, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="14:00  16:00")
direccionLabel.grid(row=11, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="16:00  18:00")
direccionLabel.grid(row=12, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="18:00  20:00")
direccionLabel.grid(row=13, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="20:00  22:00")
direccionLabel.grid(row=14, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="22:00  24:00")
direccionLabel.grid(row=15, column=0, sticky="e", padx=10, pady=10)

############ Creacion de label para texto ############
for i in [1,2,3,4,5,6,7]:  # cantidades en especifico
    for x in range (4,16): # desde una cantidad hasta otra
        ventanas=Entry(miFrame)
        ventanas.grid(row=x, column= i, padx=10, pady=10)
        
ventana.mainloop()
