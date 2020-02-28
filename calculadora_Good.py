#ITC Instituto Tecnologico Nacional de Mexico en Celaya
#by: Sotelo Pacheco José Manuel
#Fecha: Jueves 27 de febrero del 2020
#Programación avanzada


from tkinter import *

numero = ""

# operaciones necesaria para la calculadora
def digito(num):
    global numero
    numero = numero + str(num)
    x.set(numero)

def r():
    try:
        global numero
        total = str(eval(numero)) # eval () evalua operaciones del tipo str
        x.set(total)
        
    except:
        valor =  x.get()
        total = str(eval(valor)) # eval () evalua operaciones del tipo str
        x.set(total)

def limpiar():
    global numero
    numero = ""
    x.set("")

ventana = Tk()
ventana.title("Welcome to calculator")
ventana.configure(background='white')
x = StringVar()
resultado = Entry(ventana , textvariable = x,font = "arial 30",justify="right").grid(columnspan = 4,row = 0, padx = 10 , pady = 10)

#creacion de botones para numeros
label = Button(ventana, text = "1" ,font = "arial 30" , command = lambda: digito(1)).grid(column = 1, row = 1 , padx = 10 ,pady = 10)
label = Button(ventana, text = "2" ,font = "arial 30" , command = lambda: digito(2)).grid(column = 2, row = 1 , padx = 10 ,pady = 10)
label = Button(ventana, text = "3" ,font = "arial 30" , command = lambda: digito(3)).grid(column = 3, row = 1 , padx = 10 ,pady = 10)
label = Button(ventana, text = "4" ,font = "arial 30" , command = lambda: digito(4)).grid(column = 1, row = 2 , padx = 10 ,pady = 10)
label = Button(ventana, text = "5" ,font = "arial 30" , command = lambda: digito(5)).grid(column = 2, row = 2 , padx = 10 ,pady = 10)
label = Button(ventana, text = "6" ,font = "arial 30" , command = lambda: digito(6)).grid(column = 3, row = 2 , padx = 10 ,pady = 10)
label = Button(ventana, text = "7" ,font = "arial 30" , command = lambda: digito(7)).grid(column = 1, row = 3 , padx = 10 ,pady = 10)
label = Button(ventana, text = "8" ,font = "arial 30" , command = lambda: digito(8)).grid(column = 2, row = 3 , padx = 10 ,pady = 10)
label = Button(ventana, text = "9" ,font = "arial 30" , command = lambda: digito(9)).grid(column = 3, row = 3 , padx = 10 ,pady = 10)
label = Button(ventana, text = "0" ,font = "arial 30" , command = lambda: digito(0)).grid(column = 2, row = 4 , padx = 10 ,pady = 10)

#creaciond e botones para operaciones
label = Button(ventana, text = "ca" ,font = "arial 25" , command = limpiar).grid(column = 4, row = 0 , padx = 10 ,pady = 10)
label = Button(ventana, text = "." ,font = "arial 30" , command = lambda: digito(".")).grid(column = 1, row = 4 , padx = 10 ,pady = 10)
label = Button(ventana, text = "=" ,font = "arial 30" , command = r).grid(column = 3, row = 4 , padx = 10 ,pady = 10)
label = Button(ventana, text = "+" ,font = "arial 30" , command = lambda: digito("+")).grid(column = 4, row = 1 , padx = 10 ,pady = 10)
label = Button(ventana, text = "-" ,font = "arial 30" , command = lambda: digito("-")).grid(column = 4, row = 2 , padx = 10 ,pady = 10)
label = Button(ventana, text = "*" ,font = "arial 30" , command = lambda: digito("*")).grid(column = 4, row = 3 , padx = 10 ,pady = 10)
label = Button(ventana, text = "/" ,font = "arial 30" , command = lambda: digito("/")).grid(column = 4, row = 4 , padx = 10 ,pady = 10)

ventana.mainloop()
