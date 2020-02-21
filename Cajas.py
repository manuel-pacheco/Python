from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
from tkinter import PhotoImage
global c
global m
global g

c=0
m=0
g=0

def BoxCH():
    global c
    c+=1
    
def BoxM():
    global m
    m+=1
    
def BoxG():
    global g
    g+=1

def destroy():
    global c
    global m
    global g
    
    principal.destroy()
    resultados= Tk()
    resultados.title("Resultados ingresados de cajas")
    resultados.geometry("450x150")
    resultados.configure(background='peach puff')

    E2=Label(resultados,text="Cajas Chicas", bg="dark slate gray",fg="white")
    E2.grid(column=1,row=1,sticky="e",padx=10,pady=10)
    E3=Label(resultados,text="Cajas Medianas", bg="dark slate gray",fg="white")
    E3.grid(column=2,row=1,sticky="e",padx=10,pady=10)
    E1=Label(resultados,text="Cajas Grandes", bg="dark slate gray",fg="white")
    E1.grid(column=3,row=1,sticky="e",padx=10,pady=10)
    E1=Label(resultados,text="Total de cajas", bg="dark slate gray",fg="white")
    E1.grid(column=4,row=1,sticky="e",padx=10,pady=10)

    E2=Label(resultados,text=c, bg="aquamarine4",fg="white")
    E2.grid(column=1,row=2,sticky="e",padx=10,pady=10)
    E2=Label(resultados,text=m, bg="aquamarine4",fg="white")
    E2.grid(column=2,row=2,sticky="e",padx=10,pady=10)
    E2=Label(resultados,text=g, bg="aquamarine4",fg="white")
    E2.grid(column=3,row=2,sticky="e",padx=10,pady=10)
    E2=Label(resultados,text=c+m+g, bg="tan",fg="black")
    E2.grid(column=4,row=2,sticky="e",padx=10,pady=10)

def bienvenido():    
    boton1=tk.Button(principal,text='Ingresar cajas',command=menuprincipal,fg="blue")
    boton1.grid(column=0,row=1,sticky="e",padx=10,pady=10)

def menuprincipal():
    global c
    global m
    global g
    
    E2=Label(principal,text="Seleccione la opcion deceada")
    E2.grid(columnspan=3,row=0,sticky="e",padx=10,pady=10)
    E2=Label(principal,text=c)
    E2.grid(column=1,row=2,sticky="e",padx=10,pady=10)
    E2=Label(principal,text=m)
    E2.grid(column=2,row=2,sticky="e",padx=10,pady=10)
    E2=Label(principal,text=g)
    E2.grid(column=3,row=2,sticky="e",padx=10,pady=10)
    

    
    boton1=tk.Button(principal,text='Caja Chica',command=BoxCH,fg="blue")
    boton1.grid(column=1,row=1,sticky="e",padx=10,pady=10)
    boton2=tk.Button(principal,text='Caja Mediana',command=BoxM,fg="dark green")
    boton2.grid(column=2,row=1,sticky="e",padx=10,pady=10)
    boton3=tk.Button(principal,text='Caja Grande',command=BoxG,fg="gold")
    boton3.grid(column=3,row=1,sticky="e",padx=10,pady=10)
    boton4=tk.Button(principal,text='Terminar Pedido',command=destroy,fg="blue")
    boton4.grid(column=2,row=3,sticky="e",padx=10,pady=10)
    E2.after(1000,menuprincipal)

principal=tk.Tk()
principal.title("EXAMEN S.A. DE C.V.")
principal.geometry("500x190")

image=tk.PhotoImage(file="tecno.gif")
image=image.subsample(1,1)
label=tk.Label(image=image).place(x=0,y=0)


bienvenido()

principal.mainloop()
