from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
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
    resultados.configure(background='white')

    E2=Label(resultados,text="Cajas chicas")
    E2.grid(column=1,row=1,sticky="e",padx=10,pady=10)
    E3=Label(resultados,text="Cajas medianas")
    E3.grid(column=2,row=1,sticky="e",padx=10,pady=10)
    E1=Label(resultados,text="cajas grandes")
    E1.grid(column=3,row=1,sticky="e",padx=10,pady=10)
    E1=Label(resultados,text="Total de cajas")
    E1.grid(column=4,row=1,sticky="e",padx=10,pady=10)

    E2=Label(resultados,text=c)
    E2.grid(column=1,row=2,sticky="e",padx=10,pady=10)
    E2=Label(resultados,text=m)
    E2.grid(column=2,row=2,sticky="e",padx=10,pady=10)
    E2=Label(resultados,text=g)
    E2.grid(column=3,row=2,sticky="e",padx=10,pady=10)
    E2=Label(resultados,text=c+m+g)
    E2.grid(column=4,row=2,sticky="e",padx=10,pady=10)

def bienvenido():    
    boton1=tk.Button(principal,text='Ingresar cajas',command=menuprincipal)
    boton1.grid(column=0,row=1,sticky="e",padx=10,pady=10)

def menuprincipal():
    E2=Label(principal,text="Seleccione la opcion deceada")
    E2.grid(columnspan=3,row=0,sticky="e",padx=10,pady=10)
    
    boton1=tk.Button(principal,text='Caja chica',command=BoxCH)
    boton1.grid(column=1,row=1,sticky="e",padx=10,pady=10)
    boton2=tk.Button(principal,text='Caja mediana',command=BoxM)
    boton2.grid(column=2,row=1,sticky="e",padx=10,pady=10)
    boton3=tk.Button(principal,text='Caja grande',command=BoxG)
    boton3.grid(column=3,row=1,sticky="e",padx=10,pady=10)
    boton4=tk.Button(principal,text='Terminar pedido',command=destroy)
    boton4.grid(column=2,row=2,sticky="e",padx=10,pady=10)

principal=tk.Tk()
principal.title("EXAMEN S.A. DE C.V.")
principal.geometry("450x150")
principal.configure(background='white')
bienvenido()

principal.mainloop()
