#ITC Instituto Tecnologico Nacional de Mexico en Celaya
#by: 
#-----Martínez Ramírez Brandon Yoel
#-----Peña Martínez José Rodrigo
#-----Sotelo Pacheco José Manuel
#-----Villagómez González Daniel

#Fecha: Viernes 13 de marzo del 2020
#Programación Avanzada

#Programa del juego de la ruleta, donde puedas apostar lo minimo, monto inicial, mantener tu apuesta
#retirar, jugar todo y apuesta dividida.

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import random

global r 
global mon
global sub
global numero
global subi

m = 0
s = 0
p = 0
o=0
n=0
F=0

def cerrar(nu):
	global mon
	global sub
	global mnn

	if nu == 1:
		mon.withdraw()
		BApostar=Button(ventana,text="MONTO INICIAL",bg="black",fg= "white" ,bd="5", font = "arial 10 bold", width = 15 , height = 1, command = monto , state = "disabled").grid(column=4,row=0)

		
	elif nu == 2:
		sub.withdraw()
		BApueMin=Button(ventana,text="APUESTA MINÍMA",bg="black",bd="5",fg= "white", font = "arial 10 bold", width = 15 , height = 1, command = apuesta , state = "disabled").grid(column=5,row=0)
	elif nu == 3:
		p = M.get() + y.get()
		y.set(p)
		mnn.withdraw()
		

def casilla(num):
	global numero
	L3= Label(ventana , text = "Casilla:", font = "arial 15", width = 12 , height = 1).grid( row = 6, column = 4)
	E3 = Label(ventana , text = "     ",font = "arial 15",justify="center").grid( row = 6 , column = 5)
	E3 = Label(ventana , text = num,font = "arial 15",justify="center").grid( row = 6 , column = 5)
	numero = num

def monto():
	global mon
	global X1

	X1 = IntVar()

	mon = Toplevel()
	l1 = Label(mon , text = "Teclee su monto inicial:  ",font = "arial 15",justify="center").grid( row = 0 , column = 0 )
	
	r1= Entry(mon , textvariable = X1,font = "arial 15",justify="center").grid( row = 0, column = 1)
	b1 = Button(mon , text = "OK", command = lambda: cerrar(1), font = "arial 15", justify="center").grid( row = 1 , columnspan = 2)
	
	L1= Label(ventana , text = "Disponible:", font = "arial 15", width = 12 , height = 1).grid( row = 4 , column = 4)
	E1 = Entry(ventana , textvariable = X1,font = "arial 15",justify="center", state = "disabled").grid( row =4 , column = 5)


def subir():
	global mnn
	global s
	global M

	M = IntVar()
	mnn = Toplevel()
	l1 = Label(mnn , text = "Ingrese cantidad extra:  ",font = "arial 15",justify="center").grid( row = 0 , column = 0 )
	
	r1= Entry(mnn , textvariable = M,font = "arial 15",justify="center")
	r1.grid( row = 0, column = 1)
	b1 = Button(mnn , text = "OK", command = lambda: cerrar(3), font = "arial 15", justify="center").grid( row = 1 , columnspan = 2)
	

def mantener():
	pass

def retirar():

	texto=X1.get()
	ser=Label(ventana,text="TE RETIRAS CON: ",font = "arial 15",justify="center").grid(column=5,row=8)
	ser=Label(ventana,text="$",font = "arial 15",justify="center").grid(column=4,row=9)
	Ganar=Label(ventana,text=texto,font = "arial 15",justify="center").grid(column=5,row=9)
	cerra=Button(ventana,text="ADIOS JUGADOR \n VUELVE PRONTO",font = "arial 10",justify="center",command=destruir,bg="gold",fg="black").grid(column=5,row=10)

def destruir():
	ventana.destroy()

def apuesta():
	global sub
	global y

	y = IntVar()
	sub = Toplevel()
	l2 = Label(sub , text = "Cuanto desea subir:  ",font = "arial 15",justify="center").grid( row = 0 , column = 0 )
	
	r2 = Entry(sub , textvariable = y,font = "arial 15",justify="center").grid( row = 0, column = 1)
	b2 = Button(sub , text = "OK", command = lambda: cerrar(2), font = "arial 15", justify="center").grid( row = 1 , columnspan = 2)
	
	L1= Label(ventana , text = "Apuesta:", font = "arial 15", width = 12 , height = 1).grid( row = 5 , column = 4)
	E1 = Entry(ventana , textvariable = y,font = "arial 15",justify="center", state = "disabled").grid( row =5 , column = 5)
	
def only():
	y.set(X1.get())

def ap():
	pass

def jugar():
	global numero
	F=0 
	m = X1.get()
	n = y.get()
	salto = random.randrange(0,38)

	L4= Label(ventana , text = "Num :", font = "arial 15", width = 12 , height = 1).grid( row = 7, column = 4)
	E4 = Label(ventana , text = "     ",font = "arial 15",justify="center").grid( row = 7 , column = 5)
	E4 = Label(ventana , text = salto,font = "arial 15",justify="center").grid( row = 7 , column = 5)

	if var.get() == 1:
		if numero == salto:
			s = n*36 + m
			X1.set(s)
			s = 0
		else:
			print(n)
			print(m)
			s = m - n
			print(s)
			X1.set(s)

#######par o impar ##################
	if var.get() != 1:
		if salto % 2 == 0 :
			if var.get() == 2:
				L3= Label(ventana , text = "      	", font = "arial 15", width = 12 , height = 1).grid( row = 6, column = 4)
				E3 = Label(ventana , text = "        ",font = "arial 15",justify="center").grid( row = 6 , column = 5)
				s = n + m
				X1.set(s)
				F=s
				s = 0
			else:
				L3= Label(ventana , text = "      	", font = "arial 15", width = 12 , height = 1).grid( row = 6, column = 4)
				E3 = Label(ventana , text = "        ",font = "arial 15",justify="center").grid( row = 6 , column = 5)
				s = X1.get() - y.get() 
				X1.set(s)
				F=s
				s = 0

		else:
			if var.get() == 3:
				L3= Label(ventana , text = "      	", font = "arial 15", width = 12 , height = 1).grid( row = 6, column = 4)
				E3 = Label(ventana , text = "        ",font = "arial 15",justify="center").grid( row = 6 , column = 5)
				s = n + m
				X1.set(s)
				F=s
				s = 0
			else:
				L3= Label(ventana , text = "      	", font = "arial 15", width = 12 , height = 1).grid( row = 6, column = 4)
				E3 = Label(ventana , text = "        ",font = "arial 15",justify="center").grid( row = 6 , column = 5)
				s = X1.get() - y.get() 
				X1.set(s)
				F=s
				s = 0
	if F<=0:
		messagebox.showerror("Monto insuficiente","Favor de retirarse") 
		ventana.destroy()  
				
#################################

def boton():

	if var.get() == 1:
		A = "normal"
	else:
		A = "disabled"

	B0=Button(ventana,text="0",fg="white",bg="green", font = "arial 15", width = 3 , height = 1 , command = lambda:casilla(0) , state = A).grid(column=0,row=0)
	B00=Button(ventana,text="00",fg="white",bg="green", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(00), state = A).grid(column=1,row=0)
	B1=Button(ventana,text="1",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(1), state = A).grid(column=0,row=1)
	B2=Button(ventana,text="2",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(2), state = A).grid(column=1,row=1)
	B3=Button(ventana,text="3",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(3), state = A).grid(column=2,row=1)
	B4=Button(ventana,text="4",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(4), state = A).grid(column=0,row=2)
	B5=Button(ventana,text="5",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(5), state = A).grid(column=1,row=2)
	B6=Button(ventana,text="6",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(6), state = A).grid(column=2,row=2)
	B7=Button(ventana,text="7",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(7), state = A).grid(column=0,row=3)
	B8=Button(ventana,text="8",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(8), state = A).grid(column=1,row=3)
	B9=Button(ventana,text="9",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(9), state = A).grid(column=2,row=3)
	B10=Button(ventana,text="10",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(10), state = A).grid(column=0,row=4)
	B10=Button(ventana,text="11",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(11), state = A).grid(column=1,row=4)
	B12=Button(ventana,text="12",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(12), state = A).grid(column=2,row=4)
	B13=Button(ventana,text="13",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(13), state = A).grid(column=0,row=5)
	B14=Button(ventana,text="14",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(14), state = A).grid(column=1,row=5)
	B15=Button(ventana,text="15",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(15), state = A).grid(column=2,row=5)
	B16=Button(ventana,text="16",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(16), state = A).grid(column=0,row=6)
	B17=Button(ventana,text="17",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(17), state = A).grid(column=1,row=6)
	B18=Button(ventana,text="18",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(18), state = A).grid(column=2,row=6)
	B19=Button(ventana,text="19",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(19), state = A).grid(column=0,row=7)
	B20=Button(ventana,text="20",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(20), state = A).grid(column=1,row=7)
	B21=Button(ventana,text="21",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(21), state = A).grid(column=2,row=7)
	B22=Button(ventana,text="22",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(22), state = A).grid(column=0,row=8)
	B23=Button(ventana,text="23",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(23), state = A).grid(column=1,row=8)
	B24=Button(ventana,text="24",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(24), state = A).grid(column=2,row=8)
	B25=Button(ventana,text="25",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(25), state = A).grid(column=0,row=9)
	B26=Button(ventana,text="26",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(26), state = A).grid(column=1,row=9)
	B27=Button(ventana,text="27",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(27), state = A).grid(column=2,row=9)
	B28=Button(ventana,text="28",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(28), state = A).grid(column=0,row=10)
	B29=Button(ventana,text="29",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(29), state = A).grid(column=1,row=10)
	B30=Button(ventana,text="30",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(30), state = A).grid(column=2,row=10)
	B31=Button(ventana,text="31",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(31), state = A).grid(column=0,row=11)
	B32=Button(ventana,text="32",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(32), state = A).grid(column=1,row=11)
	B33=Button(ventana,text="33",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(33), state = A).grid(column=2,row=11)
	B34=Button(ventana,text="34",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(34), state = A).grid(column=0,row=12)
	B35=Button(ventana,text="35",fg="white",bg="black", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(35), state = A).grid(column=1,row=12)
	B36=Button(ventana,text="36",fg="white",bg="red", font = "arial 15", width = 3 , height = 1, command = lambda:casilla(36), state = A).grid(column=2,row=12)


ventana=Tk()
ventana.title("Juego de la Ruleta")

q=("white")
z=("arial 10 bold")
BApostar=Button(ventana,text="MONTO INICIAL",bg="black",fg=q,bd="5", font = z, width = 15 , height = 1, command = monto).grid(column=4,row=0)
BSubir=Button(ventana,text="SUBIR APUESTA",bg="black",fg=q,bd="5" ,font = z, width = 15 , height = 1, command = subir).grid(column=4,row=1)
BRetirar=Button(ventana,text="RETIRAR",bg="black",fg=q,bd="5", font = z, width = 15 , height = 1, command = retirar).grid(column=6,row=0)
BApueMin=Button(ventana,text="APUESTA MINÍMA",bg="black",bd="5",fg=q, font = z, width = 15 , height = 1, command = apuesta).grid(column=5,row=0)
BOnli=Button(ventana,text="ALL-IN",bg="black",fg=q,bd="5", font = z, width = 15 , height = 1, command = only).grid(column=5,row=1)
BApuDiv=Button(ventana,text="Jugar",bg="black",fg=q, bd="5",font = z, width = 15 , height = 1, command = jugar).grid(column=6,row=1)

var = IntVar()
var.set(1)
boton()


Rad = Radiobutton(ventana , text = "Juego por casillas" , variable = var ,value = 1 , command = boton ).grid( row = 2 , column = 6)
Rad = Radiobutton(ventana , text = "Juego por pares" , variable = var ,value = 2 , command = boton).grid( row = 2 , column = 5)
Rad = Radiobutton(ventana , text = "Juego por impares" , variable = var ,value = 3, command = boton).grid( row = 2 , column = 4)

mainloop()
