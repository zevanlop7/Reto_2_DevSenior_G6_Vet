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

#clases principales
class SistemaVeterinaria:     # se crea una clase llamado SistemaVeterianaria

    class Persona:            # se crea una clase Persona
        id_counter = 1                                          #se iniciara el contador para personas en 1
        def __init__(self, nombre, contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre                                # variable que almacenara el nombre de la persona
            self.contacto = contacto                            # variable que almacenara el telefono de la persona
            SistemaVeterinaria.Persona.id_counter += 1          # el contador se autoincrementara a medida que se cree una persona

    class Cliente(Persona):    #se crea una clase cliente que hereda de la clase Persona
        def __init__(self, nombre, contacto, direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []   # el cliente tiene vinculada una mascota   #ojo

        #def agregar_cliente(self, cliente):
            #self.cliente.append(cliente)
        
        def agregar_mascota(self, mascota):
            self.mascotas.append(mascota)              #se quito self.mascota

        def mostrar_informacion(self):
            return f"cliente: {self.nombre}, contacto{self.contacto}, direccion: {self.direccion}"  # función para mostrar informacion del cliente 

