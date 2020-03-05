#ITC Instituto Tecnologico Nacional de Mexico en Celaya
#by: Sotelo Pacheco José Manuel
#Fecha: Jueves 27 de febrero del 2020
#Programación avanzada


from tkinter import *
import tkinter
from tkinter import PhotoImage
from PIL import Image,ImageTk

cm = 5 #cantidad de columnas en la matriz
fm = 5 #cantidad de filas en la matriz


def updat():
    global r
    global c
    global cm
    global fm

    c = 2
    r = 2

    for ro in range(0,fm):
        for co in range(0,cm):
            l2 = Label(miFram, text = "", font = "arial 35", width = 3 , height = 1).grid( column = co , row = ro)    
    
    l1= Label(miFram, text = "    " , font = "arial 35" , bg = "black").grid( column = c , row = r )

def up():
    global r
    global c
    global cm
    global fm

    if r == 0:
        l1= Label(miFram, text = "    " , font = "arial 35").grid( column = c , row = r )
        r = r + 4
        l1= Label(miFram, text = "    " , font = "arial 35" , bg = "black").grid( column = c , row = r )
    
    else: 
        l1= Label(miFram, text = "    " , font = "arial 35").grid( column = c , row = r )
        r = r - 1
        l1= Label(miFram, text = "    " , font = "arial 35" , bg = "black").grid( column = c , row = r )

def down():
    global r
    global c
    global cm
    global fm

    if r == fm -1 :
        l1= Label(miFram, text = "    " , font = "arial 35").grid( column = c , row = r )
        r = r -4
        l1= Label(miFram, text = "    " , font = "arial 35" , bg = "black").grid( column = c , row = r )
    
    else:
        l1= Label(miFram, text = "    " , font = "arial 35").grid( column = c , row = r )
        r = r + 1
        l1= Label(miFram, text = "    " , font = "arial 35" , bg = "black").grid( column = c , row = r )

def left():
    global r
    global c
    global cm
    global fm

    if c == 0:
        l1= Label(miFram, text = "    " , font = "arial 35"  ).grid( column = c , row = r )
        c = c +4
        l1= Label(miFram, text = "    " , font = "arial 35" , bg = "black").grid( column = c , row = r )

    else:
        l1= Label(miFram, text = "    " , font = "arial 35"  ).grid( column = c , row = r )
        c = c -1
        l1= Label(miFram, text = "    " , font = "arial 35" , bg = "black").grid( column = c , row = r )

def right():
    global r
    global c
    global cm
    global fm

    if c == cm - 1:
        l1= Label(miFram, text = "    " , font = "arial 35" ).grid( column = c , row = r )
        c = c -4
        l1= Label(miFram, text = "    ", font = "arial 35" , bg = "black").grid( column = c , row = r )

    else:
        l1= Label(miFram, text = "    " , font = "arial 35" ).grid( column = c , row = r )
        c = c + 1
        l1= Label(miFram, text = "    ", font = "arial 35" , bg = "black").grid( column = c , row = r )


ventana = Tk()
miFrame = Frame(ventana, width=1200, height=600)
miFrame.pack()

ventana1 = Tk()
miFram = Frame(ventana1, width=1200, height=600)
miFram.pack()

img = Image.open('Update.png')
img = img.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)

imgup = Image.open('arrowup.png')
imgup = imgup.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgup = ImageTk.PhotoImage(imgup)

imgdo = Image.open('arrowdown.png')
imgdo = imgdo.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgdo = ImageTk.PhotoImage(imgdo)

imgle = Image.open('arrowleft.png')
imgle = imgle.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgle = ImageTk.PhotoImage(imgle)

imgri = Image.open('arrowright.png')
imgri = imgri.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgri = ImageTk.PhotoImage(imgri)

for f in range(0,fm):
    for c in range(0,cm):
        l1 = Label(miFram, text = "", font = "arial 35", width = 3 , height = 1).grid( column = c , row = f )

b1 = Button(miFrame, image = img  , command = updat).grid( column = 1 , row = 1)
b2 = Button(miFrame, image = imgup, command = up   ).grid( column = 1 , row = 0)
b3 = Button(miFrame, image = imgdo, command = down ).grid( column = 1 , row = 2)
b4 = Button(miFrame, image = imgle, command = left ).grid( column = 0 , row = 1)
b5 = Button(miFrame, image = imgri, command = right).grid( column = 2 , row = 1)

miFrame.mainloop()