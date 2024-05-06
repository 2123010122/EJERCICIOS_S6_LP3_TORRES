# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:08:31 2024

@author: Dell
"""

# Importamos la libreria
import camelcase

nombre = "henry fabian torres Guzman"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'henry' y 'fabian' 
cam2 = camelcase.CamelCase('henry','fabian')
print(cam2.hump(nombre))


