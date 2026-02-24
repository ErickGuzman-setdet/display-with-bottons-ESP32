from machine import Pin
import time

# ---- Establecemos los segmentos del Display ABC---
A = Pin(2, Pin.OUT)
B = Pin(4, Pin.OUT)
C = Pin(5, Pin.OUT)
D = Pin(18, Pin.OUT)
E = Pin(19, Pin.OUT)
F = Pin(13, Pin.OUT)
G = Pin(12, Pin.OUT)

# ---- Los guardamos en un arreglo -------
segmentos = [A,B,C,D,E,F,G]

# ---- Tabla que me diste ----
numeros = [
    [1,1,1,1,1,1,0], #0
    [0,1,1,0,0,0,0], #1
    [1,1,0,1,1,0,1], #2
    [1,1,1,1,0,0,1], #3
    [0,1,1,0,0,1,1], #4
    [1,0,1,1,0,1,1], #5
    [1,0,1,1,1,1,1], #6
    [1,1,1,0,0,0,0], #7
    [1,1,1,1,1,1,1], #8
    [1,1,1,1,0,1,1], #9
    [1,1,1,0,1,1,1], #A
    [0,0,1,1,1,1,1], #B
    [1,0,0,1,1,1,0], #C
    [0,1,1,1,1,0,1], #D
    [1,0,0,1,1,1,1], #E
    [1,0,0,0,1,1,1]  #F
]

# ---- Pines de Botones en ESP32 ----
boton_up   = Pin(14, Pin.IN, Pin.PULL_UP)
boton_down = Pin(27, Pin.IN, Pin.PULL_UP)

numero = 0

def mostrar(n):
    for i in range(7): # 7 segmentos 
        segmentos[i].value(numeros[n][i]) #selecciona y asigna el Pin y el valor 0 o 1 para encender/apagar

mostrar(numero)

#Como son 16 segmentos diferentes solamente, cuando llegue al final del arreglo de segmentos el residuo sea 0
# Esto hace un ciclo de 0 hasta 16, y de 16 a 0 y asi 
while True:
    if boton_up.value() == 0:
        numero = (numero + 1) % 16
        mostrar(numero)   #Muestra 
        time.sleep(0.30)
    
    if boton_down.value() == 0:
        numero = (numero - 1) % 16
        mostrar(numero)
        time.sleep(0.30)
