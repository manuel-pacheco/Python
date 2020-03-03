#in this program you can play cat 

from tkinter import *
from tkinter import messagebox

m = [0,0,0],[0,0,0],[0,0,0]
Count = 0
Count2 = 0

#Creación de ventana principal
class resultado():
	def __init__(self):
		pass
	
	def variables(self , a, b):
		global Count
		global Count2
		global m
		Count = Count + 1

		if(Count == 1):
			Count2 += 1
			l1 = Label(miFrame , text = "X" , font = "arial 35", width = 3 , height = 1).grid( column = a , row = b )
			m[a][b] = 1

		else:
			Count2 += 1
			l1 = Label(miFrame , text = "O" ,  font = "arial 35", width = 3 , height = 1).grid( column = a , row = b )
			m[a][b] = 2
			
		if(Count == 2):
			Count = 0

		if(Count2 > 4):
			calculo()
		if(Count2 == 9):
			MsgBox= messagebox.askquestion ('Resultasos','NADIE GANO' + "\n ¿Desea continuar?",icon = 'warning')

		muestra()

def borrar():
	ventana.destroy()
	ventana = Tk()

def muestra():
	global Count2
	global m 

	if(Count2 == 9):
		for f in range(0,3):
			for c in range(0,3):
				print (m[c][f], end = "")
			print()
		

	
def calculo(): 
	global m
	global Count2
	# Para posibles convinaciones con lineas rectas
	if( (m[0][0]  == m[1][0]) and  (m[0][0] == m[2][0]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[0][0]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()
	elif( (m[0][1]  == m[1][1]) and  (m[0][1] == m[2][1]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[0][1]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()
	elif( (m[0][2]  == m[1][2]) and  (m[0][2] == m[2][2]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[0][2]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()
	elif( (m[0][0]  == m[0][1]) and  (m[0][0] == m[0][2]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[0][0]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()
	elif( (m[1][0]  == m[1][1]) and  (m[1][0] == m[1][2]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[1][0]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()
	elif( (m[2][0]  == m[2][1]) and  (m[2][0] == m[2][2]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[2][0]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()
	# Para posibles convinaciones con diagonales 
	elif( (m[0][0]  == m[1][1]) and  (m[0][0] == m[2][2]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[0][0]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()
	elif( (m[2][0]  == m[1][1]) and  (m[2][0] == m[0][2]) ):
		print(Count2)
		MsgBox= messagebox.askquestion ('Resultasos','EL ganador es el jugador' + str(m[2][0]) + "\n ¿Desea continuar?",icon = 'warning')
		if MsgBox == 'no':
			ventana.destroy()
		else: 
			borrar()


def b1():
	resultado().variables(0,0)
def b2():
	resultado().variables(1,0)
def b3():
	resultado().variables(2,0)
def b4():
	resultado().variables(0,1)
def b5():
	resultado().variables(1,1)
def b6():
	resultado().variables(2,1)
def b7():
	resultado().variables(0,2)
def b8():
	resultado().variables(1,2)
def b9():
	resultado().variables(2,2)

ventana = Tk()
miFrame = Frame(ventana, width=1200, height=600)
miFrame.pack()


b1 = Button(miFrame , command = b1, width = 10 , height = 5).grid( column = 0, row = 0)
b2 = Button(miFrame , command = b2, width = 10 , height = 5).grid( column = 1, row = 0)
b3 = Button(miFrame , command = b3, width = 10 , height = 5).grid( column = 2, row = 0)
b4 = Button(miFrame , command = b4, width = 10 , height = 5).grid( column = 0, row = 1)
b5 = Button(miFrame , command = b5, width = 10 , height = 5).grid( column = 1, row = 1)
b6 = Button(miFrame , command = b6, width = 10 , height = 5).grid( column = 2, row = 1)
b7 = Button(miFrame , command = b7, width = 10 , height = 5).grid( column = 0, row = 2)
b8 = Button(miFrame , command = b8, width = 10 , height = 5).grid( column = 1, row = 2)
b9 = Button(miFrame , command = b9, width = 10 , height = 5).grid( column = 2, row = 2)


miFrame.mainloop()