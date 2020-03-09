#ITC Instituto Tecnologico Nacional de Mexico en Celaya
#by: Sotelo Pacheco José Manuel
#Fecha: Jueves 05 de febrero del 2020
#Programación avanzada

import cv2

# cargar el archivo PNG indicado
img = cv2.imread('unnamed.gif')

# mostrar la imagen en una ventana
cv2.imshow('titulo', img)

# esperar hasta que se presiona una tecla
cv2.waitKey(0)
