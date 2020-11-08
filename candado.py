#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random 
"""Se define de forma aleatoria una clave para un candado de cuatro digitos enteros y positivos."""
def definirClave(): 
    
    clave = str(random.randint(0000,9999)).zfill(4)
   
    return clave

""" Pre: se recibe la clave de un candado y se compara con una posible contraseña hasta dar con la correcta.
    Aclaración: la clave hace referencia a los dígitos correctos con los cuales se abre el candado.
    Post: Se devuelve la cantidad de intentos efectuados hasta que coincidan clave y contraseña probada.  """
def realizarExperimento(): 
   
    clave = definirClave()
    contrasenia =  str(0).zfill(4)    
    intentos = 1
    while(clave != contrasenia): 
        intentos+=1
        contrasenia = int(contrasenia)+1
        contrasenia = str(contrasenia).zfill(4)
        
    print(intentos)    
    return intentos

"Se realizan la cantidad indicada de experimentos, en este caso, 100.000"
def experimentos():
    
    datos = []
    maxExperimentos = 10
    cantidadExperimentos = 0
    
    print(type(maxExperimentos))
    print(type(cantidadExperimentos))
    while(cantidadExperimentos < maxExperimentos):
        intento = realizarExperimento()
        cantidadExperimentos+=1
       # print(cantidadExperimentos)
        datos.append((cantidadExperimentos,intento))
        print(datos)
    
        
experimentos() 
