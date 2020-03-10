#ITC Instituto Tecnologico Nacional de Mexico en Celaya
#by: Sotelo Pacheco José Manuel
#    Villagomez Daniel
#    Peña Martinez Josè Rodrigo
#    Brandon
#Fecha: Jueves 27 de febrero del 2020
#Programación avanzada

import random
from tkinter import *
import tkinter
from tkinter import PhotoImage
from PIL import Image,ImageTk
import time

# values needes for the location of circles
cmin = 0
fmin = 0
cmax = 0
fmax = 0

# constant for idetify gamer
c = 0

# location of game in the matriz
f1 = 8
c1 = 12
f2 = 8
c2 = 12
sl = 0
sb = 0
sl1 = 0
sb1 = 0
# funtion for make circles in the picture

def escaleras():
    global f1
    global f2
    global c1
    global c2
    global m
    

    if m[8][2] == 1:
            m[8][2] = m[8][2] - 1
            m[6][0] = 1
            f1=6
            c1=0

    if m[8][2] == 2:
            m[8][2] = m[8][2] - 2
            m[6][0] = 2
            f2=6
            c2=0
#####################
    if m[8][2] == 3:
            m[8][2] = m[8][2] - 3
            m[6][0] = 3
            f2=6
            c2=0
            f1=6
            c1=0

#####################

    if m[7][3] == 1:
            m[7][3] = m[7][3] - 1
            m[3][1] = 1
            f1=3
            c1=1

    if m[7][3] == 2:
            m[7][3] = m[7][3] - 2
            m[3][1] = 2
            f2=3
            c2=1

    if m[7][3] == 3:
            m[7][3] = m[7][3] - 3
            m[3][1] = 3
            f2=3
            c2=1
            f1=3
            c1=1
            
    if m[7][5] == 1:
            m[7][5] = m[7][5] - 1
            m[5][5] = 1
            f1=7
            c1=5
            
    if m[7][5] == 2:
            m[7][5] = m[7][5] - 2
            m[5][5] = 2
            f2=5
            c2=5
            
    if m[7][5] == 3:
            m[7][5] = m[7][5] - 3
            m[5][5] = 3
            f2=5
            c2=5
            f1=5
            c1=5
            
    if m[7][7] == 1:
            m[7][7] = m[7][7] - 1
            m[4][9] = 1
            f1=4
            c1=9
            
    if m[7][7] == 2:
            m[7][7] = m[7][7] - 2
            m[4][9] = 2
            f2=4
            c2=9

    if m[7][7] == 3:
            m[7][7] = m[7][7] - 3
            m[4][9] = 3
            f2=4
            c2=9
            f1=4
            c1=9
            
    if m[7][12] == 1:
            m[7][12] = m[7][12] - 1
            m[5][10] = 1
            f1=5
            c1=10
            
    if m[7][12] == 2:
            m[7][12] = m[7][12] - 2
            m[5][10] = 2
            f2=5
            c2=10

    if m[7][12] == 3:
            m[7][12] = m[7][12] - 3
            m[5][10] = 3
            f2=5
            c2=10
            f1=5
            c1=10
            
    if m[5][12] == 1:
            m[5][12] = m[5][12] - 1
            m[3][10] = 1
            f1=3
            c1=10
            
    if m[5][12] == 2:
            m[5][12] = m[5][12] - 2
            m[3][10] = 2
            f2=3
            c2=10

    if m[5][12] == 3:
            m[5][12] = m[5][12] - 3
            m[3][10] = 3
            f2=3
            c2=10
            f1=3
            c1=10
            
    if m[5][3] == 1:
            m[5][3] = m[5][3] - 1
            m[2][7] = 1
            f1=2
            c1=7
            
    if m[5][3] == 2:
            m[5][3] = m[5][3] - 2
            m[2][7] = 2
            f2=2
            c2=7

    if m[5][3] == 3:
            m[5][3] = m[5][3] - 3
            m[2][7] = 3
            f2=2
            c2=7
            f1=2
            c1=7
            
    if m[3][8] == 1:
            m[3][8] = m[3][8] - 1
            m[1][10] = 1
            f1=1
            c1=10
            
    if m[3][8] == 2:
            m[3][8] = m[3][8] - 2
            m[1][10] = 2
            f2=1
            c2=10

    if m[3][8] == 3:
            m[3][8] = m[3][8] - 3
            m[1][10] = 3
            f2=1
            c2=10
            f1=1
            c1=10
            
    if m[3][4] == 1:
            m[3][4] = m[3][4] - 1
            m[1][2] = 1
            f1=1
            c1=2
            
    if m[3][4] == 2:
            m[3][4] = m[3][4] - 2
            m[1][2] = 2
            f2=1
            c2=2

    if m[3][4] == 3:
            m[3][4] = m[3][4] - 3
            m[1][2] = 3
            f2=1
            c2=2
            f1=1
            c1=2
            
    if m[1][3] == 1:
            m[1][3] = m[1][3] - 1
            m[5][0] = 1
            f1=5
            c1=0

    if m[1][3] == 2:
            m[1][3] = m[1][3] - 2
            m[5][0] = 2
            f2=5
            c2=0

    if m[1][3] == 3:
            m[1][3] = m[1][3] - 3
            m[5][0] = 3
            f2=5
            c2=0
            f1=5
            c1=0

    if m[1][6] == 1:
            m[1][6] = m[1][6] - 1
            m[3][3] = 1
            f1=3
            c1=3

    if m[1][6] == 2:
            m[1][6] = m[1][6] - 2
            m[3][3] = 2
            f2=3
            c2=3

    if m[1][6] == 3:
            m[1][6] = m[1][6] - 3
            m[3][3] = 3
            f2=3
            c2=3
            f1=3
            c1=3

    if m[2][8] == 1:
            m[2][8] = m[2][8] - 1
            m[8][5] = 1
            f1=8
            c1=5
            
    if m[2][8] == 2:
            m[2][8] = m[2][8] - 2
            m[8][5] = 2
            f2=8
            c2=5
            
    if m[2][8] == 3:
            m[2][8] = m[2][8] - 3
            m[8][5] = 3
            f2=8
            c2=5
            f1=8
            c1=5
            
    if m[3][12] == 1:
            m[3][12] = m[3][12] - 1
            m[5][9] = 1
            f1=5
            c1=9
            
    if m[3][12] == 2:
            m[3][12] = m[3][12] - 2
            m[5][9] = 2
            f2=5
            c2=9

    if m[3][12] == 3:
            m[3][12] = m[3][12] - 3
            m[5][9] = 3
            f2=5
            c2=9
            f1=5
            c1=9
            
    if m[3][9] == 1:
            m[3][9] = m[3][9] - 1
            m[6][9] = 1
            f1=6
            c1=9
            
    if m[3][9] == 2:
            m[3][9] = m[3][9] - 2
            m[6][9] = 2
            f2=6
            c2=9

    if m[3][9] == 3:
            m[3][9] = m[3][9] - 3
            m[6][9] = 3
            f2=6
            c2=9
            f1=6
            c1=9
            
    if m[4][3] == 1:
            m[4][3] = m[4][3] - 1
            m[7][0] = 1
            f1=7
            c1=0
            
    if m[4][3] == 2:
            m[4][3] = m[4][3] - 2
            m[7][0] = 2
            f2=7
            c2=0

    if m[4][3] == 3:
            m[4][3] = m[4][3] - 3
            m[7][0] = 3
            f2=7
            c2=0
            f1=7
            c1=0
            
    if m[6][3] == 1:
            m[6][3] = m[6][3] - 1
            m[7][6] = 1
            f1=7
            c1=6
            
    if m[6][3] == 2:
            m[6][3] = m[6][3] - 2
            m[7][6] = 2
            f2=7
            c2=6

    if m[6][3] == 3:
            m[6][3] = m[6][3] - 3
            m[7][6] = 3
            f2=7
            c2=6
            f1=7
            c1=6
            
    if m[7][8] == 1:
            m[7][8] = m[7][8] - 1
            m[8][11] = 1
            f1=8
            c1=11
            
    if m[7][8] == 2:
            m[7][8] = m[7][8] - 2
            m[8][11] = 2
            f2=8
            c2=11
            
    if m[7][8] == 3:
            m[7][8] = m[7][8] - 3
            m[8][11] = 3
            f2=8
            c2=11
            f1=8
            c1=11
            
    if m[7][4] == 1:
            m[7][4] = m[7][4] - 1
            m[8][7] = 1
            f1=8
            c1=7
            
    if m[7][4] == 2:
            m[7][4] = m[7][4] - 2
            m[8][7] = 2
            f2=8
            c2=7

    if m[7][4] == 3:
            m[7][4] = m[7][4] - 3
            m[8][7] = 3
            f2=8
            c2=7
            f1=8
            c1=7
            
    dibujar()


def dibujar():
	canvas.create_image(0, 0, image=img, anchor=NW) # canvas.create_image(x,y, image = img , ajuste)
	for r in range(0,9):
		for c in range(0,13):
			cmin = c * 10 * zoom
			fmin = r * 10 * zoom
				
			cmax = (c + 1) * 10 * zoom
			fmax = (r + 1) * 10 * zoom

			if m[r][c] == 1: # 1 for player 1
				canvas.create_oval(cmin, fmin, cmax, fmax, width=10, fill='',outline='black')

			if m[r][c] == 2:# 2 for player 2
				canvas.create_oval(cmin, fmin, cmax, fmax, width=10, fill='' , outline = 'blue')

			if m[r][c] == 3:# 3 for player 1 and 2 in the same place
				canvas.create_oval(cmin , fmin , cmax, fmax, width=10, fill='blue',outline='black')

# generate of number random for the player
def generar():
	global c
	global c2
	global c1
	global f1
	global f2
	global sl
	global sb
	global sl1
	global sb1

	c = c + 1
	salto = random.randrange(1,7)
	l1 = Label(ventana , text = salto). grid(column = 1 , row = 0)

	if (f1 > 2) or (f2 > 2): 

#########################################################################################################
#########################################################################################################
################################# PLAYER 1 ##############################################################
#########################################################################################################
		if c == 1:
			if f1 % 2 == 0:
				if ((c1 - salto) < 0 ):
					f1 -= 1

			else:
				if ((c1 + salto) > 12 ):
					f1 -= 1

			if f1 % 2 == 0:
				if sb == 1:
					m[f1][((25 - c1) - salto)] =  1 + m[f1][((25 - c1) - salto)]
					m[f1 + 1][c1] -= 1
					c1 = ((25 - c1) - salto)

				else:
					m[f1][(c1 - salto)] =  1 + m[f1][c1 - salto]
					m[f1][c1] -= 1
					
					c1 = c1 - salto
					sl = 0

				sb = 0
			
			else:
				if sl == 0:
					m[f1][(salto - c1) + (- 1)] =  1 + m[f1][(salto - c1) + (- 1)]
					m[f1 + 1][c1] -= 1
					c1 = (salto - c1) - 1
				
				else:
					m[f1][(c1 + salto)] =  1 + m[f1][c1 + salto]
					m[f1][c1] -= 1
					
					c1 = c1 + salto
					sb = 1 
				sl = 1

#########################################################################################################
#########################################################################################################
################################# PLAYER 2 ##############################################################
#########################################################################################################

		else:
			if f2 % 2 == 0:
				if ((c2 - salto) < 0 ):
					f2 -= 1

			else:
				if ((c2 + salto) > 12 ):
					f2 -= 1

			if f2 % 2 == 0:
				if sb1 == 1:
					m[f2][((25 - c2) - salto)] =  2 + m[f2][((25 - c2) - salto)]
					m[f2 + 1][c2] -= 2
					c2 = ((25 - c2) - salto)

				else:
					m[f2][(c2 - salto)] =  2 + m[f2][c2 - salto]
					m[f2][c2] -= 2
					
					c2 = c2 - salto
					sl1 = 0

				sb1 = 0
			
			else:
				if sl1 == 0:
					m[f2][(salto - c2) + (- 1)] =  2 + m[f2][(salto - c2) + (- 1)]
					m[f2 + 1][c2] -= 2
					c2 = (salto - c2) - 1
				
				else:
					m[f2][(c2 + salto)] =  2 + m[f2][c2 + salto]
					m[f2][c2] -= 2
					
					c2 = c2 + salto
					sb1 = 1 
				sl1 = 1
			c = 0

		dibujar()
		
		escaleras()

	else:

#########################################################################################################
#########################################################################################################
################################# PLAYER 1 ##############################################################
#########################################################################################################
		if c == 1:
			if f1 % 2 == 0:
				if ((c1 - salto) < 0 ):
					f1 -= 1

			else:
				if ((c1 + salto) > 12 ):
					f1 -= 1

			if f1 % 2 == 0:
				if sb == 1:
					m[f1][((25 - c1) - salto)] =  1 + m[f1][((25 - c1) - salto)]
					m[f1 + 1][c1] -= 1
					c1 = ((25 - c1) - salto)

				else:
					m[f1][(c1 - salto)] =  1 + m[f1][c1 - salto]
					m[f1][c1] -= 1
					
					c1 = c1 - salto
					sl = 0

				sb = 0
			
			else:
				if sl == 0:
					m[f1][(salto - c1) + 1] =  1 + m[f1][(salto - c1) + 1 ]
					m[f1 + 1][c1] -= 1
					c1 = (salto - c1) + 1
				
				else:
					m[f1][(c1 + salto)] =  1 + m[f1][c1 + salto]
					m[f1][c1] -= 1
					
					c1 = c1 + salto
					sb = 1 
				sl = 1

#########################################################################################################
#########################################################################################################
################################# PLAYER 2 ##############################################################
#########################################################################################################

		else:
			if f2 % 2 == 0:
				if ((c2 - salto) < 0 ):
					f2 -= 1

			else:
				if ((c2 + salto) > 12 ):
					f2 -= 1

			if f2 % 2 == 0:
				if sb1 == 1:
					m[f2][((25 - c2) - salto)] =  2 + m[f2][((25 - c2) - salto)]
					m[f2 + 1][c2] -= 2
					c2 = ((25 - c2) - salto)

				else:
					m[f2][(c2 - salto)] =  2 + m[f2][c2 - salto]
					m[f2][c2] -= 2
					
					c2 = c2 - salto
					sl1 = 0

				sb1 = 0
			
			else:
				if sl1 == 0:
					m[f2][(salto - c2) +  1 ] =  2 + m[f2][(salto - c2) +  1]
					m[f2 + 1][c2] -= 2
					c2 = (salto - c2) + 1
				
				else:
					m[f2][(c2 + salto)] =  2 + m[f2][c2 + salto]
					m[f2][c2] -= 2
					
					c2 = c2 + salto
					sb1 = 1 
				sl1 = 1
			c = 0

		dibujar()

		escaleras()



zoom = 7 # ampliar la visualizacion de la pantall

# matrix needes for all the posibilities in the picture for boxes
m = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0,0,0,0,0,0,0]]

# game start
m[8][12] = 3

canvas = Canvas(width=130 * zoom, height=91 * zoom, bg='white')
canvas.pack(expand=YES, fill=BOTH)

img = Image.open('s.png')
img = img.resize((130 * zoom, 91 * zoom), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
dibujar()
escaleras()

ventana = Tk()
l1 = Label(ventana , text = "" ).grid(column  = 1 , row = 0)
b1 = Button(ventana , text = "Generar", command = generar).grid(column = 0 , row = 0)

mainloop()
