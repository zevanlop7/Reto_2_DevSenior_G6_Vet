#GestióndeClientesyMascotasReto 2 - Gestión de Veterinaria usandoProgramación Orientada a Objetos (Terminal)
#Integrantes: Daniela Palechor y Ever Lopez
from abc import ABC, abstractmethod
from datetime import datetime
import re   #libreria para crear patrones y realizar comparaciones

#Variables globales
clientes = []
mascotas = []
servicios = ["consulta", "vacunación", "esterilizacion", "spa"]
#clientes = [
#    Cliente(1, "Daniela Palechor", "3124567852", "calle 5 Nro. 26-45"),
#    Cliente(2, "Andres Agudelo", "3145824653", "calle 4 Nro. 23-36")
#]
#mascotas = []
"""mascotas = [
    Mascota(1, "Toby", "Perro", "Pastor Aleman", "3"),
    Mascota(2, "lucita", "Perro", "Crillo", "5")
]   """

